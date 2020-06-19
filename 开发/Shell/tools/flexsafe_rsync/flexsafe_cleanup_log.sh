#!/usr/bin/env bash
############################################################
# Date:    2020/6/19
# Author:  huangyangyang
# Email:   yangyang.huang@cloudfortdata.com  
# Description:  flexsafe rsync 
############################################################

log_paths="/var/log/flexsafe-rsync "
for (( i=0;i<${#log_paths[@]};i++ ))
do
  echo "${log_paths[i]} clear log."
  find ${log_paths[i]} -mtime -1 -name "*.log" -exec rm -rf {} \;
done
