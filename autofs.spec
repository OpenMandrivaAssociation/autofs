%define name    autofs
%define version 5.0.2
%define release %mkrel 8

Name:           %{name}
Version:        %{version}
Release:        %{release}
License:        GPL
Summary:        A tool for automatically mounting and unmounting filesystems
Group:          System/Kernel and hardware
URL:            ftp://ftp.kernel.org/pub/linux/daemons/autofs
Source0:        ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/autofs-%{version}.tar.bz2
Source1:        %{name}.init
Source2:        ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/autofs-%{version}.tar.bz2.sign
Patch0:     autofs-5.0.2-add-krb5-include.patch
Patch1:     autofs-5.0.2-bad-proto-init.patch
Patch2:     autofs-5.0.2-add-missing-multi-support.patch
Patch3:     autofs-5.0.2-add-multi-nsswitch-lookup.patch
Patch4:     autofs-5.0.2-consistent-random-selection-option-name.patch
Patch5:     autofs-5.0.2-fix-offset-dir-create.patch
Patch6:     autofs-5.0.2-quote-exports.patch
Patch7:     autofs-5.0.2-hi-res-time.patch
Patch8:     autofs-5.0.2-quoted-slash-alone.patch
Patch9:     autofs-5.0.2-fix-dnattr-parse.patch
Patch10:    autofs-5.0.2-fix-nfs-version-in-get-supported-ver-and-cost.patch
Patch11:    autofs-5.0.2-instance-stale-mark.patch
Patch12:    autofs-5.0.2-fix-largefile-dumbness.patch
Patch13:    autofs-5.0.2-dont-fail-on-empty-master.patch
Patch14:    autofs-5.0.2-ldap-percent-hack.patch
Patch15:    autofs-5.0.2-fix-mount-nfs-nosymlink.patch
Patch16:    autofs-5.0.2-dont-fail-on-empty-master-fix.patch
Patch17:    autofs-5.0.2-default-nsswitch.patch
Patch18:    autofs-5.0.2-add-ldap-schema-discovery.patch
Patch19:    autofs-5.0.2-random-selection-fix.patch
Patch20:    autofs-5.0.2-timeout-option-parse-fix.patch
Patch21:    autofs-5.0.2-ldap-check-star.patch
Patch22:    autofs-5.0.2-add-ldap-schema-discovery-fix.patch
Patch23:    autofs-5.0.2-ldap-schema-discovery-config-update.aptch
Patch24:    autofs-5.0.2-ldap-search-basedn-list.patch
Patch25:    autofs-5.0.2-libxml2-workaround.patch
Patch26:    autofs-5.0.2-reread-config-on-hup.patch
Patch27:    autofs-5.0.2-add-multiple-server-selection-option.patch
Patch28:    autofs-5.0.2-foreground-logging.patch
Patch29:    autofs-5.0.2-cleanup-krb5-comment.patch
Patch30:    autofs-5.0.2-submount-deadlock.patch
Patch31:    autofs-5.0.2-add-ferror-check.patch
Patch32:    autofs-5.0.2-autofs-5-typo.patch
Patch33:    autofs-5.0.2-swallow-null-macro.patch
Patch34:    autofs-5.0.2-remove-unsed-export-validation-code.patch
Patch35:    autofs-5.0.2-dynamic-logging.patch
Patch36:    autofs-5.0.2-fix-recursive-loopback-mounts.patch
Patch37:    autofs-5.0.2-log-map-reload.patch
Patch38:    autofs-5.0.2-basedn-with-spaces.patch
Patch39:    autofs-5.0.2-dynamic-logging-fixes.patch
Patch40:    autofs-5.0.2-basedn-with-spaces-fix.patch
Patch41:    autofs-5.0.2-check-mtab-updated.patch
Patch42:    autofs-5.0.2-basedn-with-spaces-fix-2.patch
Patch43:    autofs-5.0.2-master-check-underscore.patch
Patch44:    autofs-5.0.2-add-ldap-schema-discovery-fix-2.patch
Patch101:       autofs-5.0.2-set-default-browse-mode.patch
Patch102:       autofs-5.0.2-separate-config-files.patch
Patch103:       autofs-5.0.2-rename-configuration-file.patch
Patch105:       autofs-5.0.1-rc3-comment-default-master-map.patch
Requires:       nfs-utils-clients
Requires:       kernel >= 2.6.17
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
%patch0 -p 1
%patch1 -p 1
%patch2 -p 1
%patch3 -p 1
%patch4 -p 1
%patch5 -p 1
%patch6 -p 1
%patch7 -p 1
%patch8 -p 1
%patch9 -p 1
%patch10 -p 1
%patch11 -p 1
%patch12 -p 1
%patch13 -p 1
%patch14 -p 1
%patch15 -p 1
%patch16 -p 1
%patch17 -p 1
%patch18 -p 1
%patch19 -p 1
%patch20 -p 1
%patch21 -p 1
%patch22 -p 1
%patch23 -p 1
%patch24 -p 1
%patch25 -p 1
%patch26 -p 1
%patch27 -p 1
%patch28 -p 1
%patch29 -p 1
%patch30 -p 1
%patch31 -p 1
%patch32 -p 1
%patch33 -p 1
%patch34 -p 1
%patch35 -p 1
%patch36 -p 1
%patch37 -p 1
%patch38 -p 1
%patch39 -p 1
%patch40 -p 1
%patch41 -p 1
%patch42 -p 1
%patch43 -p 1
%patch44 -p 1
%patch101 -p 1
%patch102 -p 1
%patch103 -p 1
%patch105 -p 1

%build
autoconf
%serverbuild
%configure2_5x --with-mapdir=%{_sysconfdir}/%{name} \
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
