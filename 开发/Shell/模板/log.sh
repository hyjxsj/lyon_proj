#!/bin/bash

LOG_DIR="/var/log"
ROOT_UID="0"

[ $ROOT_UID != `$UID` ] && { echo "Must be root to run this script.";exit 1; }

cd $LOG_DIR || {
  echo "Cannot change to necessary directory." >&2
  exit 1
}

cat /dev/null > messages && echo "Logs cleaned up."
exit 0

cat<<EOF
#清空日志三种办法
1.  echo " " >test.log
2.  >test.log
3.  cat /dev/null >test.log
EOF

