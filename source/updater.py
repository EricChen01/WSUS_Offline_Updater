#!/usr/bin/env python3

'''
imports
'''
#beautifulsoup is a web scraping library, it allows you to easily pull elements off webpages in different forms
from bs4 import BeautifulSoup
#Parses urls and returns an object
import urllib2


#This website is NOT an official Windows Corp website, privately maintained
url = "http://download.wsusoffline.net/"
page = urllib2.urlopen(url).read()

soup = BeautifulSoup(page, 'html.parser')
#Creates a web scrapping object, imagine this as a spider named "soup" who is 
#crawling around your webpage

new = soup.find_all("a")
esr = soup.find_all("a href")

print(new)
print(esr)