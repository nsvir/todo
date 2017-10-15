#!/usr/bin/env sh

junks='*.png *.log *.pyc *.xml *.html *.pyc __pycache__'
BASEDIR=${0%/*}
cd $BASEDIR

installDB() {
    sqlite3 "$BASEDIR"/src/db/todo.db < "$BASEDIR"/src/db/create.sql
}

case $1 in
    clean)
	for junk in $junks
	do find "$BASEDIR" -name "$junk" -exec rm -rfv {} 2>/dev/null \;
	done;;
    acceptance*)
	[ ! $(which chromedriver) ] \
	    && echo "You need to install chromedriver" \
	    && exit
	python -m robot "$BASEDIR/$1";;
    test*)
	nosetests "$BASEDIR"/$1;;
    help)
	echo "$0 clean acceptance test run"
	;;
    run | *)
	[ ! -f "$BASEDIR"/src/db/todo.db ] && installDB
	python "$BASEDIR"/src/main.py;;
esac
