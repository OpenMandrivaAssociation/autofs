Name:           autofs
Version:        5.0.7
Release:        %mkrel 3
License:        GPLv2+
Summary:        A tool for automatically mounting and unmounting filesystems
Group:          System/Kernel and hardware
URL:            ftp://ftp.kernel.org/pub/linux/daemons/autofs
Source0:        ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/autofs-%{version}.tar.bz2
Patch0:		autofs-5.0.6-fix-libtirpc-name-clash.patch
Patch102:       autofs-5.0.6-separate-config-files.patch
Patch103:       autofs-5.0.4-rename-configuration-file.patch
Patch104:	autofs-5.0.7-do-not-install-init.patch
Patch105:	autofs-5.0.7-after-nss-lookup.patch
BuildRequires:  openldap-devel
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  libsasl-devel
BuildRequires:  krb5-devel
BuildRequires:  libxml2-devel
BuildRequires:  tirpc-devel
BuildRequires:	kmod-compat
Conflicts:      autosmb
Requires(post):  rpm-helper >= 0.24.1-1
Requires(preun): rpm-helper >= 0.24.1-1

%description
autofs is a daemon which automatically mounts filesystems when you use
them, and unmounts them later when you are not using them.  This can
include network filesystems, CD-ROMs, floppies, and so forth.

%prep
%setup -q
%patch0 -R -p1
%patch102 -p1
%patch103 -p1
%patch104 -p0
%patch105 -p1
autoreconf -f -i

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
rm -rf %{buildroot}
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
ROSA RPM specific notes

setup
-----
Configuration handling in ROSA package differs from upstream one on several
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
