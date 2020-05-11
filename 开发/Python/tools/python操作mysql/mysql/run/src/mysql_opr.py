#-*- coding=utf-8 -*-
_Auth_ = "yangyang.huang"

import sys,os
from ..core import logger
from ..config import config
from ..data import sql
from ..core import mysql_conn

def mysql_opr():
    m1 = mysql_conn.Mysql(config.host, config.user, config.password, config.database, config.port, config.charset)
    results = m1.sql_opr(sql.sql_selectSystem)
    print(results)

    if results[0][0] == "1.9.5beta":
        m2 = mysql_conn.Mysql(config.host, config.user, config.password, config.database, config.port, config.charset)
        m2.sql_opr(sql.sql_updateSystem)
'''
    for row in results:
        """
        results存放的是所有数据库记录，每一条记录是一个tuple、所有记录存放在一个大的tuple
        """
        name = row[0]
        value = row[1]
        comment = row[2]
        print("----->name:%s;======value:%s;====comment:%s" % (name,value,comment))
'''
def log():
    # path = os.path.abspath(os.path.dirname(__file__))
    # type = sys.getfilesystemencoding()
    sys.stdout = logger.Logger(config.log_filename)
    # print(path)




