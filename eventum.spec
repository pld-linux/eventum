# TODO
# - php5 is not tested, but not placing hard conflict on it, as it prevents php4 & php coinstallation
# - discard bundled packages (from INSTALL):
#  - JpGraph 1.5.3 (last GPL version)
#  - Smarty 2.3.0 (http://smarty.php.net)
#  - PEAR packages
#  - dTree 2.0.5 (http://www.destroydrop.com/javascript/tree/)
#  - dynCalendar.js (http://www.phpguru.org/dyncalendar.html)
#  - overLIB 3.5.1 (http://www.bosrup.com/web/overlib/)
#  - A few other small javascript libraries
# - Mail Queue Process, cron or separate package (misc/process_mail_queue.php)
# - Email Download (misc/download_emails.php)
# - Reminder System (misc/check_reminders.php)
# - Heartbeat Monitor (misc/monitor.php)
# - Email Routing Script (misc/route_emails.php)
# - Note Routing Script (misc/route_notes.php)
# - IRC Notification Bot (misc/irc/bot.php)
# - Command-line Interface (misc/cli/eventum)
Summary:	Eventum Issue / Bug Tracking System
Name:		eventum
Version:	1.4
Release:	0.8
License:	GPL
Group:		Applications/WWW
Source0:	http://mysql.wildyou.net/Downloads/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	361c1355e46a6bbfa54e420964ec92cf
Patch0:		%{name}-clock-status.patch
URL:		http://dev.mysql.com/downloads/other/eventum/index.html
BuildRequires:	sed >= 4.0
Requires:	php >= 4.1.0
Requires:	php-pcre
Requires:	php-mysql
Requires:	php-gd
Requires:	php-imap
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/%{name}

%description
Eventum is a user-friendly and flexible issue tracking system that can
be used by a support department to track incoming technical support
requests, or by a software development team to quickly organize tasks
and bugs. Eventum is used by the MySQL AB Technical Support team, and
has allowed us to dramatically improve our response times.

%prep
%setup -q
%patch0 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_appdir}/locks

# TODO: php4
sed -i -e 's,/usr/local/bin/php,/usr/bin/php,' misc/cli/eventum

cp -a . $RPM_BUILD_ROOT%{_appdir}

> $RPM_BUILD_ROOT%{_appdir}/setup.conf.php

# in doc
rm -f $RPM_BUILD_ROOT%{_appdir}/{COPYING,ChangeLog,FAQ,INSTALL,README,UPGRADE}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog FAQ INSTALL README UPGRADE
%dir %{_appdir}
%attr(640,http,root) %config(noreplace) %{_appdir}/config.inc.php
%attr(640,http,root) %config(noreplace) %{_appdir}/setup.conf.php
%{_appdir}/*[!cf].php

%{_appdir}/css
%{_appdir}/customer
%{_appdir}/docs
%{_appdir}/images
%{_appdir}/js
%{_appdir}/manage
%{_appdir}/misc
%{_appdir}/reports
%{_appdir}/rpc
%{_appdir}/setup
%{_appdir}/templates

%dir %attr(755,http,root) %{_appdir}/locks

%dir %{_appdir}/include
%{_appdir}/include/customer
%{_appdir}/include/jpgraph
%{_appdir}/include/pear
%{_appdir}/include/Smarty
%{_appdir}/include/workflow
%{_appdir}/include/class.*
%{_appdir}/include/db_access.php
%{_appdir}/include/jsrsServer.inc.php
%attr(640,http,root) %{_appdir}/include/private_key.php

%dir %attr(755,http,root) %{_appdir}/logs
%attr(640,http,root) %{_appdir}/logs/*

%dir %attr(750,http,root) %{_appdir}/templates_c
