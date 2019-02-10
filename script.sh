#!/bin/bash
cd /Sites/option_chain
source /Sites/env/bin/activate
python optionchain.py
DATE=`date +%Y-%m-%d_%H-%m`
for i in $(cat /Sites/option_chain/lists/stlist.txt);
do 
   j=$(echo "$i" | awk '{print tolower($0)}');
   ls -ltr /Sites/option_chain/$i |awk '{if (NR!=1){print $9}}'>/Sites/option_chain/lists/$j.txt; 
done
python create_analysis.py
python SendMail.py 
COMMIT_MSG="Commit on "$DATE
git add	.
git commit -m "$COMMIT_MSG"
git push -u origin master
