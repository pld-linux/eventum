# TODO
# - discard bundled packages (from INSTALL):
#  - JpGraph 1.5.3 (last GPL version)
#  - dTree 2.0.5 (http://www.destroydrop.com/javascript/tree/)
#  - dynCalendar.js (http://www.phpguru.org/dyncalendar.html)
#  - overLIB 3.5.1 (http://www.bosrup.com/web/overlib/)
#  - A few other small javascript libraries
#
# Conditional build:
%bcond_without	order	# with experimental order patch

#define	snap	20060921
%define	rev		r4034
%define	rel		2.58
#define	_rc		RC3

%define		php_min_version 5.1.2
%include	/usr/lib/rpm/macros.php
Summary:	Eventum Issue / Bug tracking system
Summary(pl.UTF-8):	Eventum - system śledzenia spraw/błędów
Name:		eventum
Version:	2.2
Release:	%{?_rc:%{_rc}.}%{rel}%{?snap:.%{snap}}%{?rev:.%{rev}}
License:	GPL
Group:		Applications/WWW
#Source0:	http://downloads.mysql.com/snapshots/eventum/%{name}-nightly-%{snap}.tar.gz
#Source0:	http://eventum.mysql.org/downloads/eventum-2.0.RC3.tar.gz
#Source0:	http://mysql.easynet.be/Downloads/eventum/%{name}-%{version}.tar.gz
# bzr branch lp:eventum eventum && cd eventum && make dist
Source0:	%{name}-%{version}-dev-%{rev}.tar.gz
# Source0-md5:	17c325c4a26d8da3f47eb5dcc24b0fe0
Source1:	%{name}-apache.conf
Source2:	%{name}-mail-queue.cron
Source3:	%{name}-mail-download.cron
Source4:	%{name}-reminder.cron
Source5:	%{name}-monitor.cron
Source6:	%{name}-cvs.php
Source7:	%{name}-irc.php
Source8:	%{name}-irc.init
Source9:	%{name}-irc.sysconfig
Source13:	%{name}-router-postfix.sh
Source14:	%{name}.logrotate
Source15:	%{name}-lighttpd.conf
Source16:	http://www.isocra.com/images/updown2.gif
# Source16-md5:	deb6eeb2552ba757d3a949ed10c4107d
Patch0:		%{name}-lf.patch
Patch2:		%{name}-order.patch
# packaging patches that probably never go upstream
Patch100:	%{name}-paths.patch
Patch101:	%{name}-cvs-config.patch
Patch105:	%{name}-bot-reconnect.patch
Patch107:	%{name}-gettext.patch
# some tests
Patch200:	%{name}-fixed-nav.patch
URL:		http://eventum.mysql.org/
BuildRequires:	gettext-devel
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
BuildRequires:	rpmbuild(macros) >= 1.461
BuildRequires:	sed >= 4.0
Requires:	%{name}-base = %{version}-%{release}
Requires:	Smarty >= 2.6.10-4
Requires:	php-common >= 4:%{php_min_version}
Requires:	php-gd
Requires:	php-iconv
Requires:	php-imap
Requires:	php-mbstring
Requires:	php-mysql
Requires:	php-pcre
Requires:	php-pear-DB
Requires:	php-pear-Date
Requires:	php-pear-Mail
Requires:	php-pear-Mail_Mime
Requires:	php-pear-Mail_mimeDecode
Requires:	php-pear-Math_Stats
Requires:	php-pear-Net_DIME
Requires:	php-pear-Net_SMTP
Requires:	php-pear-Net_Socket
Requires:	php-pear-Net_URL
Requires:	php-pear-Net_UserAgent_Detect
Requires:	php-pear-PEAR-core
Requires:	php-pear-Text_Diff
Requires:	php-pear-XML_RPC
Requires:	php-session
Requires:	smarty-gettext
Requires:	webapps
Requires:	webserver(access)
Requires:	webserver(alias)
Requires:	webserver(indexfile)
Requires:	webserver(php) >= 4.2.0
Suggests:	localedb
Conflicts:	logrotate < 3.7-4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautopear	'pear(../init.php)' 'pear(init.php)' 'pear(/etc/webapps/.*)' 'pear(%{_appdir}/.*)' 'pear(jpgraph_dir.php)' 'pear(.*Smarty.class.php)' 'pear(Services/JSON.php)'

