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

# snapshot: DATE
#define _snap 20050114

%if 0%{?_snap}
%define _source http://downloads.mysql.com/snapshots/%{name}/%{name}-nightly-%{_snap}.tar.gz
%else
%define _source http://mysql.wildyou.net/Downloads/%{name}/%{name}-%{version}.tar.gz
%endif

%define _rel 1.32

Summary:	Eventum Issue / Bug Tracking System
Name:		eventum
Version:	1.4
Release:	%{?_snap:0.%{_snap}.}%{_rel}
License:	GPL
Group:		Applications/WWW
Source0:	%{_source}
# Source0-md5:	361c1355e46a6bbfa54e420964ec92cf
Source1:	%{name}-apache.conf
Patch0:		%{name}-rpm.patch
Patch1:		%{name}-clock-status.patch
URL:		http://dev.mysql.com/downloads/other/eventum/index.html
BuildRequires:	sed >= 4.0
BuildRequires:	rpmbuild(macros) >= 1.177
Requires:	php >= 4.1.0
Requires:	php-pcre
Requires:	php-mysql
Requires:	php-gd
Requires:	php-imap
#Requires:	apache-mod_dir
# conflict with non-confdir apache
Conflicts:	apache1 < 1.3.33-1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/%{name}
%define		_appdir	%{_datadir}/%{name}

%define		_apache1dir	/etc/apache
%define		_apache2dir	/etc/httpd

%description
Eventum is a user-friendly and flexible issue tracking system that can
be used by a support department to track incoming technical support
requests, or by a software development team to quickly organize tasks
and bugs. Eventum is used by the MySQL AB Technical Support team, and
has allowed us to dramatically improve our response times.

%package setup
Summary:	Eventum setup package.
Group:		Applications/WWW
PreReq:		%{name}
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description setup
Install this package to configure initial Eventum installation. You
should uninstall this package when you're done, as it considered
insecure to keep the setup files in place.

%prep
%setup -q %{?_snap:-n %{name}-%{_snap}}
%patch0 -p1
%patch1 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_appdir}/{locks,templates_c}}

cp -a . $RPM_BUILD_ROOT%{_appdir}

> $RPM_BUILD_ROOT%{_appdir}/setup.conf.php

sed -i -e 's,/usr/local/bin/php,/usr/bin/php4,' $RPM_BUILD_ROOT%{_appdir}/misc/cli/eventum

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/apache.conf

# in doc
rm -f $RPM_BUILD_ROOT%{_appdir}/{COPYING,ChangeLog,FAQ,INSTALL,README,UPGRADE}
rm -rf $RPM_BUILD_ROOT%{_appdir}/misc/upgrade

%clean
rm -rf $RPM_BUILD_ROOT

%post
# apache1
if [ -f %{_apache1dir}/apache.conf ]; then
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
if grep -q 'header("Location: setup/")' %{_appdir}/config.inc.php; then
%banner %{name} -e <<EOF

You haven't yet configured Eventum!

Install %{name}-setup and open up http://yourserver/eventum/
-- that will help you setup initial config.

when have configured Eventum, please uninstall the setup package,
so that %{name}-setup is able to secure your Eventum installation.

EOF
#' vim stupidity.
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
		rm -f %{_apache1dir}/httpd.conf/99_%{name}.conf
		if [ -f /var/lock/subsys/httpd ]; then
			/etc/rc.d/init.d/httpd restart 1>&2
		fi
	fi
fi

%post setup
# RACE possible? chmod just in case
chmod 640 %{_appdir}/{config.inc,setup.conf}.php
chown http:root %{_appdir}/{config.inc,setup.conf}.php

%postun setup
if [ "$1" = "0" ]; then
	# RACE condition possible?
	chmod 640 %{_appdir}/{config.inc,setup.conf}.php
	chown root:http %{_appdir}/{config.inc,setup.conf}.php
fi

%files
%defattr(644,root,root,755)
%doc ChangeLog FAQ INSTALL README UPGRADE misc/upgrade
%dir %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/apache.conf

%dir %{_appdir}
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_appdir}/config.inc.php
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_appdir}/setup.conf.php
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
%{_appdir}/templates

%dir %attr(750,http,root) %{_appdir}/locks

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

%dir %attr(731,root,http) %{_appdir}/logs
%attr(640,http,root) %config(noreplace) %verify(not md5 mtime size) %{_appdir}/logs/*

%dir %attr(750,http,root) %{_appdir}/templates_c

%files setup
%defattr(644,root,root,755)
%{_appdir}/setup
