#!/bin/bash
# @Time: 2020/9/14                         
# Auth: Lukas                                 
# Mail: yangyang.huang@cloudfortdata.com      
# Func: des for script
# Ver.: 1.0                                   


#while循环
#while1
ls -d */ | while read directory
do
  cd  $directory
done

#while2
i=1
while(($i < 100))
do
  i=$(($i + 1))
done

