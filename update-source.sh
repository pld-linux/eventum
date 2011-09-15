#!/bin/sh
set -e
dropin=

# Work in package dir
dir=$(dirname "$0")
cd "$dir"

if [ "$1" ]; then
	rev=$1
	echo "Using $rev..."
fi

specfile=eventum.spec

oldrev=$(awk '/^%define[	 ]+subver[	 ]+/{print $NF}' $specfile)
if [ "$oldrev" != "$ver" ]; then
	echo "Updating $specfile for $rev"
	sed -i -e "
		s/^\(%define[ \t]\+subver[ \t]\+\)[0-9]\+\$/\1$rev/
	" $specfile
	../builder -ncs -5 $specfile
else
	echo "Already up to date"
fi
