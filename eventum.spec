# TODO
# - system pear is incompatible, at least pear DB class seems broke Eventum
# - php5 is not tested, but not placing hard conflict on it, as it prevents php4 & php coinstallation
# - discard bundled packages (from INSTALL):
#  - JpGraph 1.5.3 (last GPL version)
#  - dTree 2.0.5 (http://www.destroydrop.com/javascript/tree/)
#  - dynCalendar.js (http://www.phpguru.org/dyncalendar.html)
#  - overLIB 3.5.1 (http://www.bosrup.com/web/overlib/)
#  - A few other small javascript libraries
# - create eventum-router-qmail, eventum-router-postfix for -route-mails and -route-notes
# - need start-stop-daemon (from dpkg for now)
# - use eventum user for irc bot?

%bcond_with	pear	# build with system PEAR packages (or use bundled ones)

# snapshot: DATE
%define _snap 20050222

%if 0%{?_snap}
%define _source http://downloads.mysql.com/snapshots/%{name}/%{name}-nightly-%{_snap}.tar.gz
%else
%define _source http://mysql.wildyou.net/Downloads/%{name}/%{name}-%{version}.tar.gz
%endif

%define _rel 2.200

Summary:	Eventum Issue - a bug tracking system
Summary(pl):	Eventum - system �ledzenia spraw/b��d�w
Name:		eventum
Version:	1.4
Release:	%{?_snap:2.%{_snap}.}%{_rel}
License:	GPL
Group:		Applications/WWW
Source0:	%{_source}
# Source0-md5:	035bd8f7890260c1c058eaf1d54dcc90
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
Patch0:		%{name}-paths.patch
Patch1:		%{name}-scm-encode.patch
Patch2:		%{name}-cvs-config.patch
Patch3:		%{name}-irc-config.patch
Patch4:		%{name}-PEAR.patch
Patch11:		%{name}-scm_checkin_associated.patch
Patch12:		%{name}-mail-queue.tpl.patch
Patch13:		%{name}-maildecode.patch
Patch14:		%{name}-send-typo.patch
Patch15:		%{name}-fixes.patch
Patch16:		%{name}-rss-charset.patch
Patch17:		%{name}-scm-silence-add.patch
Patch18:		%{name}-default-TZ.patch
Patch19:		%{name}-charset-mailsubj.patch
URL:		http://dev.mysql.com/downloads/other/eventum/index.html
BuildRequires:	rpmbuild(macros) >= 1.177
BuildRequires:	sed >= 4.0
# is_a(), which wrapper we removed from config, is from 4.2.0
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
Eventum to przyjazny dla u�ytkownika system �ledzenia spraw, kt�ry
mo�e by� u�ywany przez dzia� obs�ugi do �ledzenia przychodz�cych ��da�
obs�ugi technicznej albo przez zesp� tworz�cy oprogramowanie do
szybkiej organizacji zada� i b��d�w. Eventum jest u�ywany przez zesp�
Technical Support MySQL AB i umo�liwi� im znacz�co poprawi� czasy
reakcji.

%package base
Summary:	Eventum base package
Summary(pl):	Podstawowy pakiet Eventum
Group:		Applications/WWW

%description base
This package contains base directory structure for Eventum.

%description base -l pl
Ten pakiet zawiera podstawow� struktur� katalog�w dla Eventum.

%package setup
Summary:	Eventum setup package
Summary(pl):	Pakiet do wst�pnej konfiguracji Eventum
Group:		Applications/WWW
PreReq:		%{name} = %{epoch}:%{version}-%{release}

%description setup
Install this package to configure initial Eventum installation. You
should uninstall this package when you're done, as it considered
insecure to keep the setup files in place.

%description setup -l pl
Ten pakiet nale�y zainstalowa� w celu wst�pnej konfiguracji Eventum po
pierwszej instalacji. Potem nale�y go odinstalowa�, jako �e
pozostawienie plik�w instalacyjnych mog�oby by� niebezpieczne.

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
Od pierwszego wydania Eventum poczta nie jest wysy�ana bezpo�rednio z
r�nych skrypt�w, lecz dodawana do kolejki przetwarzanej z crona.
Je�li poczta nie mo�e by� wys�ana, b�dzie odpowiednio oznaczona w logu
kolejki poczty, a skrypt z crona b�dzie pr�bowa� wys�a� j� ponownie
nast�pnym razem.

