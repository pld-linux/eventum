# TODO
# - system pear is incompatible, at least pear DB class seems broke Eventum
# - php5 is not tested, but not placing hard conflict on it, as it prevents php4 & php coinstallation
# - discard bundled packages (from INSTALL):
#  - JpGraph 1.5.3 (last GPL version)
#  - dTree 2.0.5 (http://www.destroydrop.com/javascript/tree/)
#  - dynCalendar.js (http://www.phpguru.org/dyncalendar.html)
#  - overLIB 3.5.1 (http://www.bosrup.com/web/overlib/)
#  - A few other small javascript libraries
# - need start-stop-daemon (from dpkg for now)
# - 64bit platforms beware? http://bugs.php.net/bug.php?id=30215 (it's actually Smarty related problem)

%bcond_with	pear	# build with system PEAR packages (or use bundled ones)

%define	uid	146
%define	gid	146

# snapshot: DATE
#define _snap 20050227

%if 0%{?_snap}
%define _source http://downloads.mysql.com/snapshots/%{name}/%{name}-nightly-%{_snap}.tar.gz
%else
%define _source http://mysql.wildyou.net/Downloads/%{name}/%{name}-%{version}.tar.gz
%endif

%define _rel 278

Summary:	Eventum Issue / Bug tracking system
Summary(pl):	Eventum - system ¶ledzenia spraw/b³êdów
Name:		eventum
Version:	1.5.1
Release:	0.%{?_snap:%{_snap}.}%{_rel}
License:	GPL
Group:		Applications/WWW
Source0:	%{_source}
# Source0-md5:	d326ef39b52001efcbbc0ae8db5454a5
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
Source12:	http://dev.mysql.com/common/favicon.ico
# Source12-md5:	858be0130832da4144c08d4b59116411
Patch0:		%{name}-paths.patch
Patch1:		%{name}-cvs-config.patch
Patch2:		%{name}-irc-config.patch
Patch3:		%{name}-PEAR.patch
Patch4:		%{name}-db-20050227.patch
Patch10:	%{name}-charset-recent-activity.patch
Patch11:	http://glen.alkohol.ee/pld/%{name}-cli-rpc-base64.patch
Patch12:	http://glen.alkohol.ee/pld/%{name}-send-height.patch
Patch13:	http://glen.alkohol.ee/pld/%{name}-reply-subject.patch
Patch14:	http://glen.alkohol.ee/pld/%{name}-rss-updates.patch
Patch15:	http://glen.alkohol.ee/pld/%{name}-opera.patch
Patch16:	%{name}-lf.patch
Patch17:	%{name}-iss-ass-fix.patch
Patch18:	%{name}-iss-close.patch
Patch19:	http://glen.alkohol.ee/pld/%{name}-attach-activate-links.patch
Patch20:	%{name}-irc-memlimit.patch
Patch21:	http://glen.alkohol.ee/pld/eventum-link-tilde2.patch
Patch22:	http://glen.alkohol.ee/pld/eventum-reply-timestamp.patch
URL:		http://dev.mysql.com/downloads/other/eventum/
BuildRequires:	rpmbuild(macros) >= 1.177
BuildRequires:	sed >= 4.0
Requires:	php >= 4.2.0
Requires:	php-gd
Requires:	php-imap
Requires:	php-mysql
Requires:	php-pcre
Requires:	%{name}-base = %{epoch}:%{version}-%{release}
Requires:	Smarty >= 2.6.2
%if %{with pear}
Requires:	php-pear-Benchmark
Requires:	php-pear-DB
Requires:	php-pear-Date
Requires:	php-pear-HTTP_Request
Requires:	php-pear-Mail
Requires:	php-pear-Math_Stats
Requires:	php-pear-Net_DIME
Requires:	php-pear-Net_POP3
Requires:	php-pear-Net_SMTP
Requires:	php-pear-Net_SmartIRC
Requires:	php-pear-Net_Socket
Requires:	php-pear-Net_URL
Requires:	php-pear-Net_UserAgent_Detect
Requires:	php-pear-PEAR
Requires:	php-pear-Text_Diff
Requires:	php-pear-XML_RPC
%endif
Requires:	apache >= 1.3.33-2
Requires:	apache(mod_dir)
Requires(triggerpostun):	sed >= 4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/%{name}
%define		_libdir		%{_prefix}/%{_lib}/%{name}
%define		_appdir	%{_datadir}/%{name}
%define		_smartyplugindir	%{php_pear_dir}/Smarty/plugins

