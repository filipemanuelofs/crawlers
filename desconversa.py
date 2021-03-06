# coding: utf-8

"""
Author: 
Filipe Manuel

Description: 
This crawler was made to download every pdf file 
from WordPress website http://www.desconversa.com.br 
for didactic purposes.
The files will be downloaded in current directory which
"desconversa.py" is in.

Version:
0.1 (and need a lot of adjustments)
"""

import os
import urllib2
import requests
from bs4 import BeautifulSoup as bs

_YEAR = '2013/'

_MONTH = ['01/', '02/', '03/',
          '04/', '05/', '06/',
          '07/', '08/', '09/',
          '10/']

_SUBJECT = ['matematica/', 'portugues/', 
            'geografia/', 'historia/',
            'biologia/', 'redacao/',
            'quimica/', 'fisica/'] 

_CONTEXT = 'wp-content/uploads/' + _YEAR

_URL = []
for subject_ in _SUBJECT:
    for month_ in _MONTH:
        _URL.append('http://www.desconversa.com.br/' + subject_ + _CONTEXT + month_)

# Limiting URL_ to one link using slice [2:3].
# Catch every url took too much time
# and this is for didactic purposes.
for url_ in _URL[2:3]:
    r = requests.get(url_)
    soup = bs(r.text)

urls_ = []
names_ = []
for i, link in enumerate(soup.findAll('a')):
    _FULLURL = url_ + link.get('href')
    if _FULLURL.endswith('.pdf'):
        urls_.append(_FULLURL)
        names_.append(soup.select('a')[i].attrs['href'])

urls_names = zip(names_, urls_)

print 'Starting...'
for title, url in urls_names:
    print 'Downloading now...', title
    rqst = urllib2.Request(url)
    resp = urllib2.urlopen(rqst)
    pdf = open(title, 'w+')
    pdf.write(resp.read())
    pdf.close()
print 'The end.'