Ten pakiet zawiera zadanie dla crona.

%package mail-download
Summary:	Eventum email download
Summary(pl):	�ci�ganie poczty Eventum
Group:		Applications/WWW
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	crondaemon
Requires:	php >= 4.1.0

%description mail-download
In order for Eventum's email integration feature to work, you need to
setup a cron job to run the script every so often.

This package contains the cron job.

%description mail-download -l pl
Aby integracja poczty elektronicznej w Eventum dzia�a�a, trzeba
ustawi� zadanie crona, aby uruchamia� odpowiedni skrypt wystarczaj�co
cz�sto.

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
System przypominania zosta� zaprojektowany tak, aby s�u�y� jako
bezpieczna sie� dla spraw wymagaj�cych uwagi. W zale�no�ci od
konfiguracji mo�na ustawi� r�ne przypominajki (lub alarmy) wysy�ane
przy ka�dej sprawie wymagaj�cej uwagi lub przy parametrze, kt�ry mo�na
uwa�a� za potrzebny.

Ten pakiet zawiera zadanie dla crona.

%package monitor
Summary:	Eventum Heartbeat Monitor
Summary(pl):	Monitor �ycia dla Eventum
Group:		Applications/WWW
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	php >= 4.1.0
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
Monitor �ycia to funkcjonalno�� zaprojektowana dla administratora
chc�cego by� alarmowanym przy ka�dym wykryciu popularnego problemu z
Eventum, jak nie dzia�anie serwera bazy danych albo zmiana uprawnie�
do plik�w konfiguracyjnych.

Nale�y zauwa�y�, �e przed uruchomieniem tego monitora mo�e by�
konieczne dostosowanie niekt�rych test�w do systemu, w szczeg�lno�ci
test�w uprawnie� i plik�w w Monitor::checkConfiguration().

Ten pakiet zawiera zadanie dla crona.

%package route-emails
Summary:	Eventum Email Routing
Summary(pl):	Przekazywanie poczty dla Eventum
Group:		Applications/WWW
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	php >= 4.1.0
#Requires:	eventum-router

%description route-emails
The email routing feature is used to automatically associate a thread
of emails into an Eventum issue. By setting up qmail (or even postfix)
to deliver emails sent to a specific address (usually
issue-<number>@<domain>) to the above script, users are able to use
their email clients to reply to emails coming from Eventum, and those
replies will be automatically associated with the issue and
broadcasted to the entire notification list.

%description route-emails -l pl
Funkcjonalno�� przekazywania poczty s�u�y do automatycznego wi�zania
w�tku list�w ze spraw� w Eventum. Po ustawieniu qmaila (czy nawet
postfiksa), aby dostarcza� listy wysy�ane na pewien adres (zwykle
issue-<numer>@<domena>) na powy�szy skrypt, u�ytkownicy b�d� mogli
u�ywa� klient�w pocztowych do odpowiadania na listy przychodz�ce z
Eventum, a odpowiedzi te b�d� automatycznie wi�zane ze spraw� i
rozprowadzane do ca�ej listy og�oszeniowej.

%package route-notes
Summary:	Eventum Note Routing
Summary(pl):	Przekazywanie notatek dla Eventum
Group:		Applications/WWW
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	php >= 4.1.0
#Requires:	eventum-router

%description route-notes
The note routing feature is used to automatically associate a thread
of notes into an Eventum issue. By setting up qmail (or even postfix)
to deliver emails sent to a specific address (usually
note-<number>@<domain>) to the above script, users are able to use
their email clients to reply to internal notes coming from Eventum,
and those replies will be automatically associated with the issue and
broadcasted to the notification list staff members.