%define		_apache1dir	/etc/apache
%define		_apache2dir	/etc/httpd

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

%description base
This package contains base directory structure for Eventum.

%description base -l pl
Ten pakiet zawiera podstawow± strukturê katalogów dla Eventum.

%package setup
Summary:	Eventum setup package
Summary(pl):	Pakiet do wstêpnej konfiguracji Eventum
Group:		Applications/WWW
PreReq:		%{name} = %{epoch}:%{version}-%{release}

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
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	crondaemon
Requires:	php >= 4.1.0

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
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	crondaemon
Requires:	php >= 4.1.0

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
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	php >= 4.1.0
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
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	php >= 4.1.0
Requires:	php-posix
Requires:	crondaemon

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

%package route-emails
Summary:	Eventum Email Routing
Summary(pl):	Przekazywanie poczty dla Eventum
Group:		Applications/WWW
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	php >= 4.1.0
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
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	php >= 4.1.0
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
Requires:	%{name} = %{epoch}:%{version}-%{release}
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
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	postfix
Provides:	eventum(router)
Obsoletes:	eventum(router)

%description router-postfix
This package provides way of routing notes and emails back to Eventum
via Postfix.

%description router-postfix -l pl
Ten pakiet udostêpnia metodê przekazywania notatek i listów do Eventum
przez Postfiksa.

%package irc
Summary:	Eventum IRC Notification Bot
Summary(pl):	IRC-owy bot powiadamiaj±cy dla Eventum
Group:		Applications/WWW
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	php >= 4.1.0
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
Requires:	%{name}-base = %{epoch}:%{version}-%{release}
Requires:	php >= 4.1.0
Requires:	php-cli
Requires:	php-curl
Requires:	php-xml
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
Requires:	%{name}-base = %{epoch}:%{version}-%{release}
Requires:	php >= 4.1.0

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
find . -type f -print0 | xargs -0 sed -i -e 's,
$,,'

# packaging
%patch0 -p1 -b .paths
%patch1 -p1
%patch2 -p1
%{?with_pear:%patch3 -p1 -b .PEAR}
%patch4 -p1

# bug fixes.
%patch10 -p1
%patch11 -p1
%patch12 -p0
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1

# replace in remaining scripts config.inc.php to system one
grep -rl 'include_once(".*config.inc.php")' . | xargs sed -i -e '
	s,include_once(".*config.inc.php"),include_once("%{_sysconfdir}/core.php"),
'
sed -i -e '
	s,include(".*config.inc.php"),include_once("%{_sysconfdir}/core.php"),
' misc/download_emails.php

grep -rl 'APP_INC_PATH..*"private_key.php"' . | xargs sed -i -e '
	s,include_once(APP_INC_PATH.*"private_key.php"),include_once("%{_sysconfdir}/private_key.php"),
'

