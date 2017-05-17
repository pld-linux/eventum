#
# Conditional build:
%bcond_with	order	# with experimental order patch

%define		rel		0.2
%define		subver  344
%define		githash 7f34327f
%define		php_min_version 5.5.0
%include	/usr/lib/rpm/macros.php
Summary:	Eventum Issue / Bug tracking system
Summary(pl.UTF-8):	Eventum - system śledzenia spraw/błędów
Name:		eventum
Version:	3.1.10
Release:	%{?subver:1.%{subver}.%{?githash:g%{githash}.}}%{rel}
License:	GPL v2+
Group:		Applications/WWW
#Source0:	https://github.com/eventum/eventum/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source0:	https://github.com/eventum/eventum/releases/download/snapshot/%{name}-%{version}-%{subver}-g%{githash}.tar.gz
# Source0-md5:	d7001291388fedcb55f3d3ad4da947db
Source1:	%{name}-apache.conf
Source2:	%{name}-mail-queue.cron
Source3:	%{name}-mail-download.cron
Source4:	%{name}-reminder.cron
Source5:	%{name}-monitor.cron
Source8:	%{name}-irc.init
Source9:	%{name}-irc.sysconfig
Source10:	sphinx.crontab
Source13:	%{name}-router-postfix.sh
Source14:	%{name}.logrotate
Source15:	%{name}-lighttpd.conf
Source16:	http://www.isocra.com/images/updown2.gif
# Source16-md5:	deb6eeb2552ba757d3a949ed10c4107d
Source17:	%{name}.tmpfiles
Patch2:		%{name}-order.patch
#Patch3:		group-users.patch
#Patch4:		https://github.com/glensc/eventum/compare/cf_escape.patch
# packaging patches that probably never go upstream
Patch100:	%{name}-paths.patch
Patch107:	%{name}-gettext.patch
Patch108:	autoload.patch
# some tests
Patch200:	%{name}-fixed-nav.patch
URL:		https://wiki.github.com/eventum/eventum/
BuildRequires:	gettext-tools
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
BuildRequires:	rpmbuild(macros) >= 1.654
BuildRequires:	sed >= 4.0
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires:	fonts-TTF-RedHat-liberation
Requires:	php(core) >= %{php_min_version}
Requires:	php(filter)
Requires:	php(iconv)
Requires:	php(imap)
Requires:	php(json)
Requires:	php(mbstring)
Requires:	php(pcre)
Requires:	php(pdo_mysql)
Requires:	php(session)
Requires:	php-Smarty >= 3.1
Requires:	php-Smarty-plugin-gettext
Requires:	php-ZendFramework-Config >= 2.4
Requires:	php-ZendFramework-Loader >= 2.4
Requires:	php-ZendFramework-Mail >= 2.4.9-2
Requires:	php-ZendFramework-Mime >= 2.4
Requires:	php-ZendFramework-ServiceManager >= 2.4
Requires:	php-ZendFramework-Validator >= 2.4
Requires:	php-monolog >= 1.17.2
Requires:	php-pear-Mail
Requires:	php-pear-Mail_Mime
Requires:	php-pear-Mail_mimeDecode
Requires:	php-pear-Math_Stats
Requires:	php-pear-Net_SMTP
Requires:	php-pear-Net_Socket
Requires:	php-pear-Net_URL
Requires:	php-pear-PEAR-core
Requires:	php-pear-Text_Diff
Requires:	php-psr-Log >= 1.0.0-2
Requires:	php-symfony2-Config >= 2.7.7
Requires:	php-symfony2-Console >= 2.7.7
Requires:	php-symfony2-Filesystem >= 2.7.7
Requires:	php-symfony2-HttpFoundation >= 2.7.7
Requires:	php-symfony2-OptionsResolver >= 2.7.7
Requires:	php-symfony2-Serializer >= 2.7.7
Requires:	php-symfony2-Yaml >= 2.7.7
Requires:	phplot >= 5.8.0
Requires:	webapps
Requires:	webserver(access)
Requires:	webserver(alias)
Requires:	webserver(indexfile)
Requires:	webserver(php) >= 4.2.0
Suggests:	localedb
Suggests:	php(mcrypt)
Suggests:	php(openssl)
Suggests:	php-pear-Net_LDAP2
Suggests:	php-pear-Net_POP3
Suggests:	webserver(setenv)
Provides:	group(eventum)
Provides:	user(eventum)
Obsoletes:	eventum-base < 3.0.3-1.305
Obsoletes:	eventum-route-drafts < 3.0.8-1.1
Obsoletes:	eventum-route-emails < 3.0.8-1.1
Obsoletes:	eventum-route-notes < 3.0.8-1.1
Conflicts:	logrotate < 3.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq_pear	../init.php ../../init.php init.php /usr/share/eventum/init.php /etc/webapps/.* %{_appdir}/.* .*Smarty.class.php Services/JSON.php class.date_helper.php sphinxapi.php Net/LDAP2.* Auth/SASL.* Util.php smarty_internal.*

