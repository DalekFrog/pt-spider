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
    'authority':'hdchina.club',
    'referer':'https://hdchina.club/'
    }
t_url = 'https://hdchina.club/torrents.php'
s_url = ''
f = open('hdc.cookie','r')
headers['Cookie'] = f.read().strip()
f.close()

s = requests.Session()
s.headers.update(headers)

conn = sqlite3.connect('test.db')
conn.text_factory = str

def showtop():
    site = 'HDC'
    r = s.get(t_url)
    soup =  BeautifulSoup(r.content, "lxml")
    fulltable = soup.find("table",{"class" : "torrent_list"})
    #hdc_torrents = []
    cur = conn.cursor()
    for row in fulltable.find_all("tr",class_=["stickz_bg","sticky_bg"],recursive=False):
        torrent_fix = row.find("td",{"class":"t_name"}).find("tr").find_all("td")[1]
        torrent_misc = torrent_fix.h3.a
        title = torrent_misc['title']
        site_id = re.search(r'\d+(?=&)',torrent_misc['href']).group()
        up_time = row.find("td",{"class":"t_time"}).span['title']
        upltime = int(time.mktime(time.strptime(up_time,"%Y-%m-%d %H:%M:%S")))
        try:
            name = torrent_fix.h4.text
        except:
            name = ''
        size = row.find("td",{"class":"t_size"}).text
        #torrent = ['HDC',title,name,site_id,size,upltime]
        t_link = "https://hdchina.club/details.php?id=" + site_id + "&hit=1"
        d_link = "https://hdchina.club/download.php?id="+ site_id + "&passkey=" + "my-passkey"

        cur.execute("INSERT INTO PTTOP (SITE,TITLE,NAME,SITE_ID,SIZE,T_LINK,D_LINK,UPLTIME ) VALUES (?,?,?,?,?,?,?,?) " ,  (site,title,name,site_id,size,t_link,d_link,upltime))
        conn.commit()
        #print(torrent)
        #hdc_torrents.extend([torrent])
    #return hdc_torrents

if __name__ == '__main__':
    #print(showtop())
    showtop()
    conn.close()
