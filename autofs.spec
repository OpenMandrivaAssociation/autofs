Summary:        A tool for automatically mounting and unmounting filesystems
Name:           autofs
Version:        5.0.7
Release:        14
License:        GPLv2+
Group:          System/Kernel and hardware
Url:            ftp://ftp.kernel.org/pub/linux/daemons/autofs
Source0:        ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-%{version}.tar.bz2
Patch102:       autofs-5.0.6-separate-config-files.patch
Patch103:       autofs-5.0.4-rename-configuration-file.patch
Patch104:	autofs-5.0.7-do-not-install-init.patch
Patch105:	autofs-5.0.7-after-nss-lookup.patch
Patch106:	autofs-5.0.7-add-missing-libtirpc-linkage.patch

BuildRequires:  bison
BuildRequires:  flex
BuildRequires:	kmod-compat
BuildRequires:  krb5-devel
BuildRequires:  openldap-devel
BuildRequires:  sasl-devel
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
%apply_patches
autoreconf -fi

%build
%serverbuild
export CFLAGS="%{optflags} -fPIC"
%configure2_5x \
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
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_libdir}/autofs
mkdir -p %{buildroot}%{_mandir}/{man5,man8}
mkdir -p %{buildroot}%{_sysconfdir}

%make install INSTALLROOT=%{buildroot}

install -d -m 755 %{buildroot}%{_unitdir}
install -m 644 samples/autofs.service %{buildroot}%{_unitdir}/autofs.service

rm -f %{buildroot}%{_sysconfdir}/init.d/%{name}
rm -f %{buildroot}%{_mandir}/man8/autofs*

cat > README.urpmi <<EOF
%{distribution} specific notes

setup
-----
Configuration handling in %{distribution} package differs from upstream one on several
points:
- the automounts daemon configuration file is %{_sysconfdir}/autofs/autofs.conf
- the autofs service configuration file is %{_sysconfdir}/sysconfig/autofs

Upgrade
-------
Map files have been moved from %{_sysconfdir} to %{_sysconfdir}/autofs. Upgrade
procedure should handle the change automatically.
LDAP usage has changed between autofs 4 and 5. The LDAP schema used has now to
be configured explicitely in autofs configuration, so as to avoid useless
queries. As this can't be handled by package upgrade procedure, you'll have to
edit your configuration manually. See auto.master(5) for details.

EOF

# tune default configuration
perl -pi -e 's|^BROWSE_MODE="no"|BROWSE_MODE="yes"|' \
    %{buildroot}%{_sysconfdir}/autofs/autofs.conf
perl -pi \
    -e 's|^/misc\t|#/misc\t|;' \
    -e 's|^/net\t|#/net\t|;' \
    %{buildroot}%{_sysconfdir}/autofs/auto.master

%post
%_post_service autofs

%preun
%_preun_service autofs

%files
%doc INSTALL CHANGELOG CREDITS README* examples
%config(noreplace) %{_sysconfdir}/autofs
%config(noreplace) %{_sysconfdir}/sysconfig/autofs
%{_unitdir}/autofs.service
%{_libdir}/%{name}
%{_sbindir}/automount
%{_mandir}/*/*

