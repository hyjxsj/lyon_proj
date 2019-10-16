import paramiko
import time
ssh = paramiko.client.SSHClient()
ssh.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
ssh.connect(hostname='172.16.71.174', username='root', password = '00123')


stdin, stdout, stderr = ssh.exec_command('/home/cfservice/pvl/pvl.sh')

for line in stdout.read().splitlines():
    print(line)
