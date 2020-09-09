#!/bin/bash
###############################################
# Date: 2020-8-10                             #
# Auth: Lukas                                 #
# Mail: yangyang.huang@cloudfortdata.com      #
# Func: log frame
# Ver.: 1.0                                   #
###############################################

LOG_DIR="/var/log"


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

