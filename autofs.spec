%define name    autofs
%define version 5.0.1
%define release %mkrel 2

Name:           %{name}
Version:        %{version}
Release:        %{release}
License:        GPL
Summary:        A tool for automatically mounting and unmounting filesystems
Group:          System/Kernel and hardware
URL:            ftp://ftp.kernel.org/pub/linux/daemons/autofs
Source0:        ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/autofs-%{version}.tar.bz2
Source1:        %{name}.init
Patch100:       autofs-5.0.1-rc1-fix-man-page.patch
Patch101:       autofs-5.0.1-rc1-drop-default-prefix-from-config.patch
Patch102:       autofs-5.0.1-rc3-separate-config-files.patch
Patch103:       autofs-5.0.1-rc1-cleanup-config-files-names.patch
Patch105:       autofs-5.0.1-rc3-comment-default-master-map.patch
Patch200:       autofs-5.0.1-rc1-fix-hesiod-check.patch
Requires:       nfs-utils-clients
Requires:       kernel >= 2.6.17
Requires(post): rpm-helper
Requires(preun):rpm-helper
BuildRequires:  openldap-devel
BuildRequires:  flex
BuildRequires:  bison
Conflicts:      autosmb
Buildroot:      %{_tmppath}/%{name}-%{version}

%description
autofs is a daemon which automatically mounts filesystems when you use
them, and unmounts them later when you are not using them.  This can
include network filesystems, CD-ROMs, floppies, and so forth.

%prep
%setup -q -n %{name}-%{version}
%patch100 -p 1
%patch101 -p 1
%patch102 -p 1
%patch103 -p 1
%patch105 -p 1
%patch200 -p 1

%build
autoconf-2.5x
%serverbuild
%configure --with-mapdir=%{_sysconfdir}/%{name} \
           --with-confdir=%{_sysconfdir}/%{name} \
           --with-sasl=no
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

install -d -m 755 %{buildroot}%{_initrddir}
install -m 755 %{SOURCE1} %{buildroot}%{_initrddir}/%{name}

rm -f %{buildroot}%{_sysconfdir}/init.d/%{name}

cat > README.urpmi <<EOF
Mandriva RPM specific notes

setup
-----
The configuration files setup differs from default one, by separating daemon
configuration file (%{_sysconfdir}/autofs/autofs.conf) from initscript
configuration file (%{_sysconfdir}/sysconfig/autofs).

Upgrade
-------
Map files have been moved from %{_sysconfdir} to %{_sysconfdir}/autofs. Upgrade
procedure should handle the change automatically.
LDAP usage has changed between autofs 4 and 5. The LDAP schema used has now to
be configured explicitely in autofs configuration, so as to avoid useless
queries. As this can't be handled by package upgrade procedure, you'll have to
edit your configuration manually. See auto.master(5) for details.

EOF

%pre
if [ $1 = "0" ]; then
    # installation
    if grep -q '^alias autofs autofs4'  /etc/modules.conf; then
    echo "alias autofs autofs4" >> /etc/modules.conf
    fi
else
    if [ ! -d %{_sysconfdir}/autofs ]; then
        # 4 -> 5 upgrade
        mkdir %{_sysconfdir}/autofs
        for file in %{_sysconfdir}/auto.{master,misc,net,smb}; do
            if [ -f "$file" ]; then
                mv $file* %{_sysconfdir}/autofs
            fi
        done
    fi
fi

%post
%_post_service autofs

%preun
%_preun_service autofs

%postun
if [ $1 = "0" ]; then # removal
    perl -ni -e 'print unless ( m!^.*autofs.*$! || /^\s*$/)' /etc/modules.conf
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc INSTALL CHANGELOG CREDITS README* examples
%config(noreplace) %{_sysconfdir}/autofs
%config(noreplace) %{_sysconfdir}/sysconfig/autofs
%{_initrddir}/%{name}
%{_libdir}/%{name}
%{_sbindir}/automount
%{_mandir}/*/*