rm -f */*~ */*/*~

%install
rm -rf $RPM_BUILD_ROOT
install -d \
	$RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir},%{_libdir}} \
	$RPM_BUILD_ROOT/etc/{rc.d/init.d,cron.d,sysconfig} \
	$RPM_BUILD_ROOT/var/{run,log,cache,lib}/%{name} \
	$RPM_BUILD_ROOT%{_appdir}/{include,htdocs/misc,upgrade} \

cp -a *.php css customer images js manage reports rpc setup $RPM_BUILD_ROOT%{_appdir}/htdocs
cp -a misc/*.html $RPM_BUILD_ROOT%{_appdir}/htdocs/misc
cp -a misc/*.php $RPM_BUILD_ROOT%{_appdir}
cp -a misc/irc $RPM_BUILD_ROOT%{_appdir}
cp -a templates $RPM_BUILD_ROOT%{_appdir}
cp -a include/{customer,jpgraph,pear,workflow} $RPM_BUILD_ROOT%{_appdir}/include
cp -a include/*.php $RPM_BUILD_ROOT%{_appdir}/include
cp -a logs/* $RPM_BUILD_ROOT/var/log/%{name}
cp -a misc/upgrade $RPM_BUILD_ROOT%{_appdir}

install %{SOURCE12} $RPM_BUILD_ROOT%{_appdir}/htdocs/favicon.ico

# cli
install -d $RPM_BUILD_ROOT%{_appdir}/cli
install misc/cli/include/class.{misc,command_line}.php $RPM_BUILD_ROOT%{_appdir}/cli
install misc/cli/config.inc.php $RPM_BUILD_ROOT%{_sysconfdir}/cli.php
sed -e '1s,#!.*/bin/php,#!%{_bindir}/php4,' \
	misc/cli/eventum > $RPM_BUILD_ROOT%{_bindir}/%{name}
cp -f misc/cli/eventumrc_example eventumrc

# scm
echo '#!%{_bindir}/php4 -q' > %{name}-scm
cat misc/scm/process_cvs_commits.php >> %{name}-scm
install %{name}-scm $RPM_BUILD_ROOT%{_libdir}/scm

# private key
mv $RPM_BUILD_ROOT{%{_appdir}/include/private_key.php,%{_sysconfdir}}
# change private key, so we can easily grep
sed -i -e '
s,$private_key\s*=\s*".*";,$private_key = "DEFAULTPRIVATEKEYPLEASERUNSETUP!";,
' $RPM_BUILD_ROOT%{_sysconfdir}/private_key.php

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/apache.conf
install %{SOURCE2} $RPM_BUILD_ROOT/etc/cron.d/%{name}-mail-queue
install %{SOURCE3} $RPM_BUILD_ROOT/etc/cron.d/%{name}-mail-download
install %{SOURCE4} $RPM_BUILD_ROOT/etc/cron.d/%{name}-reminder
install %{SOURCE5} $RPM_BUILD_ROOT/etc/cron.d/%{name}-monitor
install %{SOURCE6} $RPM_BUILD_ROOT%{_sysconfdir}/cvs.php
install %{SOURCE7} $RPM_BUILD_ROOT%{_sysconfdir}/irc.php
install %{SOURCE8} $RPM_BUILD_ROOT/etc/rc.d/init.d/eventum-irc
install %{SOURCE9} $RPM_BUILD_ROOT/etc/sysconfig/eventum-irc
sed -e 's,%%{APP_VERSION}%%,%{version}%{?_snap:-%{_snap}},' \
	%{SOURCE10} > $RPM_BUILD_ROOT%{_sysconfdir}/core.php

# config
> $RPM_BUILD_ROOT%{_sysconfdir}/setup.php
mv $RPM_BUILD_ROOT{%{_appdir}/htdocs/config.inc,%{_sysconfdir}/config}.php

# sample, not used in eventum
rm -f $RPM_BUILD_ROOT%{_appdir}/htdocs/rpc/xmlrpc_client.php

%if %{with pear}
# provided by PEAR
rm -rf $RPM_BUILD_ROOT%{_appdir}/include/pear
%endif

# use system Smarty
rm -rf $RPM_BUILD_ROOT%{_appdir}/include/Smarty
install -d $RPM_BUILD_ROOT%{_smartyplugindir}
# These plugins are not in Smarty package (Smarty-2.6.2-3)
cp -a include/Smarty/plugins/function.{calendar,get_{display_style,innerhtml,textarea_size}}.php \
	$RPM_BUILD_ROOT%{_smartyplugindir}

