#!/usr/bin/env bash
############################################################
# Date:    2020/6/16
# Author:  huangyangyang
# Email:   yangyang.huang@cloudfortdata.com  
# Description:  flexsafe rsync 
############################################################

log_path="/var/log/flexsafe-rsync"
[ ! -d /var/log/flexsafe-rsync ] && mkdir -p /var/log/flexsafe-rsync

#log
exec 1>$log_path/rsync-"`date \"+%F %T\"`".log 2>&1
#msg
msg() { echo "$*"; } #
rmsg() { echo -e "\e[1;31m$*\e[0m"; } #red
gmsg() { echo -e "\e[1;32m$*\e[0m"; } #green
bmsg() { echo -e "\033[34;49m$*\033[0m"; } #blue

echo -n "Rsync start：" && date "+%F %T"
#run user
user=`whoami`
if [[ X$user != Xroot ]];then
  msg "Please execute this script under the root user!"
  exit 1
fi

#config
remote_host="172.16.71.137"
flexsafe_rsync_user="null"


#check
setup(){
  ping $remote_host -c 10 || { msg "$remote_host cannot connect！"; exit 1; }
}

#rsync 
rsync_flexsafe(){
  input="$1"
  case $input in 
    sys)
      msg "SYS Rsync..."
      #base
      /usr/bin/rsync -avpz --delete /flexsafe/data/volume/ root@$remote_host:/flexsafe/data/volume/

      /usr/bin/rsync -avpz --delete /boxsafe/data/ root@$remote_host:/boxsafe/data/

      /usr/bin/rsync -avpz --delete /cloudfort/ root@$remote_host:/cloudfort/

      /usr/bin/rsync -avpz --delete /flexsafe_userdata root@$remote_host:/flexsafe_userdata
      
      #extend    
      ;;
    user)
      msg "USER $flexsafe_rsync_user Rsync..."
      #rsync only user data
      if [ -d /flexsafe/data/volume/${flexsafe_rsync_user:?"rsync user not defined"} ];then
        /usr/bin/rsync -avpz --delete /flexsafe/data/volume/$flexsafe_rsync_user/ root@$remote_host:/flexsafe/data/volume/$flexsafe_rsync_user/
      else
        msg "/flexsafe/data/volume/$flexsafe_rsync_user，No such file or directory" && exit 1
      fi
      ;;
  esac
}

#restart service & cleanup
teardown(){
  ssh root@$remote_host "service mysql stop; service mysql start"
}

main(){
  setup
  
  input="$1"
  case ${input:-sys} in
    sys)
      rsync_flexsafe "sys"
      teardown
      ;;
    user)
      rsync_flexsafe "user"
      ;;
  esac
  
}

#parameters to extend
main $@

echo -n "Rsync end：" && date "+%F %T"