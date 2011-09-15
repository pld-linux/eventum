#!/bin/sh
set -e
dropin=
specfile=eventum.spec

# Work in package dir
dir=$(dirname "$0")
cd "$dir"

if [ -f "$1" ]; then
	rev=$1
	rev=${rev#eventum-*-r}
	rev=${rev%.tar.gz}
	echo "Using $rev..."

elif [ "$1" ]; then
	rev=$1
	echo "Using $rev..."
fi

oldrev=$(awk '/^%define[	 ]+subver[	 ]+/{print $NF}' $specfile)
if [ "$oldrev" != "$rev" ]; then
	echo "Updating $specfile for $rev"
	sed -i -e "
		s/^\(%define[ \t]\+subver[ \t]\+\)[0-9]\+\$/\1$rev/
	" $specfile
	../builder -ncs -5 $specfile
else
	echo "Already up to date"
fi
