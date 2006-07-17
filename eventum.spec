# TODO
# - discard bundled packages (from INSTALL):
#  - JpGraph 1.5.3 (last GPL version)
#  - dTree 2.0.5 (http://www.destroydrop.com/javascript/tree/)
#  - dynCalendar.js (http://www.phpguru.org/dyncalendar.html)
#  - overLIB 3.5.1 (http://www.bosrup.com/web/overlib/)
#  - A few other small javascript libraries
# - 64bit platforms beware? http://bugs.php.net/bug.php?id=30215 (it's actually Smarty related problem)
#
# Conditional build:
%bcond_with	qmail	# build the router-qmail subpackage
%bcond_with	order_patch	# with custom issue order patch

#define	_snap	20060330
#define	_rc		RC3
%define	_rel	2.37

%include	/usr/lib/rpm/macros.php
Summary:	Eventum Issue / Bug tracking system
Summary(pl):	Eventum - system ¶ledzenia spraw/b³êdów
Name:		eventum
Version:	1.7.1
Release:	%{?_snap:0.%{_snap}.}%{?_rc:%{_rc}.}%{_rel}
License:	GPL
Group:		Applications/WWW
#Source0:	http://downloads.mysql.com/snapshots/eventum/%{name}-nightly-%{_snap}.tar.gz
Source0:	http://mysql.dataphone.se/Downloads/eventum/%{name}-%{version}.tar.gz
# Source0-md5:	e1845de39b4d9bd30ddec9c26031a7d5
Source1:	%{name}-apache.conf
Source2:	%{name}-mail-queue.cron
Source3:	%{name}-mail-download.cron
Source4:	%{name}-reminder.cron
Source5:	%{name}-monitor.cron
Source6:	%{name}-cvs.php
Source7:	%{name}-irc.php
Source8:	%{name}-irc.init
Source9:	%{name}-irc.sysconfig
Source10:	%{name}-config.php
Source11:	%{name}-router-qmail.sh
Source12:	%{name}-config-setup.php
Source13:	%{name}-upgrade.sh
Source14:	%{name}-router-postfix.sh
Source15:	%{name}.logrotate
Patch0:		%{name}-lf.patch
Patch1:		%{name}-perms.patch
Patch2:		%{name}-cli-wr-separated.patch
Patch3:		%{name}-scm-parse-response.patch
Patch4:		%{name}-double-decode.patch
Patch5:		%{name}-route-mem.patch
Patch6:		%{name}-scm-pluscharisbad.patch
Patch7:		%{name}-scm-updates.patch
Patch8:		%{name}-close-signature.patch
Patch9:		%{name}-list-sorting.patch
Patch10:	%{name}-workflow-handlenewnote-note_id.patch
Patch11:	%{name}-order4b.patch
Patch12:	%{name}-cli-errorcheck.patch
Patch13:	%{name}-combined.patch
Patch14:	%{name}-xml-inline.patch
Patch15:	%{name}-timetracking-advanced-logic.patch
Patch16:	%{name}-timedisplay.patch
Patch17:	%{name}-bug-17267.patch
Patch18:	%{name}-compact-issue-display.patch
Patch19:	%{name}-fixed-nav.patch
Patch20:	%{name}-scm-ssl.patch
Patch21:	%{name}-scm-quick-out.patch
Patch22:	%{name}-mem-limits.patch
Patch23:	%{name}-backtraces.patch
Patch24:	%{name}-errorhandler.patch
Patch25:	%{name}-unbalancedquotesinemailaddress.patch
# packaging patches that probably never go upstream
Patch100:	%{name}-paths.patch
Patch101:	%{name}-cvs-config.patch
Patch102:	%{name}-irc-mem.patch
Patch103:	%{name}-irc-config.patch
Patch104:	%{name}-PEAR.patch
Patch105:	%{name}-httpclient-clientside.patch
Patch106:	%{name}-bot-reconnect.patch
Patch107:	%{name}-private-key.patch
URL:		http://dev.mysql.com/downloads/other/eventum/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	sed >= 4.0
Requires(triggerpostun):	/usr/bin/php
Requires(triggerpostun):	sed >= 4.0
Requires:	%{name}-base = %{version}-%{release}
Requires:	Smarty >= 2.6.10-4
Requires:	apache(mod_dir)
Requires:	php >= 3:4.2.0
Requires:	php-gd
Requires:	php-imap
Requires:	php-mysql
Requires:	php-pcre
Requires:	php-pear-Benchmark
Requires:	php-pear-DB
Requires:	php-pear-Date
Requires:	php-pear-HTTP_Request
Requires:	php-pear-Mail
Requires:	php-pear-Mail_Mime
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
Requires:	webapps
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'pear(/etc/webapps/.*)' 'pear(jpgraph_dir.php)' 'pear(.*Smarty.class.php)'

