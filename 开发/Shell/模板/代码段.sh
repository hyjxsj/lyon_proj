#!/usr/bin/env


#color config
rmsg() { echo -e "\e[1;31m$*\e[0m"; } #输出红色
gmsg() { echo -e "\e[1;32m$*\e[0m"; } #输出绿色
bmsg() { echo -e "\033[34;49m$*\033[0m"; } #输出蓝色

#current path
WD="$(cd `dirname $0`; pwd)"

#root 
user=`whoami`
if [[ X$user != Xroot ]];then
  echo -e "\E[1;31m Please execute this script under the root user!         \n \E[0m"
  exit 1
fi