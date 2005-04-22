#!/bin/sh

scriptdir="$1"
if [ ! -d "$scriptdir" ]; then
	echo >&2 "Missing scriptdir: $scriptdir"
	exit 1
fi

cat >&2 <<-EOF
Running eventum upgrade scripts to in $scriptdir
These will fail if your eventum user doesn't have ALTER privilege to database.

!!! Proceeding in 10 seconds !!!
EOF

sleep 10s
if [ -x /usr/bin/php4 ]; then
	php=/usr/bin/php4
else
	php=/usr/bin/php
fi

upgrade_script() {
	script="$1"; shift

	echo -n "Eventum upgrade: $@..."
	if ! $php -q $scriptdir/$script; then
		echo >&2 ""
		echo >&2 "Please run manually: $php -q $scriptdir/$script"
	fi
	echo ""
}

while read script text; do
	upgrade_script $script "$text"
done
