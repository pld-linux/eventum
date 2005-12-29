#!/bin/sh

scriptdir="$1"
if [ ! -d "$scriptdir" ]; then
	echo >&2 "Missing scriptdir: $scriptdir"
	exit 1
fi

echo >&2 "Running eventum upgrade scripts in $scriptdir"

upgrade_script() {
	script="$1"; shift

	echo -n "Eventum upgrade: $@..."
	if ! php $scriptdir/$script; then
		echo >&2 ""
		echo >&2 "Please run manually: php $scriptdir/$script"
		echo >&2 "NOTE: You might need to add CREATE, DROP, ALTER and INDEX privileges to Eventum MySQL user for this to work".
	fi
	echo ""
}

while read script text; do
	upgrade_script $script "$text"
done
