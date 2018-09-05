# -*- coding: utf-8 -*-
"""
Created on Tue Aug 07 14:46:56 2018

@author: finere
"""
import os  
import sys
import cx_Oracle
import pymssql
reload(sys)
sys.setdefaultencoding('utf8')
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
oracle_conn = cx_Oracle.connect('admin/admin@localhost:1521/orcl')
mssql_conn = pymssql.connect(server="admin",port="3723",user="sa",password="admin",database="Cash",charset="utf8")
#oracle2mssql
mysql_cur = mysql_conn.cursor()

mysql_cur.execute("select Id,FlowDateTime,Mall_Enter,Mall_Exit,UpdateTime from T_Mall_Flow where To_DAYS(UpdateTime)=TO_DAYS(now())")
resultmysql = mysql_cur.fetchall()
mssql_cur = mssql_conn.cursor()
for row in resultmysql:
    if row[0]==0:
       mssql_conn.commit()
       oracle_conn.close()
       mssql_conn.close()
       mysql_conn.close() 
    else:
        mssql_cur.execute("insert into [Cash].[dbo].[T_Mall_Flow] ( Id,FlowDateTime,Mall_Enter,Mall_Exit,UpdateTime ) values(%s,%s,%s,%s,%s)",(row))
        #print "%s,%s,%s,%s,%s"%(row)
    #print row[0].decode('utf8'),row[1].decode('utf8'),row[2].decode('utf8')
mssql_conn.commit()
oracle_conn.close()
mssql_conn.close()
