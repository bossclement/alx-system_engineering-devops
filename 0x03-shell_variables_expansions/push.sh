#!/bin/bash
comment="New commit"

# check if task file exists
if [ -f "$1" ];
then
	# change the file to executable.
	chmod u+x $1

	# append the interpreter to the file
	sed -i '1s/^/#!\/bin\/bash\n/' $1
	

	# check if the comment was provided and use it.
	if [ "$2" != "" ];
	then
		comment=$2
	fi

	# push the file to git
	git add .
	git commit -m "$comment"
	git push
fi
