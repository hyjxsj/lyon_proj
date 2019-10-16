# encoding: utf-8
"""
@version: python3.6
@author: ‘steinven‘
@license: Apache Licence 
@contact: steinven@qq.com
@software: PyCharm
@file: toolsList.py
@time: 2019/6/19 11:24
"""
from colorama import Fore
from prettytable import PrettyTable


class Colored(object):
    #  前景色:红色  背景色:默认
    def red(self, s):
        return Fore.LIGHTRED_EX + s + Fore.RESET

    #  前景色:绿色  背景色:默认
    def green(self, s):
        return Fore.LIGHTGREEN_EX + s + Fore.RESET

    def yellow(self, s):
        return Fore.LIGHTYELLOW_EX + s + Fore.RESET

    def white(self, s):
        return Fore.LIGHTWHITE_EX + s + Fore.RESET

    def blue(self, s):
        return Fore.LIGHTBLUE_EX + s + Fore.RESET

    def cyan(self, s):
        return Fore.CYAN + s + Fore.RESET

    def magenta(self, s):
        return Fore.MAGENTA + s + Fore.RESET


c = Colored()
pt = PrettyTable()
pt.field_names = ['命令', '功能', '注意事项（测试对应功能时，请勿使用该工具！）']
pt.add_row([c.magenta('autoConfig'), c.magenta('自动配置邮箱服务器、开启加锁、专用管控、配置备份服务器'), c.magenta('用5位比特码来开启对应选项')])
pt.add_row([c.green('addFlexsafeUser'), c.green('批量新增用户、修改密码、模拟登陆'), c.green('建议不要多人同时执行此命令！')])
pt.add_row([c.magenta('generateDir'), c.magenta('创建各种权限的共享、存档目录，并在其目录内上传测试文件'), c.magenta('只会创建组相关目录，不创建普通用户目录')])
pt.add_row([c.green('pvl'), c.green('自动划分逻辑卷'), c.green('自动fdisk分区，lvm划分逻辑卷')])
pt.add_row([c.magenta('deleteBuckets'), c.magenta('批量删除阿里云、亚马逊Buckets'), c.magenta('谨慎操作，请确认列出的Buckets，再执行后续操作！')])
pt.add_row([c.green('httpsSettings'), c.green('自动配置https'), c.green('仅限用于发布版及镜像')])
pt.add_row([c.magenta('syncTime'), c.magenta('自动同步系统时间'), c.magenta('与【172.16.71.180】服务器时间保持同步')])
pt.add_row([c.green('createAuthorization'), c.green('批量生成用户authorization'), c.green('仅支持“_”分割的用户')])
pt.add_row([c.magenta('emptyFlexsafe'), c.magenta('接口方式还原FlexSafe'), c.magenta('未知风险，请勿在测试任务使用。部分数据可能一次性删除不成功')])
pt.add_row([c.green('rollBack'), c.green('操作数据库方式还原FlexSafe'), c.green('未知风险，请勿在测试任务使用')])
pt.add_row([c.magenta('smoke-api-test'), c.magenta('自动化环境检查'), c.magenta('检测环境的Licence、加锁功能、邮箱服务器')])
# pt.add_row([c.white('parseXML'),c.white('提取自动化结果中错误用例编号，用于重跑。'),c.red('请使用编译好的exe文件')])
# pt.add_row([c.white('fastUpload'),c.white('多线程上传11400个小文件,自动创建对应用户组及目录,用于性能测试数据准备'),c.red('----')])

pt.align['命令'] = "l"
pt.align['功能'] = "l"
pt.align['备注'] = "c"
pt.horizontal_char = c.cyan('-')
pt.vertical_char = c.cyan('|')
pt.junction_char = c.cyan('+')

print(pt)