# exclude optional php dependencies
%define		_noautophp	php-gnupg php-hash php-pecl-http php-tk

%define		_noautoreq	%{_noautophp}

%define		_libdir		%{_prefix}/lib/%{name}
%define		_appdir		%{_datadir}/%{name}
%define		_smartydir	%{php_data_dir}/Smarty
%define		_webapps	/etc/webapps
%define		_webapp		%{name}
%define		_webappdir	%{_webapps}/%{_webapp}
%define		_sysconfdir	/etc/%{name}

%description
Eventum is a user-friendly and flexible issue tracking system that can
be used by a support department to track incoming technical support
requests, or by a software development team to quickly organize tasks
and bugs.

%description -l pl.UTF-8
Eventum to przyjazny dla użytkownika system śledzenia spraw, który
może być używany przez dział obsługi do śledzenia przychodzących żądań
obsługi technicznej albo przez zespół tworzący oprogramowanie do
szybkiej organizacji zadań i błędów.

%package setup
Summary:	Eventum setup package
Summary(pl.UTF-8):	Pakiet do wstępnej konfiguracji Eventum
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}

%description setup
Install this package to configure initial Eventum installation. You
should uninstall this package when you're done, as it considered
insecure to keep the setup files in place.

%description setup -l pl.UTF-8
Ten pakiet należy zainstalować w celu wstępnej konfiguracji Eventum po
pierwszej instalacji. Potem należy go odinstalować, jako że
pozostawienie plików instalacyjnych mogłoby być niebezpieczne.

%package doc
Summary:	Eventum documentation and Wiki
Group:		Documentation

%description doc
Eventum documentation and copy of Wiki.

%package mail-queue
Summary:	Eventum mail queue process
Summary(pl.UTF-8):	Przetwarzanie kolejki poczty Eventum
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}
Requires:	crondaemon

%description mail-queue
Beginning with the first release of Eventum, emails are not directly
sent out from the various scripts, but rather added to a mail queue
table that is processed by a cron job. If an email cannot be sent, it
will be marked as such in the mail queue log, and the cron job script
will re-try to send it again the next time it runs.

This package contains the cron job.

%description mail-queue -l pl.UTF-8
Od pierwszego wydania Eventum poczta nie jest wysyłana bezpośrednio z
różnych skryptów, lecz dodawana do kolejki przetwarzanej z crona.
Jeśli poczta nie może być wysłana, będzie odpowiednio oznaczona w logu
kolejki poczty, a skrypt z crona będzie próbował wysłać ją ponownie
następnym razem.

Ten pakiet zawiera zadanie dla crona.

%package mail-download
Summary:	Eventum email download
Summary(pl.UTF-8):	Ściąganie poczty Eventum
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}
Requires:	crondaemon

%description mail-download
In order for Eventum's email integration feature to work, you need to
setup a cron job to run the script every so often.

This package contains the cron job.

%description mail-download -l pl.UTF-8
Aby integracja poczty elektronicznej w Eventum działała, trzeba
ustawić zadanie crona, aby uruchamiał odpowiedni skrypt wystarczająco
często.

Ten pakiet zawiera zadanie dla crona.

%package reminder
Summary:	Eventum Reminder System
Summary(pl.UTF-8):	System przypominania dla Eventum
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}
Requires:	crondaemon

%description reminder
The reminder system was designed with the objective as serving as a
safe net for issues that need attention. Depending on what
configuration you create, you may have several reminders (or alerts)
be sent out whenever an issue needs attention, for whatever parameter
you may deem necessary.

This package contains the cron job.