%define		_libdir		%{_prefix}/lib/%{name}
%define		_appdir		%{_datadir}/%{name}
%define		_smartyplugindir	%{_appdir}/include/smarty
%define		_smartydir	/usr/share/php/Smarty
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

%description -l pl
Eventum to przyjazny dla u¿ytkownika system ¶ledzenia spraw, który
mo¿e byæ u¿ywany przez dzia³ obs³ugi do ¶ledzenia przychodz±cych ¿±dañ
obs³ugi technicznej albo przez zespó³ tworz±cy oprogramowanie do
szybkiej organizacji zadañ i b³êdów. Eventum jest u¿ywany przez zespó³
Technical Support MySQL AB i umo¿liwi³ im znacz±co poprawiæ czasy
reakcji.

%package base
Summary:	Eventum base package
Summary(pl):	Podstawowy pakiet Eventum
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

%description base -l pl
Ten pakiet zawiera podstawow± strukturê katalogów dla Eventum.

%package setup
Summary:	Eventum setup package
Summary(pl):	Pakiet do wstêpnej konfiguracji Eventum
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}

%description setup
Install this package to configure initial Eventum installation. You
should uninstall this package when you're done, as it considered
insecure to keep the setup files in place.

%description setup -l pl
Ten pakiet nale¿y zainstalowaæ w celu wstêpnej konfiguracji Eventum po
pierwszej instalacji. Potem nale¿y go odinstalowaæ, jako ¿e
pozostawienie plików instalacyjnych mog³oby byæ niebezpieczne.

%package mail-queue
Summary:	Eventum mail queue process
Summary(pl):	Przetwarzanie kolejki poczty Eventum
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

%description mail-queue -l pl
Od pierwszego wydania Eventum poczta nie jest wysy³ana bezpo¶rednio z
ró¿nych skryptów, lecz dodawana do kolejki przetwarzanej z crona.
Je¶li poczta nie mo¿e byæ wys³ana, bêdzie odpowiednio oznaczona w logu
kolejki poczty, a skrypt z crona bêdzie próbowa³ wys³aæ j± ponownie
nastêpnym razem.

Ten pakiet zawiera zadanie dla crona.

%package mail-download
Summary:	Eventum email download
Summary(pl):	¦ci±ganie poczty Eventum
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}
Requires:	crondaemon

%description mail-download
In order for Eventum's email integration feature to work, you need to
setup a cron job to run the script every so often.

This package contains the cron job.

%description mail-download -l pl
Aby integracja poczty elektronicznej w Eventum dzia³a³a, trzeba
ustawiæ zadanie crona, aby uruchamia³ odpowiedni skrypt wystarczaj±co
czêsto.

Ten pakiet zawiera zadanie dla crona.

%package reminder
Summary:	Eventum Reminder System
Summary(pl):	System przypominania dla Eventum
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

%description reminder -l pl
System przypominania zosta³ zaprojektowany tak, aby s³u¿y³ jako
bezpieczna sieæ dla spraw wymagaj±cych uwagi. W zale¿no¶ci od
konfiguracji mo¿na ustawiæ ró¿ne przypominajki (lub alarmy) wysy³ane
przy ka¿dej sprawie wymagaj±cej uwagi lub przy parametrze, który mo¿na
uwa¿aæ za potrzebny.

Ten pakiet zawiera zadanie dla crona.

%package monitor
Summary:	Eventum Heartbeat Monitor
Summary(pl):	Monitor ¿ycia dla Eventum
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}
Requires:	crondaemon
Requires:	php-posix

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