%description route-notes -l pl
Funkcjonalno�� przekazywania notatek s�u�y do automatycznego wi�zania
w�tku notatek ze spraw� w Eventum. Po ustawieniu qmaila (czy nawet
postfiksa), aby dostarcza� listy wysy�ane na pewien adres (zwykle
note-<numer>@<domena>) na powy�szy skrypt, u�ytkownicy b�d� mogli
u�ywa� klient�w pocztowych do odpowiadania na wewn�trzne notatki
pochodz�ce od Eventu, a odpowiedzi te b�d� automatycznie wi�zane ze
spraw� i rozprowadzane do cz�onk�w personelu listy og�oszeniowej.

%package irc
Summary:	Eventum IRC Notification Bot
Summary(pl):	IRC-owy bot powiadamiaj�cy dla Eventum
Group:		Applications/WWW
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	php >= 4.1.0
Requires:	php-sockets
# FIXME just need start-stop-daemon
Requires:	dpkg

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
IRC-owy bot powiadamiaj�cy to mi�a funkcjonalno�� dla zdalnych
zespo��w chc�cych obs�ugiwa� sprawy i mie� szybki i �atwy spos�b na
uzyskiwanie prostych powiadomie�. Aktualnie bot powiadamia o
nast�puj�cych zdarzeniach:
- nowych sprawach
- zablokowanych listach
- sprawach, dla kt�rych zmieni�a si� lista powi�za�

UWAGA: w celu wprowadzenia w�asnych ustawie�, takich jak serwer IRC i
kana� u�ywany przez bota, trzeba r�cznie zmodyfikowa� skrypt bot.php .

%package cli
Summary:	Eventum command-line interface
Summary(pl):	Interfejs linii polece� dla Eventum
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
Interfejs linii polece� Eventum pozwala na dost�p do wi�kszo�ci
funkcji interfejsu WWW prosto z linii polece� pow�oki.

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
Ten pakiet pozwala zespo�om programist�w na integracj� systemu
zarz�dzania �r�d�ami (SCM - Source Control Management) z systemem
�ledzenia spraw.

Integracja jest zaimplementowana tak, aby by� kompatybilna w prz�d z
prawie ka�dym systemem SCM, jak np. CVS.

Szczeg�y na temat instalacji mo�na przeczyta� pod
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
%patch3 -p1
%{?with_pear:%patch4 -p1 -b .PEAR}

# bug fixes.
%patch11 -p1
#%patch12 -p1
#%patch13 -p1
#%patch14 -p1
#%patch15 -p1
#%patch16 -p1
#%patch17 -p1
#%patch18 -p1
%patch19 -p1

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
	$RPM_BUILD_ROOT/var/{run,log,cache}/%{name} \
	$RPM_BUILD_ROOT%{_appdir}/{include,htdocs/misc} \