%description reminder -l pl.UTF-8
System przypominania został zaprojektowany tak, aby służył jako
bezpieczna sieć dla spraw wymagających uwagi. W zależności od
konfiguracji można ustawić różne przypominajki (lub alarmy) wysyłane
przy każdej sprawie wymagającej uwagi lub przy parametrze, który można
uważać za potrzebny.

Ten pakiet zawiera zadanie dla crona.

%package monitor
Summary:	Eventum Heartbeat Monitor
Summary(pl.UTF-8):	Monitor życia dla Eventum
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}
Requires:	crondaemon
Requires:	php(posix)

%description monitor
The heartbeat monitor is a feature designed for the administrator that
wants to be alerted whenever a common problem in Eventum is detected,
like the database server not being available anymore, or maybe when
the recommended permissions for certain configuration files are
changed.

Please note that before running the heartbeat monitor, you may need to
customize some of the checks to be appropriate for your own system,
particularly the permission and file checks on
Monitor::checkConfiguration().

This package contains the cron job.

%description monitor -l pl.UTF-8
Monitor życia to funkcjonalność zaprojektowana dla administratora
chcącego być alarmowanym przy każdym wykryciu popularnego problemu z
Eventum, jak nie działanie serwera bazy danych albo zmiana uprawnień
do plików konfiguracyjnych.

Należy zauważyć, że przed uruchomieniem tego monitora może być
konieczne dostosowanie niektórych testów do systemu, w szczególności
testów uprawnień i plików w Monitor::checkConfiguration().

Ten pakiet zawiera zadanie dla crona.

%package router-postfix
Summary:	Eventum Mail Routing - Postfix
Summary(pl.UTF-8):	Przekazywanie poczty Eventum - Postfix
Group:		Applications/Mail
Requires:	%{name} = %{version}-%{release}
Requires:	postfix
Provides:	eventum(router)
Obsoletes:	eventum(router)

%description router-postfix
This package provides way of routing notes and emails back to Eventum
via Postfix.

The Postfix configuration instructions you can find from
<https://github.com/eventum/eventum/wiki/System-Admin:-Setting-up-email-routing-with-postfix>

%description router-postfix -l pl.UTF-8
Ten pakiet udostępnia metodę przekazywania notatek i listów do Eventum
przez Postfiksa.

Opis konfiguracji Postfiksa można znaleźć pod adresem
<https://github.com/eventum/eventum/wiki/System-Admin:-Setting-up-email-routing-with-postfix>

%package irc
Summary:	Eventum IRC Notification Bot
Summary(pl.UTF-8):	IRC-owy bot powiadamiający dla Eventum
Group:		Applications/WWW
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name} = %{version}-%{release}
Requires:	php(pcntl)
Requires:	php(sockets)
Requires:	php-pear-Net_SmartIRC >= 1.1.9
Requires:	rc-scripts >= 0.4.0.18

%description irc
The IRC notification bot is a nice feature for remote teams that want
to handle issues and want to have a quick and easy way to get simple
notifications. Right now the bot notifies of the following actions:
- New Issues
- Blocked emails
- Issues that got their assignment list changed

NOTE: You will need to manually edit the bot.php script to set your
appropriate preferences, like IRC server and channel that the bot
should join.

%description irc -l pl.UTF-8
IRC-owy bot powiadamiający to miła funkcjonalność dla zdalnych
zespołów chcących obsługiwać sprawy i mieć szybki i łatwy sposób na
uzyskiwanie prostych powiadomień. Aktualnie bot powiadamia o
następujących zdarzeniach:
- nowych sprawach
- zablokowanych listach
- sprawach, dla których zmieniła się lista powiązań

UWAGA: w celu wprowadzenia własnych ustawień, takich jak serwer IRC i
kanał używany przez bota, trzeba ręcznie zmodyfikować skrypt bot.php .

%package cli
Summary:	Eventum command-line interface
Summary(pl.UTF-8):	Interfejs linii poleceń dla Eventum
Group:		Applications/WWW
Requires:	php(core) >= %{php_min_version}
Requires:	php(phar)

%description cli
The Eventum command-line interface allows you to access most of the
features of the web interface straight from your command shell.

%description cli -l pl.UTF-8
Interfejs linii poleceń Eventum pozwala na dostęp do większości
funkcji interfejsu WWW prosto z linii poleceń powłoki.

