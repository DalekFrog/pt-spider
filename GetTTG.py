#!/usr/bin/env python 
#-*- coding: UTF-8 -*- 

from bs4 import BeautifulSoup
import re
import requests
import time
import sqlite3

headers = {
    'Accept-Encoding':'gzip, deflate, sdch, br',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cache-Control':'max-age=0',
    'Referer':'https://totheglory.im/',
    'Connection':'keep-alive'
    }
t_url = 'https://totheglory.im/browse.php?c=M'
s_url = ''
f = open('ttg.cookie','r')
headers['Cookie'] = f.read().strip()
f.close()

s = requests.Session()
s.headers.update(headers)

conn = sqlite3.connect('test.db')
conn.text_factory = str

def showtop():
    site = 'TTG'
    r = s.get(t_url)
    soup =  BeautifulSoup(r.content, "lxml")
    fulltable =  soup.find("table",{"id" : "torrent_table"})
    cur = conn.cursor()
    for row in fulltable.find_all("tr",class_=["hover_hr  sticky","hover_hr"],recursive=False):
        site_id = row["id"]
        up_time = row.find_all("td",{"align":"center"})[1].text
        upltime = int(time.mktime(time.strptime(up_time,"%Y-%m-%d%H:%M:%S")))
        size = row.find_all("td",{"align":"center"})[3].text
        torrent_fix = str(row.find("td",{"align":"left"}).find("div").a.b)
        title = re.split('<|>',torrent_fix)[2] #原盘DIY制作者@字符使用了邮件保护js，直接舍弃处理
        try:
            name = re.sub(r'</?\w+[^>]*>','',torrent_fix.split('<br/>')[1]).strip()
        except:
            name = ''

        t_link = "https://totheglory.im/t/" + site_id + "/"
        d_link = "https://totheglory.im/dl/"+ site_id + "/passkey"
        cur.execute("INSERT INTO PTTOP (SITE,TITLE,NAME,SITE_ID,SIZE,T_LINK,D_LINK,UPLTIME ) VALUES (?,?,?,?,?,?,?,?) " ,  (site,title,name,site_id,size,t_link,d_link,upltime))
        conn.commit()

if __name__ == '__main__':
    showtop()
    conn.close()
