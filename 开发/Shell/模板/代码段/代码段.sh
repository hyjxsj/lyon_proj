#!/bin/bash
###############################################
# Date: 2020-8-10                             #
# Auth: Lukas                                 #
# Mail: yangyang.huang@cloudfortdata.com      #
# Func: deploy sstap service & frp            #
# Ver.: 1.0                                   #
###############################################


#color config
rmsg() { echo -e "\e[1;31m$*\e[0m"; } #输出红色
gmsg() { echo -e "\e[1;32m$*\e[0m"; } #输出绿色
bmsg() { echo -e "\033[34;49m$*\033[0m"; } #输出蓝色

#current path
WD="$(cd `dirname $0`; pwd)"

#root check
#方式一
ROOT_UID="0"
[ $ROOT_UID != "$UID" ] && { echo "Must be root to run this script.";exit 1; }
#方式二
user=`whoami`
if [[ X$user != Xroot ]];then
  echo -e "\E[1;31m Please execute this script under the root user!         \n \E[0m"
  exit 1
fi