%description monitor -l pl
Monitor ¿ycia to funkcjonalno¶æ zaprojektowana dla administratora
chc±cego byæ alarmowanym przy ka¿dym wykryciu popularnego problemu z
Eventum, jak nie dzia³anie serwera bazy danych albo zmiana uprawnieñ
do plików konfiguracyjnych.

Nale¿y zauwa¿yæ, ¿e przed uruchomieniem tego monitora mo¿e byæ
konieczne dostosowanie niektórych testów do systemu, w szczególno¶ci
testów uprawnieñ i plików w Monitor::checkConfiguration().

Ten pakiet zawiera zadanie dla crona.

%package route-drafts
Summary:	Eventum Draft Routing
Summary(pl):	Przekazywanie szkiców dla Eventum
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}
Requires:	eventum(router)

%description route-drafts
The draft routing feature is used to automatically associate a thread
of drafts into an Eventum issue. By setting up qmail (or even Postfix)
to deliver emails sent to a specific address (usually
draft-<number>@<domain>) to the above script, users are able to send
drafts written in their mail client to be stored in Eventum. These
drafts will NOT broadcasted to the notification list.

%description route-drafts -l pl
Przekazywanie szkiców s³u¿y do automatycznego wi±zania w±tku szkiców z
problemem w Eventum. Ustawiaj±c qmaila (czy nawet Postfiksa), aby
dostarcza³ pocztê wys³an± na podany adres (zwykle
draft-<liczba>@<domena>) do tego skryptu umo¿liwia siê u¿ytkownikom
wysy³anie szkiców napisanych w ich kliencie pocztowym do zapisania w
Eventum. Szkice te NIE bêd± wysy³ane na listê powiadomieñ.

%package route-emails
Summary:	Eventum Email Routing
Summary(pl):	Przekazywanie poczty dla Eventum
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}
Requires:	eventum(router)

%description route-emails
The email routing feature is used to automatically associate a thread
of emails into an Eventum issue. By setting up qmail (or even postfix)
to deliver emails sent to a specific address (usually
issue-<number>@<domain>) to the above script, users are able to use
their email clients to reply to emails coming from Eventum, and those
replies will be automatically associated with the issue and
broadcasted to the entire notification list.

%description route-emails -l pl
Funkcjonalno¶æ przekazywania poczty s³u¿y do automatycznego wi±zania
w±tku listów ze spraw± w Eventum. Po ustawieniu qmaila (czy nawet
postfiksa), aby dostarcza³ listy wysy³ane na pewien adres (zwykle
issue-<numer>@<domena>) na powy¿szy skrypt, u¿ytkownicy bêd± mogli
u¿ywaæ klientów pocztowych do odpowiadania na listy przychodz±ce z
Eventum, a odpowiedzi te bêd± automatycznie wi±zane ze spraw± i
rozprowadzane do ca³ej listy og³oszeniowej.

%package route-notes
Summary:	Eventum Note Routing
Summary(pl):	Przekazywanie notatek dla Eventum
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}
Requires:	eventum(router)

%description route-notes
The note routing feature is used to automatically associate a thread
of notes into an Eventum issue. By setting up qmail (or even postfix)
to deliver emails sent to a specific address (usually
note-<number>@<domain>) to the above script, users are able to use
their email clients to reply to internal notes coming from Eventum,
and those replies will be automatically associated with the issue and
broadcasted to the notification list staff members.

%description route-notes -l pl
Funkcjonalno¶æ przekazywania notatek s³u¿y do automatycznego wi±zania
w±tku notatek ze spraw± w Eventum. Po ustawieniu qmaila (czy nawet
postfiksa), aby dostarcza³ listy wysy³ane na pewien adres (zwykle
note-<numer>@<domena>) na powy¿szy skrypt, u¿ytkownicy bêd± mogli
u¿ywaæ klientów pocztowych do odpowiadania na wewnêtrzne notatki
pochodz±ce od Eventu, a odpowiedzi te bêd± automatycznie wi±zane ze
spraw± i rozprowadzane do cz³onków personelu listy og³oszeniowej.

%package router-qmail
Summary:	Eventum Mail Routing - qmail
Summary(pl):	Przekazywanie poczty Eventum - qmail
Group:		Applications/Mail
# loose dep is intentional. qmail subpackage isn't built on PLD
# builders and there really nothing changes.
Requires:	%{name} >= %{version}-%{release}
Requires:	qmail >= 1.03
Provides:	eventum(router)
Obsoletes:	eventum(router)