# exclude optional php dependencies
%define		_noautophp	'php-gnupg' 'php-hash' 'php-pecl-http' 'php-json' 'php-tk'

%define		_noautoreq	%{_noautophp} %{_noautopear}

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
and bugs. Eventum is used by the MySQL AB Technical Support team, and
has allowed us to dramatically improve our response times.

%description -l pl.UTF-8
Eventum to przyjazny dla użytkownika system śledzenia spraw, który
może być używany przez dział obsługi do śledzenia przychodzących żądań
obsługi technicznej albo przez zespół tworzący oprogramowanie do
szybkiej organizacji zadań i błędów. Eventum jest używany przez zespół
Technical Support MySQL AB i umożliwił im znacząco poprawić czasy
reakcji.

%package base
Summary:	Eventum base package
Summary(pl.UTF-8):	Podstawowy pakiet Eventum
Group:		Applications/WWW
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Provides:	group(eventum)
Provides:	user(eventum)

%description base
This package contains base directory structure for Eventum.

%description base -l pl.UTF-8
Ten pakiet zawiera podstawową strukturę katalogów dla Eventum.

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

%package route-drafts
Summary:	Eventum Draft Routing
Summary(pl.UTF-8):	Przekazywanie szkiców dla Eventum
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}
Requires:	eventum(router)

%description route-drafts
The draft routing feature is used to automatically associate a thread
of drafts into an Eventum issue. By setting up Postfix to deliver
emails sent to a specific address (usually draft-<number>@<domain>) to
the above script, users are able to send drafts written in their mail
client to be stored in Eventum. These drafts will NOT broadcasted to
the notification list.

%description route-drafts -l pl.UTF-8
Przekazywanie szkiców służy do automatycznego wiązania wątku szkiców z
problemem w Eventum. Ustawiając Postfiksa, aby dostarczał pocztę
wysłaną na podany adres (zwykle draft-<liczba>@<domena>) do tego
skryptu umożliwia się użytkownikom wysyłanie szkiców napisanych w ich
kliencie pocztowym do zapisania w Eventum. Szkice te NIE będą wysyłane
na listę powiadomień.

%package route-emails
Summary:	Eventum Email Routing
Summary(pl.UTF-8):	Przekazywanie poczty dla Eventum
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}
Requires:	eventum(router)

%description route-emails
The email routing feature is used to automatically associate a thread
of emails into an Eventum issue. By setting up Postfix to deliver
emails sent to a specific address (usually issue-<number>@<domain>) to
the above script, users are able to use their email clients to reply
to emails coming from Eventum, and those replies will be automatically
associated with the issue and broadcasted to the entire notification
list.

%description route-emails -l pl.UTF-8
Funkcjonalność przekazywania poczty służy do automatycznego wiązania
wątku listów ze sprawą w Eventum. Po ustawieniu czy nawet Postfiksa,
aby dostarczał listy wysyłane na pewien adres (zwykle
issue-<numer>@<domena>) na powyższy skrypt, użytkownicy będą mogli
używać klientów pocztowych do odpowiadania na listy przychodzące z
Eventum, a odpowiedzi te będą automatycznie wiązane ze sprawą i
rozprowadzane do całej listy ogłoszeniowej.

%package route-notes
Summary:	Eventum Note Routing
Summary(pl.UTF-8):	Przekazywanie notatek dla Eventum
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}
Requires:	eventum(router)

%description route-notes
The note routing feature is used to automatically associate a thread
of notes into an Eventum issue. By setting up Postfix to deliver
emails sent to a specific address (usually note-<number>@<domain>) to
the above script, users are able to use their email clients to reply
to internal notes coming from Eventum, and those replies will be
automatically associated with the issue and broadcasted to the
notification list staff members.