# qmail router
d=$RPM_BUILD_ROOT/var/lib/%{name}
echo 'root' > $d/.qmail
echo 'root' > $d/.qmail-default
echo '| %{_libdir}/router-qmail drafts' > $d/.qmail-draft-default
echo '| %{_libdir}/router-qmail emails 1' > $d/.qmail-issue-default
echo '| %{_libdir}/router-qmail notes' > $d/.qmail-note-default
install %{SOURCE11} $RPM_BUILD_ROOT%{_libdir}/router-qmail

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%addusertogroup http %{name}

%post
# apache1
if [ -d %{_apache1dir}/conf.d ]; then
	ln -sf %{_sysconfdir}/apache.conf %{_apache1dir}/conf.d/99_%{name}.conf
	if [ -f /var/lock/subsys/apache ]; then
		/etc/rc.d/init.d/apache restart 1>&2
	fi
fi
# apache2
if [ -d %{_apache2dir}/httpd.conf ]; then
	ln -sf %{_sysconfdir}/apache.conf %{_apache2dir}/httpd.conf/99_%{name}.conf
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

# check if the package is configured.
if grep -q 'header("Location: setup/")' %{_sysconfdir}/config.php; then
if [ -f %{_appdir}/htdocs/setup/index.php ]; then
%banner %{name} -e <<EOF

You haven't yet configured Eventum!
Please open in browser <http://localhost/eventum/>
If you need access from elsewhere, you need to edit
%{_sysconfdir}/apache.conf and restart apache.

IMPORTANT: When You have configured Eventum, please uninstall the
setup package, so that %{name}-setup is able to secure your Eventum
installation.

EOF
#' vim stupidity.
else
%banner %{name} -e <<EOF

You haven't yet configured Eventum!

To setup eventum, please install %{name}-setup and open in browser
<http://localhost/eventum/>.
If you need access from elsewhere, you need to edit
%{_sysconfdir}/apache.conf and restart apache.

IMPORTANT: When You have configured Eventum, please uninstall the
setup package, so that %{name}-setup is able to secure your Eventum
installation.

EOF
#' vim stupidity.
fi

elif grep -q 'DEFAULTPRIVATEKEY' %{_sysconfdir}/private_key.php; then
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
	# apache1
	if [ -f %{_apache1dir}/apache.conf ]; then
		rm -f %{_apache1dir}/conf.d/99_%{name}.conf
		if [ -f /var/lock/subsys/apache ]; then
			/etc/rc.d/init.d/apache restart 1>&2
		fi
	fi
	# apache2
	if [ -d %{_apache2dir}/httpd.conf ]; then
		rm -f %{_apache2dir}/httpd.conf/99_%{name}.conf
		if [ -f /var/lock/subsys/httpd ]; then
			/etc/rc.d/init.d/httpd restart 1>&2
		fi
	fi
fi

