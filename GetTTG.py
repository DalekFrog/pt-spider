#!/usr/bin/env python 

from bs4 import BeautifulSoup
import re
import requests


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


def showtop():
    r = requests.get(t_url)
    soup =  BeautifulSoup(r.content, "lxml")
    fulltable =  soup.find("table",{"id" : "torrent_table"})
    ttg_torrents = []
    for row in fulltable.find_all("tr",class_=["hover_hr  sticky","hover_hr"],recursive=False):
        id = row["id"]
        size = row.find_all("td",{"align":"center"})[3].text
        torrent_fix = str(row.find("td",{"align":"left"}).find("div").a.b).split('<br/>')   #.find("br").next_sibling
        title = re.sub(r'</?\w+[^>]*>','',torrent_fix[0])
        try:
            name = re.sub(r'</?\w+[^>]*>','',torrent_fix[1]).strip()
        except:
            name = ''
    
        torrent = ['TTG',title,name,id,size]
        ttg_torrents.extend([torrent])
    return ttg_torrents

if __name__ == '__main__':
    print showtop()