%description route-notes -l pl.UTF-8
Funkcjonalność przekazywania notatek służy do automatycznego wiązania
wątku notatek ze sprawą w Eventum. Po ustawieniu Postfiksa, aby
dostarczał listy wysyłane na pewien adres (zwykle
note-<numer>@<domena>) na powyższy skrypt, użytkownicy będą mogli
używać klientów pocztowych do odpowiadania na wewnętrzne notatki
pochodzące od Eventu, a odpowiedzi te będą automatycznie wiązane ze
sprawą i rozprowadzane do członków personelu listy ogłoszeniowej.

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
<http://eventum.mysql.org/wiki/index.php/Setting_up_email_routing_with_postfix>.

%description router-postfix -l pl.UTF-8
Ten pakiet udostępnia metodę przekazywania notatek i listów do Eventum
przez Postfiksa.

Opis konfiguracji Postfiksa można znaleźć pod adresem
<http://eventum.mysql.org/wiki/index.php/Setting_up_email_routing_with_postfix>.

%package irc
Summary:	Eventum IRC Notification Bot
Summary(pl.UTF-8):	IRC-owy bot powiadamiający dla Eventum
Group:		Applications/WWW
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name} = %{version}-%{release}
Requires:	php(sockets)
Requires:	php-pear-Net_SmartIRC
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
Requires:	%{name}-base = %{version}-%{release}
Requires:	php-cli
Requires:	php-common >= 4:%{php_min_version}
Requires:	php-pear-XML_RPC

%description cli
The Eventum command-line interface allows you to access most of the
features of the web interface straight from your command shell.

%description cli -l pl.UTF-8
Interfejs linii poleceń Eventum pozwala na dostęp do większości
funkcji interfejsu WWW prosto z linii poleceń powłoki.

%package scm
Summary:	Eventum SCM integration
Summary(pl.UTF-8):	Integracja SCM dla Eventum
Group:		Applications/WWW
Requires:	%{name}-base = %{version}-%{release}
Requires:	php-cli
Requires:	php-common >= 4:%{php_min_version}
Requires:	php-pcre

%description scm
This feature allows your software development teams to integrate your
Source Control Management system with your Issue Tracking System.

The integration is implemented in such a way that it will be forward
compatible with pretty much any SCM system, such as CVS.

For installation see
</eventum/help.php?topic=scm_integration_installation>.

%description scm -l pl.UTF-8
Ten pakiet pozwala zespołom programistów na integrację systemu
zarządzania źródłami (SCM - Source Control Management) z systemem
śledzenia spraw.

Integracja jest zaimplementowana tak, aby być kompatybilna w przód z
prawie każdym systemem SCM, jak np. CVS.

Szczegóły na temat instalacji można przeczytać pod
</eventum/help.php?topic=scm_integration_installation>.

%prep
%setup -q

# GPL v2
rm docs/COPYING

rm -r upgrade/*v1.[123]* # too old to support in PLD Linux
rm -r upgrade/v{1.,2.0,2.1_}* # no longer supported in PLD Linux
rm upgrade/flush_compiled_templates.php
rm -r upgrade/{*/,}index.html # not needed in PLD Linux

# bug fixes / features
%patch0 -p1
%{?with_order:%patch2 -p1}

cp -a %{SOURCE16} htdocs/images

#%patch200 -p1

# packaging
%patch100 -p1
%patch101 -p1
%patch105 -p1
%patch107 -p1

cat <<'EOF'> mysql-permissions.sql
# use this schema if you want to grant permissions manually instead of using setup
# this schema is extracted from setup/index.php.
GRANT SELECT, UPDATE, DELETE, INSERT, ALTER, DROP, CREATE, INDEX ON eventum.* TO 'eventum'@'localhost' IDENTIFIED BY 'password';
EOF

