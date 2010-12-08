%define name    autofs
%define version 5.0.5
%define release %mkrel 4

Name:           %{name}
Version:        %{version}
Release:        %{release}
License:        GPL
Summary:        A tool for automatically mounting and unmounting filesystems
Group:          System/Kernel and hardware
URL:            ftp://ftp.kernel.org/pub/linux/daemons/autofs
Source0:        ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/autofs-%{version}.tar.bz2
Source1:        %{name}.init
Patch01:    autofs-5.0.5-fix-included-map-read-fail-handling.patch
Patch02:    autofs-5.0.5-refactor-ldap-sasl-bind.patch
Patch03:    autofs-5.0.4-add-mount-wait-parameter.patch
Patch04:    autofs-5.0.5-special-case-cifs-escapes.patch
Patch05:    autofs-5.0.5-fix-libxml2-workaround-configure.patch
Patch06:    autofs-5.0.5-more-code-analysis-corrections.patch
Patch07:    autofs-5.0.5-fix-backwards-ifndef-INET6.patch
Patch08:    autofs-5.0.5-fix-stale-init-for-file-map-instance.patch
Patch09:    autofs-5.0.5-fix-ext4-fsck-at-mount.patch
Patch10:    autofs-5.0.5-dont-use-master_lex_destroy-to-clear-parse-buffer.patch
Patch11:    autofs-5.0.5-make-documentation-for-set-log-priority-clearer.patch
Patch12:    autofs-5.0.5-fix-timeout-in-connect_nb.patch
Patch13:    autofs-5.0.5-fix-pidof-init-script-usage.patch
Patch14:    autofs-5.0.5-check-for-path-mount-location-in-generic-module.patch
Patch15:    autofs-5.0.5-dont-fail-mount-on-access-fail.patch
Patch16:    autofs-5.0.5-fix-rpc-large-export-list.patch
Patch17:    autofs-5.0.5-fix-memory-leak-on-reload.patch
Patch18:    autofs-5.0.5-update-kernel-patches-2.6.18-and-2.6.19.patch
Patch19:    autofs-5.0.5-dont-connect-at-ldap-lookup-module-init.patch
Patch20:    autofs-5.0.5-fix-random-selection-option.patch
Patch21:    autofs-5.0.5-fix-disable-timeout.patch
Patch22:    autofs-5.0.5-fix-strdup-return-value-check.patch
Patch23:    autofs-5.0.5-fix-reconnect-get-base-dn.patch
Patch24:    autofs-5.0.5-add-sasl-mutex-callbacks.patch
Patch25:    autofs-5.0.5-fix-get-qdn-fail.patch
Patch26:    autofs-5.0.5-fix-ampersand-escape-in-auto-smb.patch
Patch27:    autofs-5.0.5-add-locality-as-valid-ldap-master-map-attribute.patch
Patch28:	autofs-5.0.5-add-locality-as-valid-ldap-master-map-attribute-fix.patch
Patch29:	autofs-5.0.5-make-nfs4-default-for-redhat-replicated-selection.patch
Patch30:	autofs-5.0.5-add-simple-bind-auth.patch
Patch31:	autofs-5.0.5-fix-master-map-source-server-unavialable-handling.patch
Patch32:	autofs-5.0.5-add-autofs_ldap_auth_conf-man-page.patch
Patch33:	autofs-5.0.5-fix-random-selection-for-host-on-different-network.patch
Patch34:	autofs-5.0.5-make-redhat-init-script-more-lsb-compliant.patch
Patch35:	autofs-5.0.5-dont-hold-lock-for-simple-mounts.patch
Patch36:	autofs-5.0.5-fix-remount-locking.patch
Patch37:	autofs-5.0.5-fix-wildcard-map-entry-match.patch
Patch38:	autofs-5.0.5-fix-parse_sun-module-init.patch
Patch39:	autofs-5.0.5-dont-check-null-cache-on-expire.patch
Patch40:	autofs-5.0.5-fix-null-cache-race.patch
Patch41:	autofs-5.0.5-fix-cache_init-on-source-re-read.patch
Patch42:	autofs-5.0.5-mapent-becomes-negative-during-lookup.patch
Patch43:	autofs-5.0.5-check-each-dc-server.patch
Patch44:	autofs-5.0.5-fix-negative-cache-included-map-lookup.patch
Patch45:	autofs-5.0.5-remove-state-machine-timed-wait.patch
Patch46:	autofs-5.0.5-remove-extra-read-master-map-call.patch
Patch47:	autofs-5.0.5-fix-fix-cache_init-on-source-re-read.patch
Patch48:	autofs-5.0.5-fix-error-handing-in-do_mount_indirect.patch
Patch49:	autofs-5.0.5-expire-thread-use-pending-mutex.patch
Patch50:	autofs-5.0.5-include-krb5-library.patch
Patch51:	autofs-5.0.5-make-verbose-mode-a-little-less-verbose.patch
Patch52:	autofs-5.0.5-remove-ERR_remove_state-openssl-call.patch
Patch53:	autofs-5.0.5-fix-restart.patch
Patch54:	autofs-5.0.5-fix-status-privilege-error.patch
Patch55:	autofs-5.0.4-always-read-file-maps-mount-lookup-map-read-fix.patch
Patch56:	autofs-5.0.5-fix-direct-map-not-updating-on-reread.patch
Patch57:	autofs-5.0.5-add-external-bind-method.patch
Patch58:	autofs-5.0.5-fix-add-simple-bind-auth.patch
Patch59:	autofs-5.0.5-add-dump-maps-option.patch
Patch60:	autofs-5.0.5-fix-submount-shutdown-wait.patch
Patch102:       autofs-5.0.4-separate-config-files.patch
Patch103:       autofs-5.0.4-rename-configuration-file.patch
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
%patch01 -p 1
%patch02 -p 1
%patch03 -p 1
%patch04 -p 1
%patch05 -p 1
%patch06 -p 1
%patch07 -p 1
%patch08 -p 1
%patch09 -p 1
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
%patch45 -p 1
%patch46 -p 1
%patch47 -p 1
%patch48 -p 1
%patch49 -p 1
%patch50 -p 1
%patch51 -p 1
%patch52 -p 1
%patch53 -p 1
%patch54 -p 1
%patch55 -p 1
%patch56 -p 1
%patch57 -p 1
%patch58 -p 1
%patch59 -p 1
%patch60 -p 1
%patch102 -p 1
%patch103 -p 1

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

# tune default configuration
perl -pi -e 's|^BROWSE_MODE="no"|BROWSE_MODE="yes"|' \
    %{buildroot}%{_sysconfdir}/autofs/autofs.conf
perl -pi \
    -e 's|^/misc\t|#/misc\t|;' \
    -e 's|^/net\t|#/net\t|;' \
    %{buildroot}%{_sysconfdir}/autofs/auto.master

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
