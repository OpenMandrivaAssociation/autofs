%define name    autofs
%define version 5.0.4
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
# this one is needed for ldap support
Patch46:        autofs-5.0.4-link-with-kerberos-lib.patch
Patch102:       autofs-5.0.4-separate-config-files.patch
Patch103:       autofs-5.0.4-rename-configuration-file.patch
Patch201:       autofs-5.0.4-fix-dumb-libxml2-check.patch
Patch202:       autofs-5.0.4-expire-specific-submount-only.patch
Patch203:       autofs-5.0.4-fix-negative-cache-non-existent-key.patch
Patch204:       autofs-5.0.4-fix-ldap-detection.patch
Patch205:       autofs-5.0.4-use-CLOEXEC-flag.patch
Patch206:       autofs-5.0.4-fix-select-fd-limit.patch
Patch207:       autofs-5.0.4-make-hash-table-scale-to-thousands-of-entries.patch
Patch208:       autofs-5.0.4-fix-quoted-mess.patch
Patch209:       autofs-5.0.4-use-CLOEXEC-flag-setmntent.patch
Patch210:       autofs-5.0.4-fix-hosts-map-use-after-free.patch
Patch211:       autofs-5.0.4-uris-list-locking-fix.patch
Patch212:       autofs-5.0.4-renew-sasl-creds-upon-reconnect-fail.patch
Patch213:       autofs-5.0.4-library-reload-fix-update.patch
Patch214:       autofs-5.0.4-force-unlink-umount.patch
Patch215:       autofs-5.0.4-always-read-file-maps.patch
Patch216:       autofs-5.0.4-code-analysis-corrections.patch
Patch217:       autofs-5.0.4-make-MAX_ERR_BUF-and-PARSE_MAX_BUF-use-easier-to-audit.patch
Patch218:       autofs-5.0.4-easy-alloca-replacements.patch
Patch219:       autofs-5.0.4-configure-libtirpc.patch
Patch220:       autofs-5.0.4-ipv6-name-and-address-support.patch
Patch221:       autofs-5.0.4-ipv6-parse.patch
Patch222:       autofs-5.0.4-add-missing-changelog-entries.patch
Patch223:       autofs-5.0.4-use-CLOEXEC-flag-setmntent-include-fix.patch
Patch224:       autofs-5.0.4-easy-alloca-replacements-fix.patch
Patch225:       autofs-5.0.4-libxml2-workaround-fix.patch
Patch226:       autofs-5.0.4-configure-libtirpc-fix.patch
Patch227:       autofs-5.0.4-add-nfs-mount-proto-default-conf-option.patch
Patch228:       autofs-5.0.4-fix-bad-token-declare.patch
Patch229:       autofs-5.0.4-fix-return-start-status-on-fail.patch
Patch230:       autofs-5.0.4-fix-double-free-in-expire_proc.patch
Patch231:       autofs-5.0.4-another-easy-alloca-replacements-fix.patch
Patch232:       autofs-5.0.4-add-lsb-init-script-parameter-block.patch
Patch233:       autofs-5.0.4-always-read-file-maps-fix.patch
Patch234:       autofs-5.0.4-use-misc-device.patch
Patch235:       autofs-5.0.4-fix-restorecon.patch
Patch236:       autofs-5.0.4-clear-rpc-client-on-lookup-fail.patch
Patch237:       autofs-5.0.4-fix-lsb-init-script-header.patch
Patch238:       autofs-5.0.4-fix-memory-leak-reading-ldap-master.patch
Patch239:       autofs-5.0.4-fix-st_remove_tasks-locking.patch
Patch240:       autofs-5.0.4-reset-flex-scanner-when-setting-buffer.patch
Patch241:       autofs-5.0.4-zero-s_magic-is-valid.patch
Patch242:       autofs-5.0.4-use-percent-hack-for-master.patch
Patch243:       autofs-5.0.4-use-intr-as-hosts-mount-default.patch
Patch244:       autofs-5.0.4-fix-kernel-includes.patch
Patch245:       autofs-5.0.4-dont-umount-existing-direct-mount-on-reread.patch
Patch246:       autofs-5.0.4-library-reload-fix-update-fix.patch
Patch247:       autofs-5.0.4-improve-manual-umount-recovery.patch
Patch248:       autofs-5.0.4-dont-fail-on-ipv6-address-adding-host.patch
Patch249:       autofs-5.0.4-always-read-file-maps-multi-map-fix.patch
Patch250:       autofs-5.0.4-always-read-file-maps-key-lookup-fixes.patch
Patch251:       autofs-5.0.4-use-srv-query-for-domain-dn.patch
Patch252:       autofs-5.0.4-fix-incorrect-dclist-free.patch
Patch253:       autofs-5.0.4-srv-lookup-handle-endian.patch
Patch254:       autofs-5.0.4-library-reload-fix-update-fix-2.patch
Patch255:       autofs-5.0.4-fix-notify-mount-message-path.patch
Patch256:       autofs-5.0.4-remount-we-created-mount-point-fix.patch
Patch257:       autofs-5.0.4-fix-double-free-in-do_sasl_bind.patch
Patch258:       autofs-5.0.4-manual-umount-recovery-fixes.patch
Patch259:       autofs-5.0.4-fix-map-type-info-parse-error.patch
Patch260:       autofs-5.0.4-fix-map-type-info-parse-error-update.patch
Patch261:       autofs-5.0.4-fix-rpc-fd-leak.patch
Patch262:       autofs-5.0.4-allow-automount-daemon-to-dump-core.patch
Patch263:       autofs-5.0.4-fix-pthread-push-order-in-expire_proc_direct.patch
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
%patch201 -p 1
%patch202 -p 1
%patch203 -p 1
%patch204 -p 1
%patch205 -p 1
%patch206 -p 1
%patch207 -p 1
%patch208 -p 1
%patch209 -p 1
%patch210 -p 1
%patch211 -p 1
%patch212 -p 1
%patch213 -p 1
%patch214 -p 1
%patch215 -p 1
%patch216 -p 1
%patch217 -p 1
%patch218 -p 1
%patch219 -p 1
%patch220 -p 1
%patch221 -p 1
%patch222 -p 1
%patch223 -p 1
%patch224 -p 1
%patch225 -p 1
%patch226 -p 1
%patch227 -p 1
%patch228 -p 1
%patch229 -p 1
%patch230 -p 1
%patch231 -p 1
%patch232 -p 1
%patch233 -p 1
%patch234 -p 1
%patch235 -p 1
%patch236 -p 1
%patch237 -p 1
%patch238 -p 1
%patch239 -p 1
%patch240 -p 1
%patch241 -p 1
%patch242 -p 1
%patch243 -p 1
%patch244 -p 1
%patch245 -p 1
%patch246 -p 1
%patch247 -p 1
%patch248 -p 1
%patch249 -p 1
%patch250 -p 1
%patch251 -p 1
%patch252 -p 1
%patch253 -p 1
%patch254 -p 1
%patch255 -p 1
%patch256 -p 1
%patch257 -p 1
%patch258 -p 1
%patch259 -p 1
%patch260 -p 1
%patch261 -p 1
%patch262 -p 1
%patch263 -p 1

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
