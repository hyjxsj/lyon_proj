"""
@version: python3.6
@author: ‘steinven‘
@license: Apache Licence
@contact: steinven@qq.com
@software: PyCharm
@file: demo.py
@time: 2019/10/9 14:28
"""
import os
import sys

from urllib3.exceptions import InsecureRequestWarning

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import requests
from loguru import logger

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from flexsafe_utils.SSHConnection import SSHConnection
from flexsafe_utils.common import get_flexsafe_version, flexsafe_login, ssh_login, check_jetty, parse_ip

print('''
功能：

    1.自动配置https
    
注意：

    1.仅限用于发布版及镜像


''')
input_ip = input('请输入FlexSafe Server IP：172.16.')
host = parse_ip(input_ip)
logger.info("服务器IP:【%s】" % host)
if ':' not in host:
    host = '172.16.' + input_ip + ':8080'
flexsafe_version = get_flexsafe_version(host)
authorization = flexsafe_login(host)[0]
http_port = input('设置http端口（默认8080）：')
https_port = input('设置https端口（默认443）：')

if http_port == '':
    http_port = '8080'
if https_port == '':
    https_port = '443'
part1 = ''
part2 = ''
if ':' not in input_ip:
    part1 = input_ip.split('.')[0]
    part2 = input_ip.split('.')[1]
else:
    part1 = input_ip.split(':')[0].split('.')[0]
    part2 = input_ip.split(':')[0].split('.')[1]
domain = 's%ss%s.cloudfort.ml' % (part1, part2)
if authorization == None:
    logger.error("获取认证失败，请检查Flexsafe服务是否正常！")
    sys.exit(1)

current_dir = os.path.dirname(os.path.abspath(__file__))
header = {
    "Connection": "keep-alive",
    "Authorization": authorization,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
}


def upload_https():
    logger.info('正在上传https文件...')
    file = 'cloudfort.ml.zip'
    files = {'file': (file, open(os.path.join(current_dir, file), 'rb'), 'application/x-zip-compressed')}
    upload_url = 'http://%s/api/v1/https/config' % host
    r = requests.post(url=upload_url, files=files, headers=header, timeout=300, verify=False)
    if r.status_code == 204:
        logger.info('上传https文件成功')
    else:
        logger.error('上传https文件失败！')


def set_port():
    logger.info('正在开启https功能...')
    header.update({"Authorization": authorization})
    base_url = 'http://{host}/api/v1/globalConfig/%5B%7B%22name%22:%22global.system.network.protocol' \
               '%22,%22value%22:%22https%22%7D,%7B%22name%22:%22global.system.intranet.ip%22,%22' \
               'value%22:%22{intranet_ip}%22%7D,%7B%22name%22:%22global.system.extranet.ip%22,%22' \
               'value%22:%22%22%7D,%7B%22name%22:%22global.system.domain.name%22,%22' \
               'value%22:%22{domain_name}%22%7D,%7B%22name%22:%22global.system.domain.https.port%22,%22' \
               'value%22:%22{https_port}%22%7D,%7B%22name%22:%22global.system.domain.http.port%22,%22value%22:%22{http_port}%22%7D,' \
               '%7B%22name%22:%22global.system.intranet.port%22,%22value%22:%22{intranet_port}%22%7D,%7B%22name%22:%22global.system.extranet' \
               '.port%22,%22value%22:%22{extranet_port}%22%7D%5D?mailToUser=false'.format(
        host=host, intranet_ip=host.split(':')[0], domain_name=domain, http_port=http_port, https_port=https_port,
        intranet_port=http_port, extranet_port=http_port)
    put_data = {}

    try:
        r = requests.put(url=base_url, headers=header, json=put_data)
        logger.debug(r.text)
    except:
        pass


def restart_jetty():
    ssh_account = ssh_login(host)
    ssh_name = ssh_account[0]
    ssh_passwd = ssh_account[1]
    try:
        ssh = SSHConnection(host, 22, ssh_name, ssh_passwd)
    except:
        logger.error('ssh登录失败')
        sys.exit(1)
    if ssh_name != 'root':
        ls = 'sudo ls /etc/init.d/ | grep jetty'
        jetty_v = ssh.exec_command(ls, ssh_passwd).decode('utf-8').split('\r\n')[2]
        logger.info("-----正在重启Jetty....-----")
        logger.debug('jetty_v:' + jetty_v)
        ssh.exec_command('sudo service %s restart' % jetty_v, ssh_passwd)
    else:
        try:
            ssh.exec_command('service jettydr restart', ssh_passwd)
            ssh.exec_command('service jettyd restart', ssh_passwd)
        except:
            logger.error('重启Jetty失败，请手动重启！')
    logger.warning("-----所有操作完成，请等待Jetty重启完成-----")


def test_connection():
    https_url = 'https://' + domain + ':' + https_port
    http_url = 'http://' + domain + ':' + http_port
    logger.info("检查http连通性...")
    check_jetty(http_url, 100)
    logger.info("检查https连通性...")
    check_jetty(https_url, 100)


if __name__ == '__main__':
    upload_https()
    set_port()
    restart_jetty()
    test_connection()
