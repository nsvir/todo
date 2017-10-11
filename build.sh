#!/usr/bin/env sh

junks='*.png *.log *.pyc *.xml *.pyc __pycache__'

case $1 in
    clean)
	for junk in $junks
	do find -name "$junk" -exec rm -rfv {} 2>/dev/null \;
	done;;
    acceptance)
	python -m robot acceptance;;
    test)
	nosetests --with-coverage \
	       --cover-erase --cover-branches \
	       --with-doctest test;;
    run)
	python ./src/main.py;;
    *)
	echo "$0 clean acceptance test run"
	;;
esac
