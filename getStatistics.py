# -*- coding: utf-8 -*-

import urllib
from bs4 import BeautifulSoup

url  = "http://web.mta.info/developers/turnstile.html"
u    = urllib.urlopen(url)
html = u.read()

soup = BeautifulSoup(html, "html.parser")
links = soup.find_all('a')

fileNumber = 0
for link in links:
	filelink = link.get('href')
	if filelink != None:
		if filelink[-8:-6] == "06":
			completeLink = "http://web.mta.info/developers/%s" % (filelink)
			#print completeLink
			nameFile = "data/file_%s.txt" % (fileNumber)
			urllib.urlretrieve(completeLink, nameFile)
			fileNumber += 1