%package sphinx
Summary:	Eventum Sphinx Search
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}
Requires:	crondaemon
Requires:	sphinx

%description sphinx
Sphinx search integration for Eventum.

This package contains the cron job.

%prep
%setup -q -n %{name}-%{version}%{?githash:-%{subver}-g%{githash}}

mv docs/examples .

# bug fixes / features
%{?with_order:%patch2 -p1}
#%patch3 -p0
#%patch4 -p1

%{?with_order:cp -p %{SOURCE16} htdocs/images}

#%patch200 -p1

# produce default sphinx config
# must be run before paths.patch
%if 0
cat <<'EOF' > config/config.php
<?php
define('APP_SQL_DBTYPE', 'mysql');
define('APP_SQL_DBHOST', 'localhost:/var/lib/mysql/mysql.sock');
define('APP_SQL_DBPORT', 3306);
define('APP_SQL_DBNAME', 'eventum');
define('APP_SQL_DBUSER', 'mysql');
define('APP_SQL_DBPASS', '');
define('APP_TABLE_PREFIX', 'eventum_');
EOF
php config/sphinx.conf.php > config/sphinx.conf
rm config/config.php
%endif

# packaging
%patch100 -p1
%patch107 -p1
%patch108 -p1

rm htdocs/.htaccess.dist

mv config/irc_config{.dist.php,.php}
rm config/config.dist.php

# cleanup vendor. keep only needed libraries.
# (the rest are packaged with system packages)
mv vendor vendor.dist
vendor() {
	local path dir
	for path; do
		dir=$(dirname $path)
		test -d vendor/$dir || mkdir -p vendor/$dir
		mv vendor.dist/$path vendor/$path
	done
}
vendor autoload.php
vendor composer/autoload_{classmap,files,namespaces,real,psr4}.php
vendor composer/ClassLoader.php
vendor ircmaxell/{random-lib,security-lib}
vendor defuse/php-encryption
vendor willdurand/email-reply-parser
vendor theorchard/monolog-cascade
vendor malkusch/lock
vendor phpxmlrpc/phpxmlrpc
vendor robmorgan/phinx

# remove backups from patching as we use globs to package files to buildroot
find '(' -name '*~' -o -name '*.orig' ')' | xargs -r rm -v

%build
%{__make} -C localization

%install
rm -rf $RPM_BUILD_ROOT
install -d \
	$RPM_BUILD_ROOT{%{_webappdir}/{custom_field,templates,workflow},%{_sysconfdir},%{_bindir},%{_sbindir},%{_libdir}} \
	$RPM_BUILD_ROOT/etc/{rc.d/init.d,cron.d,logrotate.d,sysconfig} \
	$RPM_BUILD_ROOT/var/{run,cache,lib}/%{name} \
	$RPM_BUILD_ROOT/var/log/{archive/,}%{name} \
	$RPM_BUILD_ROOT/var/lib/%{name}/routed_{emails,drafts,notes} \
	$RPM_BUILD_ROOT%{systemdtmpfilesdir}

%{__make} install-eventum install-cli install-localization \
	sysconfdir=%{_webappdir} \
	localedir=%{_localedir} \
	DESTDIR=$RPM_BUILD_ROOT

ln -s %{_webappdir} $RPM_BUILD_ROOT%{_appdir}/config

cp -a vendor $RPM_BUILD_ROOT%{_appdir}

# unsupported locale
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ht

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{?with_order:cp -a htdocs/ajax $RPM_BUILD_ROOT%{_appdir}/htdocs}

touch $RPM_BUILD_ROOT%{_webappdir}/htpasswd
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_webappdir}/apache.conf
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_webappdir}/httpd.conf
cp -p %{SOURCE15} $RPM_BUILD_ROOT%{_webappdir}/lighttpd.conf

install -d $RPM_BUILD_ROOT/etc/sphinx
#cp -p config/sphinx.conf $RPM_BUILD_ROOT/etc/sphinx/%{name}.conf
cp -p config/sphinx.conf.php $RPM_BUILD_ROOT%{_webappdir}

