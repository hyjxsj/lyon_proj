#!/bin/bash
# @Time: 2020/9/14                         
# Auth: Lukas                                 
# Mail: yangyang.huang@cloudfortdata.com      
# Func: des for script
# Ver.: 1.0                                   

#for循环
#for1
resource="a b c"
for res in $resource
do
  cd $res && bash setup.sh
done

#for2
for shname in `ls *.sh`
do
  name=`echo "$shname" | awk -F. '{print $1}'`
  echo $name
done

#for3
for (( i=1;i<10;i++))
do
  echo $i
done
