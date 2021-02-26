#!/usr/bin/python
from BeautifulSoup import BeautifulSoup
import urllib2
import re

html_page = urllib2.urlopen("http://example.com/example.html")
soup = BeautifulSoup(html_page)
for link in soup.findAll('a'):
    print link.get('href')
