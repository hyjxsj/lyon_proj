背景：
实现两台服务器之间的文件同步，使用rsync

注意：
一、需要开放root登录，使用root用户执行rsync（因为安享文件权限的问题，无法使用cfservice用户rsync到没有权限的目录）
开放root步骤如下，
步骤1：使用sudo passwd root命令设置root的密码

步骤2：修改/etc/ssh/sshd_config文件
1.把PermitRootLogin Prohibit-password 添加#注释掉
2.新添加：PermitRootLogin yes
3.重启ssh服务/etc/init.d/ssh restart

二、打开两台服务器之间免密登录
场景，A主机往主机B传文件，
1、在主机A上创建公钥和私钥(全部默认)
ssh-keygen -t rsa
2、把A主机的公钥id_rsa.pub文件copy到B主机的root用户家目录下的.ssh目录下，并改名为authorized_keys