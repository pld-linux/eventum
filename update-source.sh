#!/bin/sh
set -e
dropin=
repo_url=https://github.com/eventum/eventum
specfile=eventum.spec

# Work in package dir
dir=$(dirname "$0")
cd "$dir"

if [ -f "$1" ]; then
	rev=$1
	rev=${rev#eventum-*-}
	rev=${rev%.tar.gz}
elif [ "$1" ]; then
	rev=$1
else
	# use tarball from "snapshot" build
	git fetch "$repo_url" refs/tags/snapshot
	out=$(git show FETCH_HEAD -s)
	tarball=$(echo "$out" | grep -o 'eventum-.*\.tar.gz')
	url="$repo_url/releases/download/snapshot/$tarball"
	test -f "$tarball" || wget -c $url
	exec "$0" "$tarball"
fi

subver=${rev%-*}
githash=${rev#*-g}

echo "Using $rev (subver: $subver, githash: $githash)..."

oldsubver=$(awk '/^%define[\t ]+subver[\t ]+/{print $NF}' $specfile)
oldgithash=$(awk '/^%define[\t ]+githash[\t ]+/{print $NF}' $specfile)
if [ "$oldsubver" = "$subver" -a "$oldgithash" = "$githash" ]; then
	echo "Already up to date"
	exit 0
fi

echo "Updating $specfile for $rev (subver: $subver, githash: $githash)..."
sed -i -re "
	s/^[#%](define[ \t]+subver[ \t]+)[0-9]+\$/%\1$subver/
	s/^[#%](define[ \t]+githash[ \t]+)[0-9a-fg]+\$/%\1$githash/
" $specfile
../builder -ncs -5 $specfile
