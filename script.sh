#!/bin/bash
cd /Sites/option_chain
source /Sites/env/bin/activate
python optionchain.py
DATE=`date +%Y-%m-%d_%H-%m`
ls -ltr /Sites/option_chain/NIFTY |awk '{if (NR!=1){print $9}}'> /Sites/option_chain/lists/nifty.txt
ls -ltr /Sites/option_chain/PVR/ | awk '{if (NR!=1){print $9}}'>/Sites/option_chain/lists/pvr.txt
ls -ltr /Sites/option_chain/TECHM/ | awk '{if (NR!=1){print $9}}'> /Sites/option_chain/lists/techm.txt
ls -ltr /Sites/option_chain/ESCORTS/ | awk '{if (NR!=1){print $9}}'> /Sites/option_chain/lists/escorts.txt
ls -ltr /Sites/option_chain/GRASIM/ | awk '{if (NR!=1){print $9}}'> /Sites/option_chain/lists/grasim.txt
ls -ltr /Sites/option_chain/KOTAKBANK/ | awk '{if (NR!=1){print $9}}'> /Sites/option_chain/lists/kotakbank.txt
ls -ltr /Sites/option_chain/L\&TFH/ | awk '{if (NR!=1){print $9}}'> /Sites/option_chain/lists/l\&tfh.txt
ls -ltr /Sites/option_chain/YESBANK/ | awk '{if (NR!=1){print $9}}'>/Sites/option_chain/lists/yesbank.txt
ls -ltr /Sites/option_chain/BANKNIFTY/ | awk '{if (NR!=1){print $9}}'> /Sites/option_chain/lists/banknifty.txt
ls -ltr /Sites/option_chain/BIOCON/ | awk '{if (NR!=1){print $9}}'> /Sites/option_chain/lists/biocon.txt
ls -ltr /Sites/option_chain/HDFC/ | awk '{if (NR!=1){print $9}}'> /Sites/option_chain/lists/hdfc.txt
ls -ltr /Sites/option_chain/M\&M/ | awk '{if (NR!=1){print $9}}'> /Sites/option_chain/lists/m\&m.txt
ls -ltr /Sites/option_chain/TCS/ | awk '{if (NR!=1){print $9}}'> /Sites/option_chain/lists/tcs.txt
COMMIT_MSG="Commit on "$DATE
git add	.
git commit -m "$COMMIT_MSG"
git push -u origin master
