%define name    autofs
%define version 5.0.4
%define release %mkrel 3

Name:           %{name}
Version:        %{version}
Release:        %{release}
License:        GPL
Summary:        A tool for automatically mounting and unmounting filesystems
Group:          System/Kernel and hardware
URL:            ftp://ftp.kernel.org/pub/linux/daemons/autofs
Source0:        ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/autofs-%{version}.tar.bz2
Source1:        %{name}.init
# this one is needed for ldap support
Patch46:        autofs-5.0.4-link-with-kerberos-lib.patch
Patch101:       autofs-5.0.2-set-default-browse-mode.patch
Patch102:       autofs-5.0.4-separate-config-files.patch
Patch103:       autofs-5.0.4-rename-configuration-file.patch
Patch105:       autofs-5.0.3-comment-default-master-map.patch
Patch201:       autofs-5.0.4-fix-dumb-libxml2-check.patch
Patch202:       autofs-5.0.4-expire-specific-submount-only.patch
Patch203:       autofs-5.0.4-fix-negative-cache-non-existent-key.patch
Patch204:       autofs-5.0.4-fix-ldap-detection.patch
Patch205:       autofs-5.0.4-use-CLOEXEC-flag.patch
Patch206:       autofs-5.0.4-fix-select-fd-limit.patch
Patch207:       autofs-5.0.4-make-hash-table-scale-to-thousands-of-entries.patch
Patch208:       autofs-5.0.4-fix-quoted-mess.patch
Patch209:       autofs-5.0.4-fix-hosts-map-use-after-free.patch
Conflicts:       kernel < 2.6.17
Requires(post): rpm-helper
Requires(preun):rpm-helper
BuildRequires:  openldap-devel
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  libsasl-devel
BuildRequires:  krb-devel
BuildRequires:  libxml2-devel
Conflicts:      autosmb
Buildroot:      %{_tmppath}/%{name}-%{version}

%description
autofs is a daemon which automatically mounts filesystems when you use
them, and unmounts them later when you are not using them.  This can
include network filesystems, CD-ROMs, floppies, and so forth.

%prep
%setup -q -n %{name}-%{version}
%patch46 -p 1
%patch101 -p 1
%patch102 -p 1
%patch103 -p 1
%patch105 -p 1
%patch201 -p 1
%patch202 -p 1
%patch203 -p 1
%patch204 -p 1
%patch205 -p 1
%patch206 -p 1
%patch207 -p 1
%patch208 -p 1
%patch209 -p 1

%build
autoreconf
%serverbuild
%configure2_5x --with-mapdir=%{_sysconfdir}/%{name} \
           --with-confdir=%{_sysconfdir}/%{name} \
           --with-sasl=yes
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
rm -f %{buildroot}%{_mandir}/man8/autofs*

cat > README.urpmi <<EOF
Mandriva RPM specific notes

setup
-----
Configuration handling in Mandriva package differs from upstream one on several points:
- the automounts daemon configuration file is %{_sysconfdir}/autofs/autofs.conf
- the autofs service configuration file is %{_sysconfdir}/sysconfig/autofs
- the configuration directives in %{_sysconfdir}/autofs/autofs.conf don't have
  the 'DEFAULT_' prefix (for instance, DEFAULT_TIMEOUT is just TIMEOUT). This
  has recently been changed upstream in version 5.0.2 too, but given than 
  documentation still refers to old names

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
if [ $1 != "0" ]; then
    # upgrade
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