%postun
# nuke cache
rm -f /var/cache/eventum/*.php

%pre base
%groupadd -P %{name}-base %{name}
%useradd -P %{name}-base -d /var/lib/%{name} -g %{name} %{name} -c "Eventum User"

%postun base
if [ "$1" = "0" ]; then
	%userremove %{name}
	%groupremove %{name}
fi

%post router-qmail
CF=/etc/qmail/control/virtualdomains
if ! grep -q ':%{name}\b' $CF 2>/dev/null; then
	FQDN=$(awk -F'"' '/define/ && $2 ~ /APP_HOSTNAME/ {print $4}' %{_sysconfdir}/config.php 2>/dev/null)
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
chmod 660 %{_sysconfdir}/{config,private_key}.php
chown root:eventum %{_sysconfdir}/{config,private_key}.php

%postun setup
if [ "$1" = "0" ]; then
	chmod 640 %{_sysconfdir}/{config,private_key}.php
	chown root:eventum %{_sysconfdir}/{config,private_key}.php
fi

%triggerpostun base -- eventum-base < 1.4-2.20050222.212
if [ "`getent passwd %{name} | cut -d: -f6`" = "%{_appdir}" ]; then
	/usr/sbin/usermod -d /var/lib/%{name} %{name}
fi

%triggerpostun -- eventum < 1.5-0.240
scriptdir=%{_appdir}/upgrade/v1.4_to_1.5
%banner %{name}-trigger-1.5 -e <<-EOF

	Running eventum upgrade scripts to 1.5 in $scriptdir
	These will fail if your eventum user doesn't have ALTER privilege to database.

EOF
#'

/usr/bin/php4 -q $scriptdir/database_changes.php || {
	echo >&2 "Please run manually: /usr/bin/php4 -q $scriptdir/database_changes.php"
}

%triggerpostun -- eventum < 1.5.1-0.257
scriptdir=%{_appdir}/upgrade/v1.5_to_v1.5.1
%banner %{name}-trigger-1.5.1 -e <<-EOF

	Running eventum upgrade scripts to 1.5.1 in $scriptdir
	These will fail if your eventum user doesn't have ALTER privilege to database.

EOF
#'

/usr/bin/php4 -q $scriptdir/database_changes.php || {
	echo >&2 "Please run manually: /usr/bin/php4 -q $scriptdir/database_changes.php"
}

%files
%defattr(644,root,root,755)
%doc ChangeLog FAQ INSTALL README UPGRADE
%doc docs/* rpc/xmlrpc_client.php setup/schema.sql
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/apache.conf
%attr(640,root,eventum) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/config.php
%attr(640,root,eventum) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/private_key.php
%attr(660,root,eventum) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/setup.php
%attr(640,root,eventum) %config %verify(not mtime) %{_sysconfdir}/core.php

%dir %attr(731,root,eventum) /var/log/%{name}
%attr(620,root,eventum) %ghost /var/log/%{name}/*

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
%{_appdir}/upgrade

%{_smartyplugindir}/*
%if %{without pear}
%{_appdir}/include/pear
%endif

%dir %{_appdir}/include
%{_appdir}/include/customer
%{_appdir}/include/jpgraph
%{_appdir}/include/workflow
%{_appdir}/include/class.[!m]*.php
%{_appdir}/include/class.mail.php
%{_appdir}/include/class.mail_queue.php
%{_appdir}/include/class.mime_helper.php
%{_appdir}/include/class.misc.php
%{_appdir}/include/db_access.php
%{_appdir}/include/jsrsServer.inc.php

%dir %attr(730,root,eventum) /var/run/%{name}
%dir %attr(730,root,eventum) /var/cache/%{name}

%files base
%defattr(644,root,root,755)
%attr(751,root,root) %dir %{_sysconfdir}
%dir %{_libdir}
%dir %{_appdir}
# qmail will ignore user, if it's home directory is not owned
%attr(750,eventum,eventum) %dir /var/lib/%{name}

%files setup
%defattr(644,root,root,755)
%{_appdir}/htdocs/setup

%files mail-queue
%defattr(644,root,root,755)
%{_appdir}/process_mail_queue.php
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/cron.d/%{name}-mail-queue

%files mail-download
%defattr(644,root,root,755)
%{_appdir}/download_emails.php
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/cron.d/%{name}-mail-download

%files reminder
%defattr(644,root,root,755)
%{_appdir}/check_reminders.php
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/cron.d/%{name}-reminder

%files monitor
%defattr(644,root,root,755)
%{_appdir}/include/class.monitor.php
%{_appdir}/monitor.php
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/cron.d/%{name}-monitor

%files route-emails
%defattr(644,root,root,755)
%{_appdir}/route_emails.php

%files route-notes
%defattr(644,root,root,755)
%{_appdir}/route_drafts.php
%{_appdir}/route_notes.php

%files router-qmail
%defattr(644,root,root,755)
%attr(640,root,eventum) %config(noreplace) %verify(not md5 mtime size) /var/lib/%{name}/.qmail*
%attr(755,root,root) %{_libdir}/router-qmail

%files router-postfix
%defattr(644,root,root,755)

%files irc
%defattr(644,root,root,755)
%attr(640,root,eventum) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/irc.php
%attr(640,root,eventum) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/eventum-irc
%{_appdir}/irc
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