%description router-qmail
This package provides way of routing notes and emails back to Eventum
via qmail.

%description router-qmail -l pl
Ten pakiet udostêpnia metodê przekazywania notatek i listów do Eventum
przez qmaila.

%package router-postfix
Summary:	Eventum Mail Routing - Postfix
Summary(pl):	Przekazywanie poczty Eventum - Postfix
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

%description router-postfix -l pl
Ten pakiet udostêpnia metodê przekazywania notatek i listów do Eventum
przez Postfiksa.

Opis konfiguracji Postfiksa mo¿na znale¼æ pod adresem
<http://eventum.mysql.org/wiki/index.php/Setting_up_email_routing_with_postfix>.

%package irc
Summary:	Eventum IRC Notification Bot
Summary(pl):	IRC-owy bot powiadamiaj±cy dla Eventum
Group:		Applications/WWW
Requires(post,preun):	/sbin/chkconfig
Requires(triggerpostun):	sed >= 4.0
Requires:	%{name} = %{version}-%{release}
Requires:	php-pear-Net_SmartIRC
Requires:	php-sockets
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

%description irc -l pl
IRC-owy bot powiadamiaj±cy to mi³a funkcjonalno¶æ dla zdalnych
zespo³ów chc±cych obs³ugiwaæ sprawy i mieæ szybki i ³atwy sposób na
uzyskiwanie prostych powiadomieñ. Aktualnie bot powiadamia o
nastêpuj±cych zdarzeniach:
- nowych sprawach
- zablokowanych listach
- sprawach, dla których zmieni³a siê lista powi±zañ

UWAGA: w celu wprowadzenia w³asnych ustawieñ, takich jak serwer IRC i
kana³ u¿ywany przez bota, trzeba rêcznie zmodyfikowaæ skrypt bot.php .

%package cli
Summary:	Eventum command-line interface
Summary(pl):	Interfejs linii poleceñ dla Eventum
Group:		Applications/WWW
Requires:	%{name}-base = %{version}-%{release}
Requires:	php-cli
Requires:	php-common >= 3:4.1.0
Requires:	php-pear-XML_RPC

%description cli
The Eventum command-line interface allows you to access most of the
features of the web interface straight from your command shell.

%description cli -l pl
Interfejs linii poleceñ Eventum pozwala na dostêp do wiêkszo¶ci
funkcji interfejsu WWW prosto z linii poleceñ pow³oki.

%package scm
Summary:	Eventum SCM integration
Summary(pl):	Integracja SCM dla Eventum
Group:		Applications/WWW
Requires:	%{name}-base = %{version}-%{release}
Requires:	php-cli
Requires:	php-common >= 3:4.1.0
Requires:	php-pcre

%description scm
This feature allows your software development teams to integrate your
Source Control Management system with your Issue Tracking System.

The integration is implemented in such a way that it will be forward
compatible with pretty much any SCM system, such as CVS.

For installation see
</eventum/help.php?topic=scm_integration_installation>.

%description scm -l pl
Ten pakiet pozwala zespo³om programistów na integracjê systemu
zarz±dzania ¼ród³ami (SCM - Source Control Management) z systemem
¶ledzenia spraw.

Integracja jest zaimplementowana tak, aby byæ kompatybilna w przód z
prawie ka¿dym systemem SCM, jak np. CVS.

Szczegó³y na temat instalacji mo¿na przeczytaæ pod
</eventum/help.php?topic=scm_integration_installation>.

%prep
%setup -q %{?_snap:-n %{name}-%{_snap}}
# undos the source
find . -type f -print0 | xargs -0 sed -i -e 's,\r$,,'

rm -f setup.conf.php # not to be installed by *.php glob
rm -rf misc/upgrade/*v1.[123]* # too old to support in PLD Linux
rm -f misc/upgrade/flush_compiled_templates.php
rm -rf misc/upgrade/*/upgrade_config.php # not needed in PLD Linux

# sample, not used in eventum
rm -f rpc/xmlrpc_client.php

# bug fixes.
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%{?with_order_patch:%patch11 -p1}
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
#%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1

# packaging
%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch107 -p1

