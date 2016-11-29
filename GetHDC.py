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
#print s.headers


def showtop():
    r = requests.get(t_url)
    soup =  BeautifulSoup(r.content, "lxml")
    #print r.content
    fulltable = soup.find("table",{"class" : "torrent_list"})
    hdc_torrents = []
    for row in fulltable.find_all("tr",class_=["stickz_bg","sticky_bg"],recursive=False):
        torrent_fix = row.find("td",{"class":"t_name"}).find("tr").find_all("td")[1]
        torrent_misc = torrent_fix.h3.a
        title = torrent_misc['title']
        id = re.search(r'\d+(?=&)',torrent_misc['href']).group()
        try:
            name = torrent_fix.h4.text
        except:
            name = ''
        size = row.find("td",{"class":"t_size"}).text
        torrent = ['HDC',title,name,id,size]
        hdc_torrents.extend([torrent])
    return hdc_torrents

if __name__ == '__main__':
    print showtop()
