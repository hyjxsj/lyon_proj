#-*- coding=utf-8 -*-
_Auth_ = "yangyang.huang"

import pymysql as mysql

class Mysql(object):
    def __init__(self,host,user,password,database,port,charset):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.charset = charset

    def sql_opr(self,sql):
        con = mysql.connect(
            #host
            self.host,
            #user
            self.user,
            #password
            self.password,
            #database
            self.database,
            #port
            port = self.port,
            #charset
            charset = self.charset)

        cursor = con.cursor()
        try:
            cursor.execute(sql)
            con.commit()
            results = cursor.fetchall()
            if not results:
                print("Null!")
            else:
                return results
        except Exception as e:
            con.rollback()
            print("Error:{0}".format(e))
        finally:
            con.close()