cat <<'EOF'> mysql-permissions.sql
# use this schema if you want to grant permissions manually instead of using setup
# this schema is extracted from setup/index.php.
GRANT SELECT, UPDATE, DELETE, INSERT, ALTER, DROP, CREATE, INDEX ON eventum.* TO 'eventum'@'localhost' IDENTIFIED BY 'password';
EOF

sed -e '1s,#!.*/bin/php -q,#!%{_bindir}/php,' misc/cli/eventum > %{name}-cli
sed -e '1i#!%{_bindir}/php' misc/scm/process_cvs_commits.php > %{name}-scm
sed -e '1i#!%{_bindir}/php' misc/irc/bot.php > %{name}-bot
mv misc/cli/eventumrc_example eventumrc
sed -i -e '1i#!%{_bindir}/php' misc/*.php
chmod +x misc/*.php
mv include/private_key.php private_key.php.in

# replace in remaining scripts config.inc.php to system one
grep -rl 'include_once(".*config.inc.php")' . | xargs sed -i -e '
	s,include_once(".*config.inc.php"),include_once("%{_webappdir}/core.php"),
'

grep -rl 'APP_INC_PATH..*"private_key.php"' . | xargs sed -i -e '
	s,include_once(APP_INC_PATH.*"private_key.php"),include_once("%{_webappdir}/private_key.php"),
'

# remove backups from patching as we use globs to package files to buildroot
find '(' -name '*~' -o -name '*.orig' ')' | xargs -r rm -v

%install
rm -rf $RPM_BUILD_ROOT
install -d \
	$RPM_BUILD_ROOT{%{_webappdir},%{_sysconfdir},%{_bindir},%{_sbindir},%{_libdir}} \
	$RPM_BUILD_ROOT/etc/{rc.d/init.d,cron.d,sysconfig} \
	$RPM_BUILD_ROOT/var/{run,cache,lib}/%{name} \
	$RPM_BUILD_ROOT/var/log/{archiv/,}%{name} \
	$RPM_BUILD_ROOT/var/lib/%{name}/routed_{emails,drafts,notes} \
	$RPM_BUILD_ROOT%{_appdir}/{include,htdocs/misc,upgrade} \

cp -a *.php css customer images js manage reports rpc setup $RPM_BUILD_ROOT%{_appdir}/htdocs
cp -a misc/*.html $RPM_BUILD_ROOT%{_appdir}/htdocs/misc
cp -a misc/*.php $RPM_BUILD_ROOT%{_appdir}
cp -a templates $RPM_BUILD_ROOT%{_appdir}
cp -a include/{customer,custom_field,jpgraph,workflow} $RPM_BUILD_ROOT%{_appdir}/include
cp -a include/*.php $RPM_BUILD_ROOT%{_appdir}/include
cp -a logs/* $RPM_BUILD_ROOT/var/log/%{name}
cp -a misc/upgrade $RPM_BUILD_ROOT%{_appdir}

cp -a favicon.ico $RPM_BUILD_ROOT%{_appdir}/htdocs/favicon.ico
install %{SOURCE12} $RPM_BUILD_ROOT%{_appdir}/htdocs/setup/config.inc.php
install %{SOURCE13} $RPM_BUILD_ROOT%{_appdir}/upgrade/upgrade.sh

# cli
install -d $RPM_BUILD_ROOT%{_appdir}/cli
cp -a misc/cli/include/class.{misc,command_line}.php $RPM_BUILD_ROOT%{_appdir}/cli
cp -a misc/cli/config.inc.php $RPM_BUILD_ROOT%{_sysconfdir}/cli.php
install %{name}-cli $RPM_BUILD_ROOT%{_bindir}/%{name}
install %{name}-bot $RPM_BUILD_ROOT%{_sbindir}

# scm
install %{name}-scm $RPM_BUILD_ROOT%{_libdir}/scm
install %{SOURCE6} $RPM_BUILD_ROOT%{_sysconfdir}/cvs.php

# private key
cp -a private_key.php.in $RPM_BUILD_ROOT%{_webappdir}/private_key.php

install %{SOURCE1} $RPM_BUILD_ROOT%{_webappdir}/apache.conf
install %{SOURCE1} $RPM_BUILD_ROOT%{_webappdir}/httpd.conf
install %{SOURCE2} $RPM_BUILD_ROOT/etc/cron.d/%{name}-mail-queue
install %{SOURCE3} $RPM_BUILD_ROOT/etc/cron.d/%{name}-mail-download
install %{SOURCE4} $RPM_BUILD_ROOT/etc/cron.d/%{name}-reminder
install %{SOURCE5} $RPM_BUILD_ROOT/etc/cron.d/%{name}-monitor
install %{SOURCE7} $RPM_BUILD_ROOT%{_sysconfdir}/irc.php
install %{SOURCE8} $RPM_BUILD_ROOT/etc/rc.d/init.d/eventum-irc
install %{SOURCE9} $RPM_BUILD_ROOT/etc/sysconfig/eventum-irc

sed -e '
s,%%{APP_VERSION}%%,%{version}%{?_snap:-%{_snap}}%{?_rc:-%{_rc}},
s,%%{PHP_PEAR_DIR}%%,%{php_pear_dir},
s,%%{APP_PATH}%%,%{_appdir},
s,%%{SMARTY_DIR}%%,%{_smartydir},
s,%%{SYSCONFDIR}%%,%{_webappdir},
' %{SOURCE10} > $RPM_BUILD_ROOT%{_webappdir}/core.php

# config
> $RPM_BUILD_ROOT%{_webappdir}/setup.php
mv $RPM_BUILD_ROOT{%{_appdir}/htdocs/config.inc,%{_webappdir}/config}.php

install -d $RPM_BUILD_ROOT%{_smartyplugindir}
# These plugins are not in Smarty package (Smarty-2.6.2-3)
cp -a \
	include/Smarty/plugins/function.{calendar,get_{display_style,innerhtml,textarea_size}}.php \
	include/Smarty/plugins/modifier.highlight_quoted.php \
	$RPM_BUILD_ROOT%{_smartyplugindir}

# qmail router
%if %{with qmail}
d=$RPM_BUILD_ROOT/var/lib/%{name}
echo 'root' > $d/.qmail
echo 'root' > $d/.qmail-default
echo '| %{_libdir}/router-qmail drafts' > $d/.qmail-draft-default
echo '| %{_libdir}/router-qmail emails 1' > $d/.qmail-issue-default
echo '| %{_libdir}/router-qmail notes' > $d/.qmail-note-default
install %{SOURCE11} $RPM_BUILD_ROOT%{_libdir}/router-qmail
%endif
# postfix router
install %{SOURCE14} $RPM_BUILD_ROOT%{_libdir}/router-postfix

install -D %{SOURCE15} $RPM_BUILD_ROOT/etc/logrotate.d/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%addusertogroup http %{name}

%post
# check if the package is configured.
if grep -q 'header("Location: setup/")' %{_webappdir}/config.php; then
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
%{_webappdir}/apache.conf and restart apache.

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

%post router-qmail
CF=/etc/qmail/control/virtualdomains
if ! grep -q ':%{name}\b' $CF 2>/dev/null; then
	FQDN=$(awk -F'"' '/define/ && $2 ~ /APP_HOSTNAME/ {print $4}' %{_webappdir}/config.php 2>/dev/null)
	[ "$FQDN" ] || FQDN=$(hostname -f 2>/dev/null || echo localhost)
	umask 022
	echo "#${FQDN}:%{name}" >> $CF

%banner %{name}-qmail -e <<EOF

Added "#${FQDN}:%{name}" to $CF,
Please verify that it is correct and restart qmail:
# service qmail reload

Consult qmail-send(8) for more information on virtualdomains.

EOF
fi

%preun router-qmail
if [ "$1" = "0" ]; then
	sed -i -e '/:%{name}\b/d' /etc/qmail/control/virtualdomains
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

%triggerin -- apache1
%webapp_register apache %{_webapp}

%triggerun -- apache1
%webapp_unregister apache %{_webapp}

%triggerin -- apache < 2.2.0, apache-base
%webapp_register httpd %{_webapp}

%triggerun -- apache < 2.2.0, apache-base
%webapp_unregister httpd %{_webapp}

# FIXME
# only one upgrade trigger is called if you're upgrading over two
# versions, say 1.5 to 1.5.3, only 1.5.3 trigger is called.
# use common trigger (the highest version and rpmvercmp from poldek?)
%triggerpostun -- eventum < 1.5.1-0.257
%{_appdir}/upgrade/upgrade.sh %{_appdir}/upgrade/v1.5_to_v1.5.1 <<EOF
database_changes.php Perform database changes
EOF

%triggerpostun -- eventum < 1.5.2-0.289
%{_appdir}/upgrade/upgrade.sh %{_appdir}/upgrade/v1.5.1_to_v1.5.2 <<EOF
database_changes.php Perform database changes
set_priority_ranks.php Fix the ranking of priority values
EOF

%triggerpostun -- eventum < 1.5.3-0.291
%{_appdir}/upgrade/upgrade.sh %{_appdir}/upgrade/v1.5.2_to_v1.5.3 <<EOF
database_changes.php Perform database changes
EOF

%triggerpostun -- eventum < 1.5.4-1.12
%{_appdir}/upgrade/upgrade.sh %{_appdir}/upgrade/v1.5.3_to_v1.5.4 <<EOF
database_changes.php Perform database changes
EOF

%triggerpostun -- eventum < 1.6.0-RC2.6
%{_appdir}/upgrade/upgrade.sh %{_appdir}/upgrade/v1.5.5_to_v1.6.0 <<EOF
database_changes.php Perform database changes
upgrade_saved_searches.php Upgrade existing custom filters (saved searches)
EOF

%triggerpostun -- eventum < 1.6.1-0.2
%{_appdir}/upgrade/upgrade.sh %{_appdir}/upgrade/v1.6.0_to_v1.6.1 <<EOF
database_changes.php Perform database changes
EOF

%triggerpostun irc -- eventum-irc < 1.6.1-3.14
sed -i -e '
s,\$irc_host,$irc_server_hostname,
s,\$irc_port,$irc_server_port,
s,\$irc_nick,$nickname,
s,\$irc_realname,$realname,
s,\$irc_username,$username,
s,\$irc_password,$password,
' /etc/eventum/irc.php

%triggerpostun -- eventum < 1.7.0-2.0.48
# migrate from apache-config macros
if [ -f /etc/%{name}/apache.conf.rpmsave ]; then
	if [ -d /etc/apache/webapps.d ]; then
		cp -f %{_webapps}/%{_webapp}/apache.conf{,.rpmnew}
		cp -f /etc/%{name}/apache.conf.rpmsave %{_webapps}/%{_webapp}/apache.conf
	fi

	if [ -d /etc/httpd/webapps.d ]; then
		cp -f %{_webapps}/%{_webapp}/httpd.conf{,.rpmnew}
		cp -f /etc/%{name}/apache.conf.rpmsave %{_webapps}/%{_webapp}/httpd.conf
	fi
fi

if [ -L /etc/apache/conf.d/99_%{_webapp}.conf ]; then
	/usr/sbin/webapp register apache %{_webapp}
	rm -f /etc/apache/conf.d/99_%{_webapp}.conf
	%service -q apache reload
fi
if [ -L /etc/httpd/httpd.conf/99_%{_webapp}.conf ]; then
	/usr/sbin/webapp register httpd %{_webapp}
	rm -f /etc/httpd/httpd.conf/99_%{_webapp}.conf
	%service -q httpd reload
fi

%{_appdir}/upgrade/upgrade.sh %{_appdir}/upgrade/v1.6.1_to_v1.7.0 <<EOF
database_changes.php Perform database changes
set_root_message_ids.php Set iss_root_message_id
EOF

# regular configs
for i in apache.conf config.php private_key.php setup.php; do
	if [ -f /etc/eventum/$i.rpmsave ]; then
		mv -f %{_webappdir}/$i{,.rpmnew}
		mv -f /etc/eventum/$i.rpmsave %{_webappdir}/$i
	fi
done

%triggerpostun cli -- %{name}-cli < 1.7.0-3.4
if [ -f %{_webappdir}/cli.php.rpmsave ]; then
	mv -f %{_sysconfdir}/cli.php{,.rpmnew}
	mv -f %{_webappdir}/cli.php.rpmsave %{_sysconfdir}/cli.php
fi

%triggerpostun irc -- %{name}-irc < 1.7.0-3.4
if [ -f %{_webappdir}/irc.php.rpmsave ]; then
	mv -f %{_sysconfdir}/irc.php{,.rpmnew}
	mv -f %{_webappdir}/irc.php.rpmsave %{_sysconfdir}/irc.php
fi

%files
%defattr(644,root,root,755)
%doc ChangeLog FAQ INSTALL README UPGRADE CONTRIB
%doc docs/* setup/schema.sql mysql-permissions.sql
%attr(751,root,root) %dir %{_webappdir}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_webappdir}/apache.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_webappdir}/httpd.conf
%attr(640,root,eventum) %config(noreplace) %verify(not md5 mtime size) %{_webappdir}/config.php
%attr(640,root,eventum) %config(noreplace) %verify(not md5 mtime size) %{_webappdir}/private_key.php
%attr(660,root,eventum) %config(noreplace) %verify(not md5 mtime size) %{_webappdir}/setup.php
%attr(640,root,eventum) %config %verify(not mtime) %{_webappdir}/core.php

%dir %attr(731,root,eventum) /var/log/%{name}
%attr(620,root,eventum) %ghost /var/log/%{name}/*
%dir %attr(750,root,root) /var/log/archiv/%{name}
%config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/%{name}

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
%{_appdir}/templates
%dir %{_appdir}/upgrade
%attr(755,root,root) %{_appdir}/upgrade/upgrade.sh
%{_appdir}/upgrade/[!u]*
%{_smartyplugindir}

%dir %{_appdir}/include
%{_appdir}/include/customer
%{_appdir}/include/custom_field
%{_appdir}/include/jpgraph
%{_appdir}/include/workflow
%{_appdir}/include/class.[!m]*.php
%{_appdir}/include/class.mail.php
%{_appdir}/include/class.mail_queue.php
%{_appdir}/include/class.mime_helper.php
%{_appdir}/include/class.misc.php
%{_appdir}/include/db_access.php

%dir %attr(730,root,eventum) /var/run/%{name}
%dir %attr(730,root,eventum) /var/cache/%{name}

%files base
%defattr(644,root,root,755)
%attr(751,root,root) %dir %{_sysconfdir}
%dir %{_libdir}
%dir %{_appdir}
# qmail will ignore user, if it's home directory is not owned
%attr(750,eventum,eventum) %dir /var/lib/%{name}
# saved mail copies
%attr(770,root,eventum) %dir /var/lib/%{name}/routed_emails
%attr(770,root,eventum) %dir /var/lib/%{name}/routed_drafts
%attr(770,root,eventum) %dir /var/lib/%{name}/routed_notes

%files setup
%defattr(644,root,root,755)
%{_appdir}/htdocs/setup

%files mail-queue
%defattr(644,root,root,755)
%attr(755,root,root) %{_appdir}/process_mail_queue.php
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/cron.d/%{name}-mail-queue

%files mail-download
%defattr(644,root,root,755)
%attr(755,root,root) %{_appdir}/download_emails.php
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/cron.d/%{name}-mail-download

%files reminder
%defattr(644,root,root,755)
%attr(755,root,root) %{_appdir}/check_reminders.php
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/cron.d/%{name}-reminder

%files monitor
%defattr(644,root,root,755)
%{_appdir}/include/class.monitor.php
%attr(755,root,root) %{_appdir}/monitor.php
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

%if %{with qmail}
%files router-qmail
%defattr(644,root,root,755)
%attr(640,root,eventum) %config(noreplace) %verify(not md5 mtime size) /var/lib/%{name}/.qmail*
%attr(755,root,root) %{_libdir}/router-qmail
%endif

%files router-postfix
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/router-postfix

%files irc
%defattr(644,root,root,755)
%attr(640,root,eventum) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/irc.php
%attr(640,root,eventum) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/eventum-irc
%attr(755,root,root) %{_sbindir}/%{name}-bot
%attr(754,root,root) /etc/rc.d/init.d/%{name}-irc

%files cli
%defattr(644,root,root,755)
%doc eventumrc
%attr(644,root,root) %config %verify(not md5 mtime size) %{_sysconfdir}/cli.php
%attr(755,root,root) %{_bindir}/%{name}
%{_appdir}/cli

%files scm
%defattr(644,root,root,755)
%attr(644,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/cvs.php
%attr(755,root,root) %{_libdir}/scm
