# encoding: utf-8
"""
@version: python3.6
@author: ‘steinven-office‘
@license: Apache Licence 
@contact: steinven@qq.com
@software: PyCharm
@file: SSHConnection.py
@time: 2019/4/26 17:11
"""
# coding=utf-8
import paramiko
from loguru import logger

from autoLicense import utils


class SSHConnection(object):
    def __init__(self, host, port, username, password):
        self._host = host
        if ':' in host:
            self._host = self._host.split(':')[0]
        self._port = port
        self._username = username
        self._password = password
        self._transport = None
        self._sftp = None
        self._client = None
        self._connect()

    def _connect(self):
        transport = paramiko.Transport((self._host, self._port))
        transport.auth_timeout = 5
        transport.handshake_timeout = 5
        transport.banner_timeout = 5
        transport.clear_to_send_timeout = 5
        transport.connect(username=self._username, password=self._password)
        self._transport = transport

    # 下载
    def download(self, remotepath, localpath):
        if self._sftp is None:
            self._sftp = paramiko.SFTPClient.from_transport(self._transport)
        self._sftp.get(remotepath, localpath)

    # 上传
    def put(self, localpath, remotepath):
        if self._sftp is None:
            self._sftp = paramiko.SFTPClient.from_transport(self._transport)
        self._sftp.put(localpath, remotepath)

    # 执行命令
    def exec_command(self, command, ssh_passwd):
        if self._client is None:
            self._client = paramiko.SSHClient()
            self._client._transport = self._transport
        stdin, stdout, stderr = self._client.exec_command(command, get_pty=True)
        stdin.write('%s\n' % ssh_passwd)
        stdin.flush()
        data = stdout.read()
        if len(data) > 0:
            logger.info(data.strip().decode())
            return data
        err = stderr.read()
        if len(err) > 0:
            utils.logger().debug(err.strip())
            return err

    def close(self):
        if self._transport:
            self._transport.close()
        if self._client:
            self._client.close()


if __name__ == "__main__":
    conn = SSHConnection('172.16.71.8', 22, 'cfservice', '00123')
    localpath = 'license'
    remotepath = '/home/cfservice/license'
    # print ('downlaod start')
    # conn.download(remotepath, localpath)
    # print ('download end')
    # print ('put begin')
    # jetty_v = 'sudo ls /etc/init.d/ | grep jetty'
    # conn.exec_command(jetty_v)
    # ff = conn.exec_command(jetty_v).decode('utf-8')
    # print(conn.exec_command(jetty_v).decode('utf-8').split('\r\n')[2])
    # ls = 'sudo ls /etc/init.d/ | grep jetty'
    # jetty_v = conn.exec_command(ls).decode('utf-8').split('\r\n')[2]
    #
    # c = 'sudo service %s restart ' % jetty_v
    # print(c)
    # conn.exec_command(c)
    # conn.exec_command('mysql')
    # conn.exec_command('sudo mv /home/cfservice/backup / ')

    # conn.exec_command('cd WorkSpace/Python/test;pwd')  #cd需要特别处理
    # conn.exec_command('pwd')
    # conn.exec_command('tree WorkSpace/Python/test')
    # conn.exec_command('ls -l')
    # conn.exec_command('echo "hello python" > python.txt')
    # conn.exec_command('ls hello')  #显示错误信息
    conn.close()
