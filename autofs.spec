%define _disable_lto 1
%define _disable_ld_no_undefined 1

Summary:        A tool for automatically mounting and unmounting filesystems
Name:           autofs
Version:	5.1.8
Release:	1
License:        GPLv2+
Group:          System/Kernel and hardware
Url:            http://kernel.org/pub/linux/daemons/autofs
Source0:        http://kernel.org/pub/linux/daemons/autofs/v5/%{name}-%{version}.tar.xz
Patch102:       autofs-5.0.6-separate-config-files.patch
Patch104:	autofs-5.0.7-do-not-install-init.patch

BuildRequires:  bison
BuildRequires:  flex
BuildRequires:	kmod-compat
BuildRequires:  krb5-devel
BuildRequires:  openldap-devel
BuildRequires:  sasl-devel
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libtirpc)
BuildRequires:  pkgconfig(libxml-2.0)
Requires(post,preun):  rpm-helper >= 0.24.1-1
Conflicts:      autosmb

%description
autofs is a daemon which automatically mounts filesystems when you use
them, and unmounts them later when you are not using them.  This can
include network filesystems, CD-ROMs, floppies, and so forth.

%prep
%setup -q
%autopatch -p1
autoreconf -fi

%build
%serverbuild
export CFLAGS="%{optflags} -fPIC"
%configure \
	--with-mapdir=%{_sysconfdir}/%{name} \
	--with-confdir=%{_sysconfdir}/%{name} \
	--with-sasl=yes \
	--disable-mount-locking \
	--enable-ignore-busy \
	--with-libtirpc \
	--disable-mount-move \
	--with-systemd

%make DONTSTRIP=1

mkdir examples
cp samples/ldap* examples
cp samples/autofs.schema examples

rm -f README.gentoo

%install
install -d -m 755 %{buildroot}%{_unitdir}
mkdir -p -m755 %{buildroot}%{_sbindir}
mkdir -p -m755 %{buildroot}%{_libdir}/autofs
mkdir -p -m755 %{buildroot}%{_mandir}/{man5,man8}
mkdir -p -m755 %{buildroot}/etc/sysconfig
mkdir -p -m755 %{buildroot}/etc/auto.master.d

make install mandir=%{_mandir} initdir=%{_initrddir} systemddir=%{_unitdir} INSTALLROOT=%{buildroot}
echo make -C redhat
make -C redhat
install -m 755 -d %{buildroot}/misc
# Configure can get this wrong when the unit files appear under /lib and /usr/lib
find %{buildroot} -type f -name autofs.service -exec rm -f {} \;
install -m 644 redhat/autofs.service %{buildroot}%{_unitdir}/autofs.service
%define init_file_name %{_unitdir}/autofs.service
install -m 644 redhat/autofs.conf %{buildroot}/etc/autofs.conf
install -m 644 redhat/autofs.sysconfig %{buildroot}/etc/sysconfig/autofs

install -m 644 samples/auto.master %{buildroot}/etc/auto.master
install -m 644 samples/auto.misc %{buildroot}/etc/auto.misc
install -m 755 samples/auto.net %{buildroot}/etc/auto.net
install -m 755 samples/auto.smb %{buildroot}/etc/auto.smb
install -m 600 samples/autofs_ldap_auth.conf %{buildroot}/etc/autofs_ldap_auth.conf

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%triggerun -- %{name} < 5.0.6-5
# Save the current service runlevel info
# User must manually run systemd-sysv-convert --apply %{name}
# to migrate them to systemd targets
%{_bindir}/systemd-sysv-convert --save %{name} >/dev/null 2>&1 ||:

# Run these because the SysV package being removed won't do them
%{_sbindir}/chkconfig --del %{name} >/dev/null 2>&1 || :
%{_bindir}/systemctl try-restart %{name}.service >/dev/null 2>&1 || :

%files
%doc CREDITS INSTALL COPY* README* samples/ldap* samples/autofs.schema
%{_unitdir}/%{name}.service
%config(noreplace,missingok) /etc/auto.master
%config(noreplace) /etc/autofs.conf
%config(noreplace,missingok) /etc/auto.misc
%config(noreplace,missingok) /etc/auto.net
%config(noreplace,missingok) /etc/auto.smb
%config(noreplace) /etc/sysconfig/autofs
%config(noreplace) /etc/autofs_ldap_auth.conf
%{_sbindir}/automount
%{_mandir}/*/*
%{_libdir}/autofs/
%{_libdir}/libautofs.so
%dir /etc/auto.master.d
