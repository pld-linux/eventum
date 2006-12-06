#!/bin/sh
# $Id$
#

# qmail exit codes
HARD=100
SOFT=111
OK=0

case "$1" in
drafts|emails|notes)
	TYPE="$1"
	shift
;;
*)
	echo >&2 "Invalid type: $1"
	exit $SOFT
esac

/usr/share/eventum/route_$TYPE.php "$@" && exit $OK
rc=$?

# exit codes are for postfix, based on /usr/include/sysexits.h
#define EX_NOINPUT      66      /* cannot open input */
#define EX_DATAERR      65      /* data format error */
#define EX_NOPERM       77      /* permission denied */
#define EX_CONFIG       78      /* configuration error */

# all known exit codes (from source) are hard errors
case $rc in
78|77|65|66)
	rc=$HARD
	;;
*)
	rc=$SOFT
	;;
esac
exit $rc
