#!/usr/bin/env sh

junks='*.png *.log *.pyc *.xml *.html *.pyc __pycache__'

case $1 in
    clean)
	for junk in $junks
	do find -name "$junk" -exec rm -rfv {} 2>/dev/null \;
	done;;
    acceptance)
	[ ! $(which geckodriver) ] \
	    && echo "geckodriver must be installed and in \$PATH\nhttps://github.com/mozilla/geckodriver/releases" \
	    && exit
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