%{__sed} -i -e "
s;define('CONFIG_PATH'.*');define('CONFIG_PATH', '%{_webappdir}');
" upgrade/{*/,}*.php

# remove backups from patching as we use globs to package files to buildroot
find '(' -name '*~' -o -name '*.orig' ')' | xargs -r rm -v

%build
%{__make} -C localization

%install
rm -rf $RPM_BUILD_ROOT
install -d \
	$RPM_BUILD_ROOT{%{_webappdir},%{_sysconfdir},%{_bindir},%{_sbindir},%{_libdir}} \
	$RPM_BUILD_ROOT/etc/{rc.d/init.d,cron.d,sysconfig} \
	$RPM_BUILD_ROOT/var/{run,cache,lib}/%{name} \
	$RPM_BUILD_ROOT/var/log/{archive/,}%{name} \
	$RPM_BUILD_ROOT/var/lib/%{name}/routed_{emails,drafts,notes} \
	$RPM_BUILD_ROOT%{_appdir}/{include,htdocs/misc,upgrade} \

%{__make} install-eventum install-cli install-irc install-scm install-jpgraph install-localization \
	sysconfdir=%{_webappdir} \
	DESTDIR=$RPM_BUILD_ROOT

%{?with_order:cp -a htdocs/ajax $RPM_BUILD_ROOT%{_appdir}/htdocs}

touch $RPM_BUILD_ROOT%{_webappdir}/htpasswd
cp -a %{SOURCE1} $RPM_BUILD_ROOT%{_webappdir}/apache.conf
cp -a %{SOURCE1} $RPM_BUILD_ROOT%{_webappdir}/httpd.conf
cp -a %{SOURCE15} $RPM_BUILD_ROOT%{_webappdir}/lighttpd.conf

cp -a %{SOURCE2} $RPM_BUILD_ROOT/etc/cron.d/%{name}-mail-queue
cp -a %{SOURCE3} $RPM_BUILD_ROOT/etc/cron.d/%{name}-mail-download
cp -a %{SOURCE4} $RPM_BUILD_ROOT/etc/cron.d/%{name}-reminder
cp -a %{SOURCE5} $RPM_BUILD_ROOT/etc/cron.d/%{name}-monitor

cp -a %{SOURCE7} $RPM_BUILD_ROOT%{_webappdir}/irc_config.php

cp -a %{SOURCE8} $RPM_BUILD_ROOT/etc/rc.d/init.d/eventum-irc
cp -a %{SOURCE9} $RPM_BUILD_ROOT/etc/sysconfig/eventum-irc

# postfix router
install %{SOURCE13} $RPM_BUILD_ROOT%{_libdir}/router-postfix

install -D %{SOURCE14} $RPM_BUILD_ROOT/etc/logrotate.d/%{name}

%find_lang %{name}

# scm
install %{SOURCE6} $RPM_BUILD_ROOT%{_sysconfdir}/scm.php

# old compat
ln -s %{_sbindir}/eventum-cvs-hook $RPM_BUILD_ROOT%{_libdir}/process_cvs_commits
ln -s %{_sbindir}/eventum-svn-hook $RPM_BUILD_ROOT%{_libdir}/process_svn_commits

# skip pear for cli
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/cli
cp -a cli/lib/eventum $RPM_BUILD_ROOT%{_datadir}/%{name}/cli

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%addusertogroup http %{name}

%post
# check if the package is configured.
if grep -q "Header('Location: setup/')" %{_webappdir}/config.php; then
if [ -f %{_appdir}/htdocs/setup/index.php ]; then
%banner %{name} -e <<EOF

You haven't yet configured Eventum!
Please open in browser <http://localhost/eventum/>
If you need access from elsewhere, you need to edit
%{_webappdir}/apache.conf and restart apache.

IMPORTANT: When You have configured Eventum, please uninstall the
setup package, so that %{name}-setup is able to secure your Eventum
installation.

EOF
#' vim syntax hack
else
%banner %{name} -e <<EOF

You haven't yet configured Eventum!

To setup eventum, please install %{name}-setup and open in browser
<http://localhost/eventum/>.
If you need access from elsewhere, you need to edit
%{_webappdir}/*.conf depending on webserver and restart the webserver.

IMPORTANT: When You have configured Eventum, please uninstall the
setup package, so that %{name}-setup is able to secure your Eventum
installation.

EOF
#' vim syntax hack
fi

elif grep -q 'DEFAULTPRIVATEKEY' %{_webappdir}/private_key.php; then
%banner %{name} -e <<EOF

You have default private key installed!

Install %{name}-setup and open up http://yourserver/eventum/setup/
-- that will help you setup initial config.

when have configured Eventum, please uninstall the setup package,
so that %{name}-setup is able to secure your Eventum installation.

EOF
	elif [ -d %{_appdir}/setup ]; then
%banner %{name} -e <<EOF

If you have have configured Eventum, please uninstall the setup package,
so that %{name}-setup is able to secure your Eventum installation.

EOF
fi

# greate empty ghost files
for a in cli.log errors.log irc_bot.log login_attempts.log; do
	if [ ! -f /var/log/%{name}/$a ]; then
		install -m620 -oroot -geventum /dev/null /var/log/%{name}/$a
	fi
done

# database update
%{_appdir}/upgrade/update-database.php || :

# nuke Smarty templates cache after upgrade
rm -f /var/cache/eventum/*.php

%preun
if [ "$1" = "0" ]; then
	# nuke cache
	rm -f /var/cache/eventum/*.php 2>/dev/null || :
fi

%pre base
%groupadd -P %{name}-base -g 146 %{name}
%useradd -P %{name}-base -u 146 -d /var/lib/%{name} -g %{name} -c "Eventum User" %{name}

%postun base
if [ "$1" = "0" ]; then
	%userremove %{name}
	%groupremove %{name}
fi

%post setup
chmod 660 %{_webappdir}/{config,private_key}.php
chown root:eventum %{_webappdir}/{config,private_key}.php

%postun setup
if [ "$1" = "0" ]; then
	chmod 640 %{_webappdir}/{config,private_key}.php
	chown root:eventum %{_webappdir}/{config,private_key}.php
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

%triggerpostun -- %{name} < 2.2-2.57
# switching eventum->http user
chgrp http %{_webappdir}/config.php
chgrp http %{_webappdir}/private_key.php
chgrp http %{_webappdir}/setup.php
chgrp http /var/log/%{name}/*
# update crontab user
for a in /etc/cron.d/eventum-*; do
	awk '!/#/ && NR > 6 && $6 =="eventum" {sub("eventum", "http", $6)}{print}'  $a > $a.rpmtmp && cat $a.rpmtmp > $a
	rm -f $a.rpmtmp
done

# crontabs moved to crons subdir
%{__sed} -i -e '
	s,/usr/share/eventum/process_mail_queue.php,/usr/share/eventum/crons/process_mail_queue.php,
	s,/usr/share/eventum/download_emails.php,/usr/share/eventum/crons/download_emails.php,
	s,/usr/share/eventum/check_reminders.php,/usr/share/eventum/crons/check_reminders.php,
	s,/usr/share/eventum/monitor.php,/usr/share/eventum/crons/monitor.php,
' /etc/cron.d/eventum-*

%triggerpostun mail-download -- %{name}-mail-download < 2.2-2.57
%triggerpostun reminder -- %{name}-reminder < 2.2-2.57
%triggerpostun monitor -- %{name}-monitor < 2.2-2.57


%files -f %{name}.lang
%defattr(644,root,root,755)
%doc docs/* htdocs/setup/schema.sql mysql-permissions.sql
%attr(751,root,root) %dir %{_webappdir}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_webappdir}/apache.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_webappdir}/httpd.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_webappdir}/lighttpd.conf
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_webappdir}/config.php
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_webappdir}/private_key.php
%attr(660,root,http) %config(noreplace) %verify(not md5 mtime size) %{_webappdir}/setup.php
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_webappdir}/htpasswd

%dir %attr(731,root,http) /var/log/%{name}
%attr(620,root,http) %ghost /var/log/%{name}/*
%dir %attr(750,root,root) /var/log/archive/%{name}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/%{name}

%dir %{_appdir}/crons
%{_appdir}/init.php
%dir %{_appdir}/htdocs
%{_appdir}/htdocs/*.php
%{_appdir}/htdocs/*.ico
%{_appdir}/htdocs/css
%{_appdir}/htdocs/customer
%{_appdir}/htdocs/images
%{_appdir}/htdocs/js
%{_appdir}/htdocs/manage
%{_appdir}/htdocs/reports
%{_appdir}/htdocs/rpc
%{_appdir}/htdocs/misc
%if %{with order}
%{_appdir}/htdocs/ajax
%endif
%{_appdir}/templates

%dir %{_appdir}/upgrade
%{_appdir}/upgrade/init.php
%attr(755,root,root) %{_appdir}/upgrade/update-database.php
%dir %{_appdir}/upgrade/v*
%attr(755,root,root) %{_appdir}/upgrade/v*/*.php
%{_appdir}/upgrade/patches

%dir %{_appdir}/lib
%{_appdir}/lib/eventum
%{_appdir}/lib/jpgraph
%exclude %{_appdir}/lib/eventum/class.monitor.php

%dir %attr(730,root,http) /var/run/%{name}
%dir %attr(730,root,http) /var/cache/%{name}

%files base
%defattr(644,root,root,755)
%attr(751,root,root) %dir %{_sysconfdir}
%dir %{_libdir}
%dir %{_appdir}
%dir /var/lib/%{name}
# saved mail copies
%attr(770,root,http) %dir /var/lib/%{name}/routed_emails
%attr(770,root,http) %dir /var/lib/%{name}/routed_drafts
%attr(770,root,http) %dir /var/lib/%{name}/routed_notes

%files setup
%defattr(644,root,root,755)
%{_appdir}/htdocs/setup

%files mail-queue
%defattr(644,root,root,755)
%attr(755,root,root) %{_appdir}/crons/process_mail_queue.php
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/cron.d/%{name}-mail-queue

%files mail-download
%defattr(644,root,root,755)
%attr(755,root,root) %{_appdir}/crons/download_emails.php
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/cron.d/%{name}-mail-download

%files reminder
%defattr(644,root,root,755)
%attr(755,root,root) %{_appdir}/crons/check_reminders.php
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/cron.d/%{name}-reminder

%files monitor
%defattr(644,root,root,755)
%{_appdir}/lib/eventum/class.monitor.php
%attr(755,root,root) %{_appdir}/crons/monitor.php
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/cron.d/%{name}-monitor

%files route-drafts
%defattr(644,root,root,755)
%attr(755,root,root) %{_appdir}/route_drafts.php

%files route-emails
%defattr(644,root,root,755)
%attr(755,root,root) %{_appdir}/route_emails.php

%files route-notes
%defattr(644,root,root,755)
%attr(755,root,root) %{_appdir}/route_notes.php

%files router-postfix
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/router-postfix

%files irc
%defattr(644,root,root,755)
%attr(640,root,eventum) %config(noreplace) %verify(not md5 mtime size) %{_webappdir}/irc_config.php
%attr(640,root,eventum) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/eventum-irc
%attr(755,root,root) %{_sbindir}/%{name}-irc-bot
%attr(754,root,root) /etc/rc.d/init.d/%{name}-irc

%files cli
%defattr(644,root,root,755)
%doc cli/eventumrc
%attr(755,root,root) %{_bindir}/%{name}
%{_appdir}/cli

%files scm
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/scm.php
%attr(755,root,root) %{_libdir}/process_cvs_commits
%attr(755,root,root) %{_libdir}/process_svn_commits
%attr(755,root,root) %{_sbindir}/eventum-cvs-hook
%attr(755,root,root) %{_sbindir}/eventum-svn-hook
