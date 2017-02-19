#!/usr/bin/python
#-*- coding: UTF-8 -*- 

import sqlite3


conn = sqlite3.connect('test.db')
conn.text_factory = str
print("Opened database successfully")

conn.execute('''CREATE TABLE PTTOP
       (ID integer PRIMARY KEY autoincrement,
	SITE	TEXT	NOT NULL,
	TITLE	TEXT	NOT NULL,
        NAME    TEXT,
	SITE_ID INT	NOT NULL,
        SIZE    CHAR(50)     NOT NULL,
	T_LINK	TEXT	NOT NULL,
	D_LINK	TEXT	NOT NULL,
	UPLTIME	INT	NOT NULL);''')
print("Table created successfully")


#site = 'TTG123'
#title = 'Doctor Strange 2016 720p BluRay x264-SPARKS'
#name = "MBC月火剧 逆贼：偷百姓的盗贼 역적：백성을 훔친 도적 尹均相 蔡秀彬 李荷妮主演"
#site_id = 324020
#size = '5.46GB'
#t_link = 'dfasdfsdfsd'
#d_link = 'dsidgfldfasdfsdfsd'
#upltime = 1487234639
#
#value = {
#    "site" : "TTG",
#    "title" : "Doctor Strange 2016 720p BluRay x264-SPARKS",
#    "name" : "MBC月火剧 逆贼：偷百姓的盗贼 역적：백성을 훔친 도적 尹均相 蔡秀彬 李荷妮主演",
#    "site_id" : 324020,
#    "size" : "5.46GB",
#    "t_link" : "dfasdfsdfsd",
#    "d_link" : "dsidgfldfasdfsdfsd",
#    "upltime" : 1487234639
#    }
#cur = conn.cursor()

#cur.execute("INSERT INTO PTTOP (SITE,TITLE,NAME,SITE_ID,SIZE,T_LINK,D_LINK,UPLTIME ) VALUES (?,?,?,?,?,?,?,?) ",(site,title,name,site_id,size,t_link,d_link,upltime));

#cur.execute("INSERT INTO PTTOP (SITE,TITLE,NAME,SITE_ID,SIZE,T_LINK,D_LINK,UPLTIME ) VALUES (?,?,?,?,?,?,?,?) " ,  (site,title,name,site_id,size,t_link,d_link,upltime))
#sql = "INSERT INTO PTTOP VALUES(%(site)s, %(title)s, %(name)s, %(site_id)s, %(size)s, %(t_link)s, %(d_link)s, %(upltime)s)"
#conn.execute("INSERT INTO PTTOP (SITE,TITLE,NAME,SITE_ID,SIZE,T_LINK,D_LINK,UPLTIME ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) " \
#conn.execute(sql,value)
conn.commit()
conn.close()