cp -p %{SOURCE2} $RPM_BUILD_ROOT/etc/cron.d/%{name}-mail-queue
cp -p %{SOURCE3} $RPM_BUILD_ROOT/etc/cron.d/%{name}-mail-download
cp -p %{SOURCE4} $RPM_BUILD_ROOT/etc/cron.d/%{name}-reminder
cp -p %{SOURCE5} $RPM_BUILD_ROOT/etc/cron.d/%{name}-monitor
cp -p %{SOURCE10} $RPM_BUILD_ROOT/etc/cron.d/%{name}-sphinx

install -p %{SOURCE8} $RPM_BUILD_ROOT/etc/rc.d/init.d/eventum-irc
cp -p %{SOURCE9} $RPM_BUILD_ROOT/etc/sysconfig/eventum-irc

cp -p %{SOURCE14} $RPM_BUILD_ROOT/etc/logrotate.d/%{name}

# postfix router
install -p %{SOURCE13} $RPM_BUILD_ROOT%{_libdir}/router-postfix

cp -p %{SOURCE17} $RPM_BUILD_ROOT%{systemdtmpfilesdir}/%{name}.conf

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%groupadd -g 146 %{name}
%useradd -u 146 -d /var/lib/%{name} -g %{name} -c "Eventum User" %{name}
%addusertogroup http %{name}

%post
# create empty ghost files
# these permissions ensure the logs are write only
for a in \
	errors.log login_attempts.log \
	eventum.log \
	auth.log cli.log \
	irc_bot_error.log irc_bot_smartirc.log \
; do
	test -f /var/log/%{name}/$a && continue
	install -m 0620 -o root -g http /dev/null /var/log/%{name}/$a
done

# run database update if configured
test -s %{_webappdir}/config.php && \
%{_appdir}/bin/upgrade.php || :

