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
oracle_cur = oracle_conn.cursor()

oracle_cur.execute("select TRANSSTORE,TRADEDATE,TTLORGAMOUNT,POSTTIME from possalestotal t where trunc(TRADEDATE)=trunc(sysdate) ")
resultoracle = oracle_cur.fetchall()
mssql_cur = mssql_conn.cursor()
for row in resultoracle:
    if row[0].strip() =='':
       mssql_conn.commit()
       oracle_conn.close()
       mssql_conn.close()
       mysql_conn.close() 
    else:
        mssql_cur.execute("insert into [Cash].[dbo].[possalestotal] ( TRANSSTORE,TRADEDATE,TTLORGAMOUNT,POSTTIME ) values(%s,%s,%s,%s)",(row))
mssql_conn.commit()
oracle_conn.close()
mssql_conn.close()
