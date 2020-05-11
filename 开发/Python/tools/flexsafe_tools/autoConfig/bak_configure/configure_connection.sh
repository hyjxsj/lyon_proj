#!/usr/bin/env bash
echo "开始配置本地服务器"
echo "HOST:$1"
echo "PASSWD:$2"

if [[ ! -f /root/.ssh/config ]]; then
	echo "拷贝.ssh目录至/root/"
	cp -r ./.ssh /root/
	echo "[Done]"
fi

#install sshpass
echo "安装 sshpass"
rm -fr /var/lib/dpkg/lock
dpkg -i ./sshpass_1.05-1_amd64.deb
echo "安装 sshpass 完成"

echo "[执行ssh-copy-id命令]"
sshpass -p $2 ssh-copy-id -i /root/.ssh/id_rsa.pub cfbackup@$1 -f
echo "[完成]"

