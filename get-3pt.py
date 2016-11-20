#!/usr/bin/env python 

import requests
import urllib2

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36',
    'Cookie' : 'tp=OGNmNTdkYjQ0NGNmMzhhNWVjYTM3ZTgxZDFiZjczNGI2NzBjZDMzNw%3D%3D'
    }

url = 'https://tp.m-team.cc/adult.php'
r1 = requests.get(url,headers=headers)
r2 = urllib2.Request(url,headers=headers)

html1 = r1.content
html2 = html = urllib2.urlopen(r2).read()

print "html1:\n"
print html1,"\n\n"
print "html2:\n"
print html2
