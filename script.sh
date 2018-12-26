#!/bin/bash
cd /Sites/option_chain
source /Sites/env/bin/activate
python optionchain.py
DATE=`date +%Y-%m-%d%H-%m`
ls -ltr /Sites/option_chain/NIFTY |awk '{if (NR!=1){print $9}}'> /Sites/option_chain/niftyoptionlist.txt
COMMIT_MSG="Commit on "$DATE
git add	.
git commit -m "$COMMIT_MSG"
git push -u origin master
