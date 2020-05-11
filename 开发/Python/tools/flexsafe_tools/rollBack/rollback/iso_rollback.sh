#!/usr/bin/env bash
#rollback iso 1.9.5alpha
#Auth:      lyon
#email:     yangyang.huang@cloudfortdata.com
#date:      2019-3-14

#start or not
[ "root" != "`whoami`" ] && { echo -e "\e[1;31m Please run under root! \e[0m"; exit 1; }

#variable define
GREEN_COLOR="\e[1;32m"
RED_COLOR="\e[1;31m"
RES="\e[0m"
#path
WD="$(cd `dirname $0`;pwd)"
log_path="${WD}/logs"
license_path="/usr/lib/jni"
volume_path="/flexsafe/data/volume"
log_file=${log_path}/rollback.log

[ ! -d ${log_path} ] && mkdir -p "${log_path}" || echo "logs already exist."

start_stop_service(){
  
  #start or stop service
  case "$1" in 
    start)
      service jettydr start
      service apache2 start
      ;;
    stop)
      service jettydr stop
      service apache2 stop
      ;;
    *)
      echo -e "${RED_COLOR} Usage:start_stop_service [start/stop] ${RES}"
      ;;
  esac
  
}

clean_up(){
  #clean up database
  mysql -uroot -pcloudfort -e "drop database flexsafe; drop database boxsafe;" && echo -e "${GREEN_COLOR} Database clean up success.${RES}" \
  || echo -e "${RED_COLOR} Database clean up failed! ${RES}"

  #delete volume
  chattr -R -i ${volume_path}/*
  rm -rf ${volume_path}/*
  rm -rf /boxsafe/data/*
  rm -rf /var/www/boxsafe/config/config.php
  #add
  cd ${volume_path}
  mklost+found
  
  #delete license config
  #rm -rf ${license_path}/{KeyReg,license}
}

brush(){
  cd ${WD}
  #brush database
  #brush boxsafe
  mysql -uroot -pcloudfort < ./mysqlsetup.txt && echo -e "${GREEN_COLOR} Database boxsafe brush success.${RES}" || echo -e "${RED_COLOR} Database boxsafe brush failed! ${RES}"
  #brush flexsafe
  mysql -uroot -pcloudfort < ./flexsafe.sql && echo -e "${GREEN_COLOR} Database flexsafe brush success.${RES}" || echo -e "${RED_COLOR} Database flexsafe brush failed! ${RES}"
  
  #brush config
  cp ${WD}/flexsafe.conf /etc/flexsafe.conf
}

main(){
echo -e "${GREEN_COLOR} -----------------------------------Rollback begin----------------------------------- ${RES}"
  #stop service
  #start_stop_service stop
  
  #clean
  clean_up
  
  #brush database
  brush
  
  #start service
  #start_stop_service start
echo -e "${GREEN_COLOR} -----------------------------------Rollback end----------------------------------- ${RES}"
}

main "$@"