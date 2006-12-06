#!/bin/sh
# $Id$

case "$1" in
emails|emails\ *)
	TYPE="emails"
	ARG="${1#* }"
	;;
drafts|notes)
	TYPE="$1"
;;
*)
	echo >&2 "Invalid type: $1"
	exit 78
esac


exec /usr/share/eventum/route_$TYPE.php $ARG