# nuke Smarty templates cache after upgrade
rm -f /var/cache/eventum/*.php

# Restart webserver on upgrade to get .mo translations reloaded.
# actually php engines "php-fcgi" and "php-fpm" needed only, apache is restarted anyway via webapp trigger.
%php_webserver_restart

%preun
if [ "$1" = "0" ]; then
	# nuke cache
	rm -f /var/cache/eventum/*.php 2>/dev/null || :
fi

%postun
if [ "$1" = "0" ]; then
	%userremove %{name}
	%groupremove %{name}
fi

%post setup
chmod 660 %{_webappdir}/{config,private_key,secret_key}.php
chown root:http %{_webappdir}/{config,private_key,secret_key}.php

%postun setup
if [ "$1" = "0" ] && [ -f %{_webappdir}/config.php ]; then
	chmod 640 %{_webappdir}/{config,private_key,secret_key}.php
	chown root:http %{_webappdir}/{config,private_key,secret_key}.php
fi

%post irc
/sbin/chkconfig --add eventum-irc
%service eventum-irc restart "Eventum IRC Bot"

%preun irc
if [ "$1" = 0 ]; then
	%service eventum-irc stop
	/sbin/chkconfig --del eventum-irc
fi

%triggerin -- apache1 < 1.3.37-3, apache1-base
%webapp_register apache %{_webapp}

%triggerun -- apache1 < 1.3.37-3, apache1-base
%webapp_unregister apache %{_webapp}

%triggerin -- apache < 2.2.0, apache-base
%webapp_register httpd %{_webapp}

%triggerun -- apache < 2.2.0, apache-base
%webapp_unregister httpd %{_webapp}

%triggerin -- lighttpd
%webapp_register lighttpd %{_webapp}

%triggerun -- lighttpd
%webapp_unregister lighttpd %{_webapp}

%triggerpostun -- %{name} < 3.0.0-0.2
for f in /etc/cron.d/eventum-*; do
	# crontabs moved to bin
	%{__sed} -i -e '
		s,/usr/share/eventum/crons/process_mail_queue.php,%{_appdir}/bin/process_mail_queue.php,
		s,/usr/share/eventum/crons/download_emails.php,%{_appdir}/bin/download_emails.php,
		s,/usr/share/eventum/crons/check_reminders.php,%{_appdir}/bin/check_reminders.php,
		s,/usr/share/eventum/crons/monitor.php,%{_appdir}/bin/monitor.php,
	' $f
done

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(751,root,root) %dir %{_webappdir}
%attr(751,root,http) %dir %{_webappdir}/custom_field
%attr(751,root,http) %dir %{_webappdir}/templates
%attr(751,root,http) %dir %{_webappdir}/workflow
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_webappdir}/apache.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_webappdir}/httpd.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_webappdir}/lighttpd.conf
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_webappdir}/config.php
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_webappdir}/private_key.php
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_webappdir}/secret_key.php
%attr(660,root,http) %config(noreplace) %verify(not md5 mtime size) %{_webappdir}/setup.php
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_webappdir}/htpasswd

%dir %attr(711,root,http) /var/log/%{name}
%attr(620,root,http) %ghost /var/log/%{name}/*
%dir %attr(750,root,root) /var/log/archive/%{name}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/%{name}

%dir %{_appdir}
%{_appdir}/config

%dir %{_appdir}/bin
%attr(755,root,root) %{_appdir}/bin/process_all_emails.php
%attr(755,root,root) %{_appdir}/bin/upgrade.php

%{_appdir}/autoload.php
%{_appdir}/globals.php
%{_appdir}/init.php
%{_appdir}/phinx.php
%dir %{_appdir}/htdocs
%{_appdir}/htdocs/*.php
%{_appdir}/htdocs/*.ico
%{_appdir}/htdocs/ajax
%{_appdir}/htdocs/css
%{_appdir}/htdocs/customer
%{_appdir}/htdocs/images
%{_appdir}/htdocs/js
%{_appdir}/htdocs/manage
%{_appdir}/htdocs/reports
%{_appdir}/htdocs/rpc
%{_appdir}/htdocs/components
%{_appdir}/templates

%dir %{_appdir}/upgrade
%{_appdir}/upgrade/*.sql
%{_appdir}/upgrade/patches
%dir %{_appdir}/db
%dir %{_appdir}/db/migrations
%{_appdir}/db/migrations/*.php

%{_appdir}/res
%{_appdir}/src
%{_appdir}/vendor
%dir %{_appdir}/lib
%{_appdir}/lib/eventum
%exclude %{_appdir}/lib/eventum/class.monitor.php

%dir %{_libdir}

%{systemdtmpfilesdir}/%{name}.conf

%dir /var/lib/%{name}
%dir %attr(730,root,http) /var/run/%{name}
%dir %attr(730,root,http) /var/cache/%{name}

# saved mail copies
%attr(770,root,http) %dir /var/lib/%{name}/routed_emails
%attr(770,root,http) %dir /var/lib/%{name}/routed_drafts
%attr(770,root,http) %dir /var/lib/%{name}/routed_notes

%files setup
%defattr(644,root,root,755)
%{_appdir}/htdocs/setup

%files doc
%defattr(644,root,root,755)
%doc docs/*
%{_examplesdir}/%{name}-%{version}

%files mail-queue
%defattr(644,root,root,755)
%attr(755,root,root) %{_appdir}/bin/process_mail_queue.php
%attr(755,root,root) %{_appdir}/bin/truncate_mail_queue.php
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/cron.d/%{name}-mail-queue

%files mail-download
%defattr(644,root,root,755)
%attr(755,root,root) %{_appdir}/bin/download_emails.php
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/cron.d/%{name}-mail-download

%files reminder
%defattr(644,root,root,755)
%attr(755,root,root) %{_appdir}/bin/check_reminders.php
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/cron.d/%{name}-reminder

%files monitor
%defattr(644,root,root,755)
%{_appdir}/lib/eventum/class.monitor.php
%attr(755,root,root) %{_appdir}/bin/monitor.php
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/cron.d/%{name}-monitor

%files router-postfix
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/router-postfix

%files irc
%defattr(644,root,root,755)
%attr(640,root,eventum) %config(noreplace) %verify(not md5 mtime size) %{_webappdir}/irc_config.php
%attr(640,root,eventum) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/eventum-irc
%attr(755,root,root) %{_appdir}/bin/irc-bot.php
%attr(754,root,root) /etc/rc.d/init.d/%{name}-irc

%files cli
%defattr(644,root,root,755)
%doc cli/eventumrc
%attr(755,root,root) %{_bindir}/%{name}

%files sphinx
%defattr(644,root,root,755)
%{_webappdir}/sphinx.conf.php
#%attr(750,root,http) %config(noreplace) %verify(not md5 mtime size) /etc/sphinx/%{name}.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/cron.d/%{name}-sphinx