cp -a *.php css customer images js manage reports rpc setup $RPM_BUILD_ROOT%{_appdir}/htdocs
cp -a misc/*.html $RPM_BUILD_ROOT%{_appdir}/htdocs/misc
cp -a misc/*.php $RPM_BUILD_ROOT%{_appdir}
cp -a misc/irc $RPM_BUILD_ROOT%{_appdir}
cp -a templates $RPM_BUILD_ROOT%{_appdir}
cp -a include/{customer,jpgraph,pear,workflow} $RPM_BUILD_ROOT%{_appdir}/include
cp -a include/*.php $RPM_BUILD_ROOT%{_appdir}/include
cp -a logs/* $RPM_BUILD_ROOT/var/log/%{name}

# cli
install -d $RPM_BUILD_ROOT%{_appdir}/cli
install misc/cli/include/class.{misc,command_line}.php $RPM_BUILD_ROOT%{_appdir}/cli
install misc/cli/config.inc.php $RPM_BUILD_ROOT%{_sysconfdir}/cli.php
sed -e 's,/usr/local/bin/php,/usr/bin/php4,' misc/cli/eventum \
	> $RPM_BUILD_ROOT%{_bindir}/%{name}
cp -f misc/cli/eventumrc_example eventumrc

# scm
echo '#!/usr/bin/php4 -q' > %{name}-scm
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

%clean
rm -rf $RPM_BUILD_ROOT

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
%banner %{name} -e <<EOF

You haven't yet configured Eventum!

Install %{name}-setup and open up http://yourserver/eventum/
-- that will help you setup initial config.

when have configured Eventum, please uninstall the setup package,
so that %{name}-setup is able to secure your Eventum installation.

EOF
#' vim stupidity.

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

%post setup
chmod 660 %{_sysconfdir}/{config,private_key}.php
chown root:http %{_sysconfdir}/{config,private_key}.php

%postun setup
if [ "$1" = "0" ]; then
	chmod 640 %{_sysconfdir}/{config,private_key}.php
	chown root:http %{_sysconfdir}/{config,private_key}.php
fi

%triggerpostun -- eventum < 1.4-2.160
cp -f %{_sysconfdir}/config.php{,.rpmsave}
# very loose trigger
sed -i -e '
/config.php/,/SQL variables/d;/_LOG/d;/APP_VERSION/d;/APP_BENCHMARK/,/content-type:/d
' %{_sysconfdir}/config.php

%triggerpostun -- eventum < 1.4-2.174
cp -f %{_sysconfdir}/apache.conf{,.rpmsave}
# loosely fix htdocs directory
sed -i -e '
s,%{_appdir},%{_appdir}/htdocs,
' %{_sysconfdir}/apache.conf

%triggerpostun mail-download -- eventum-mail-download < 1.4-2.20050222.2.200
sed -i -e 's,%{_appdir}/misc,%{_appdir},' /etc/cron.d/eventum-mail-download
touch /etc/cron.d/eventum-mail-download

%triggerpostun mail-queue -- eventum-mail-queue < 1.4-2.20050222.2.200
sed -i -e 's,%{_appdir}/misc,%{_appdir},' /etc/cron.d/eventum-mail-queue
touch /etc/cron.d/eventum-mail-queue

%triggerpostun monitor -- eventum-monitor < 1.4-2.20050222.2.200
sed -i -e 's,%{_appdir}/misc,%{_appdir},' /etc/cron.d/eventum-monitor
touch /etc/cron.d/eventum-monitor

%triggerpostun reminder -- eventum-reminder < 1.4-2.20050222.2.200
sed -i -e 's,%{_appdir}/misc,%{_appdir},' /etc/cron.d/eventum-reminder
touch /etc/cron.d/eventum-reminder

%files
%defattr(644,root,root,755)
%doc ChangeLog FAQ INSTALL README UPGRADE
%doc misc/upgrade docs/* rpc/xmlrpc_client.php setup/schema.sql 
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/apache.conf
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/config.php
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/private_key.php
%attr(660,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/setup.php
%attr(640,root,http) %config %verify(not mtime) %{_sysconfdir}/core.php

%dir %attr(731,root,http) /var/log/%{name}
%attr(620,root,http) %ghost /var/log/%{name}/*

%dir %{_appdir}/htdocs
%{_appdir}/htdocs/*.php
%{_appdir}/htdocs/css
%{_appdir}/htdocs/customer
%{_appdir}/htdocs/images
%{_appdir}/htdocs/js
%{_appdir}/htdocs/manage
%{_appdir}/htdocs/reports
%{_appdir}/htdocs/rpc
%{_appdir}/htdocs/misc

%{_appdir}/templates

%{_smartyplugindir}/*
%if %{without pear}
%{_appdir}/include/pear
%endif

%dir %{_appdir}/include
%{_appdir}/include/customer
%{_appdir}/include/jpgraph
%{_appdir}/include/workflow
%{_appdir}/include/class.[^m]*.php
%{_appdir}/include/class.mail.php
%{_appdir}/include/class.mail_queue.php
%{_appdir}/include/class.mime_helper.php
%{_appdir}/include/class.misc.php
%{_appdir}/include/db_access.php
%{_appdir}/include/jsrsServer.inc.php

%dir %attr(730,root,http) /var/run/%{name}
%dir %attr(730,root,http) /var/cache/%{name}

%files base
%defattr(644,root,root,755)
%attr(751,root,root) %dir %{_sysconfdir}
%dir %{_libdir}
%dir %{_appdir}

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

%files irc
%defattr(644,root,root,755)
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/irc.php
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/eventum-irc
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
