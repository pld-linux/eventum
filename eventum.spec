# TODO
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
Release:	0.5
License:	GPL
Group:		Applications/WWW
Source0:	http://mysql.wildyou.net/Downloads/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	361c1355e46a6bbfa54e420964ec92cf
URL:		http://dev.mysql.com/downloads/other/eventum/index.html
BuildRequires:	sed >= 4.0
Requires:	php >= 4.1.0
Conflicts:	php >= 5.0.0
Requires:	php-pcre
Requires:	php-mysql
Requires:	php-gd
Requires:	php-imap
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	%{_datadir}/%{name}

%description
Eventum is a user-friendly and flexible issue tracking system that can
be used by a support department to track incoming technical support
requests, or by a software development team to quickly organize tasks
and bugs. Eventum is used by the MySQL AB Technical Support team, and
has allowed us to dramatically improve our response times.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_htmldir}/locks

# TODO: php4
sed -i -e 's,/usr/local/bin/php,/usr/bin/php,' misc/cli/eventum

cp -a . $RPM_BUILD_ROOT%{_htmldir}

> $RPM_BUILD_ROOT%{_htmldir}/setup.conf.php

# in doc
rm -f $RPM_BUILD_ROOT%{_htmldir}/{COPYING,ChangeLog,FAQ,INSTALL,README,UPGRADE}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog FAQ INSTALL README UPGRADE
%dir %{_htmldir}
%attr(640,http,root) %config(noreplace) %{_htmldir}/config.inc.php
%attr(640,http,root) %config(noreplace) %{_htmldir}/setup.conf.php
%{_htmldir}/*[!cf].php

%{_htmldir}/css
%{_htmldir}/customer
%{_htmldir}/docs
%{_htmldir}/images
%{_htmldir}/js
%{_htmldir}/manage
%{_htmldir}/misc
%{_htmldir}/reports
%{_htmldir}/rpc
%{_htmldir}/setup
%{_htmldir}/templates

%dir %attr(755,http,root) %{_htmldir}/locks

%dir %{_htmldir}/include
%{_htmldir}/include/customer
%{_htmldir}/include/jpgraph
%{_htmldir}/include/pear
%{_htmldir}/include/Smarty
%{_htmldir}/include/workflow
%{_htmldir}/include/class.*
%{_htmldir}/include/db_access.php
%{_htmldir}/include/jsrsServer.inc.php
%attr(640,http,root) %{_htmldir}/include/private_key.php

%dir %attr(755,http,root) %{_htmldir}/logs
%attr(640,http,root) %{_htmldir}/logs/*

%dir %attr(750,http,root) %{_htmldir}/templates_c
