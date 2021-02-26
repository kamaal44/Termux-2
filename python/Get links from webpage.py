#!/data/data/com.termux/files/usr/bin/python3

# To get all links from a webpage:

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

req = Request("https://github.com/MrRio/jsPDF")
html_page = urlopen(req)

soup = BeautifulSoup("html_page", "lxml")

links = []
for link in soup.findAll('a'):
    links.append(link.get('href'))

print(links)
