#!/usr/bin/env bash

shopt -s expand_aliases
shopt expand_aliases
#alias
alias pv='/usr/share/lvm_command/pv/pv.sh /usr/share/lvm_command/pv'
alias vg='/usr/share/lvm_command/vg/vg.sh /usr/share/lvm_command/vg'
alias lv='/usr/share/lvm_command/lv/lv.sh /usr/share/lvm_command/lv'

init(){
  rmsg() { echo -e "\e[1;31m$*\e[0m"; } #red
  gmsg() { echo -e "\e[1;32m$*\e[0m"; } #green
  bmsg() { echo -e "\033[34;49m$*\033[0m"; } #blue
}

create_lvm(){
  read -p "please input device for lv,for example[sda]" dev
  read -p "please input device size,for example[100G]" size
  size_num=${size%G*}

fdisk /dev/$dev <<EOF
n
e


+$size
n
l

+$((size_num - 1))G
w
EOF

  #apt install
  apt update && apt install parted && partprobe /dev/$dev

  gmsg "--------------------------------------->partition list:"
  fdisk -l | grep -A 10 "Device.*Boot"
  gmsg "--------------------------------------->partition list end!"
  read -p "please input partition for pv,for example[sda5]" partition

  pv -c /dev/$partition && vg -c data /dev/$partition && lv -c $((size_num - 2))G volume data
}

delete_lvm(){
  gmsg "----------------------------------->delete lvm default"
  #alias
  alias pv='/usr/share/lvm_command/pv/pv.sh /usr/share/lvm_command/pv'
  alias vg='/usr/share/lvm_command/vg/vg.sh /usr/share/lvm_command/vg'
  alias lv='/usr/share/lvm_command/lv/lv.sh /usr/share/lvm_command/lv'

  shopt -s expand_aliases
  
  #delete lvm
  echo -e "y\n y\n" | lv -r volume data
  vg -r data
  read -p "Please enter the partition to delete PV,for example[sda5]" partition
  pv -r /dev/$partition
  #delete partition
  
}

main(){
  #init
  init
  [ $# -ne 1 ] && { rmsg "Usage: bash lvm.sh [create/delete]"; exit 1; }
  
  case "$@" in
    create)
      create_lvm
      ;;
    delete)
      delete_lvm
      ;;
    *)
      rmsg "invalid parameter！"
      ;;
  esac
}

main "$@"


