#!/usr/bin/env python 

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
    'Referer':'https://tp.m-team.cc/',
    'Connection':'keep-alive',
    'Cache-Control':'max-age=0'
    }
t_url = 'https://tp.m-team.cc/torrents.php'
s_url = ''
f = open('mt.cookie','r')
headers['Cookie'] = f.read().strip()
f.close()

s = requests.Session()
s.headers.update(headers)

conn = sqlite3.connect('test.db')
conn.text_factory = str

def showtop():
    site = 'MT'
    r = s.get(t_url)
    soup =  BeautifulSoup(r.content, "lxml")
    fulltable = soup.find("table",{"class" : "torrents"})
    cur = conn.cursor()
    #mt_torrents = []
    for row in fulltable.find_all("tr",class_=['sticky_top','sticky_normal'],recursive=False):
        torrent_other = row.find_all("td",{"class":"rowfollow"})
        size = torrent_other[3].text
        up_time = torrent_other[2].span['title']
        upltime = int(time.mktime(time.strptime(up_time,"%Y-%m-%d %H:%M:%S")))
        torrent_table = row.find("table",{"class":"torrentname"})
        torrent_img = torrent_table.find("td",{"class":"torrentimg"}).a.find("img")['src']
        torrent_fix = torrent_table.find("td",{"class":"embedded"})
       	t_title = torrent_fix.a['title']
       	try:
       	    name = torrent_fix.find('br').nextSibling
       	except:
       	    name = ''
       	site_id = re.search(r'\d+(?=&)', torrent_fix.a['href'] ).group()

        t_link = "https://tp.m-team.cc/details.php?id=" + site_id + "&hit=1"
        d_link = "https://tp.m-team.cc/download.php?id=" +site_id + "&passkey=" + "mypasskey" + "&https=1"

        cur.execute("INSERT INTO PTTOP (SITE,TITLE,NAME,SITE_ID,SIZE,T_LINK,D_LINK,UPLTIME ) VALUES (?,?,?,?,?,?,?,?) " ,  (site,t_title,name,site_id,size,t_link,d_link,upltime))
        conn.commit()
        #per_torrent = ['MT',t_title,name,id,size,upltime]
        #mt_torrents.extend([per_torrent])
    #return mt_torrents

if __name__ == '__main__':
    showtop()

