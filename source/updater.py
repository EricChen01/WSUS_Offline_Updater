#!/usr/bin/env python3

'''
imports
'''
#BeautifulSoup is a web scraping library, it allows you to easily pull elements off webpages in different forms
from bs4 import BeautifulSoup
#Parses urls and returns an object
import urllib3

#This website is NOT an official Windows Corp website, privately maintained
url = "http://download.wsusoffline.net/"

#Retrieves the HTML page as an object
http = urllib3.PoolManager()
page = http.request('GET', url) #GET and POST requests are how PCs communicate 
status = page.status #provides the returned header of the page

#Imagine you have a pet spider and you called him soup. Now he is walking all up in yo webpage
soup = BeautifulSoup(page.data, 'html.parser')
new = soup.find_all('a')[8].get('href') #hardcoded index because --> The original webpage author didn't use id's --> there is malformed HTML --> selectors are more complicated to understand --> The index will not change
esr = soup.find_all('a')[11].get('href')

#Open the url files and read the stored url into memory --> Will be used to check if your local download is update to date with the remote
new_url = open('new_url.txt')
esr_url = open('esr_url.txt')
file_new = new_url.readline()
file_esr = esr_url.readline()

#If the website is down it will return a 404 "webpage not found error" or 200 "SUCCESS" if it worked correctly
if (status == 404):
    print("THE WSUS OFFLINE UPDATE WEBSITE HAS BEEN TAKEN DOWN")
else:
    if (file_new != new): #Check if the new WSUS is up to date
        print("YOU HAVE AN OUTDATED CURRENT VERSION, DOWNLOADING NEW VERSION")
        new_download = http.request('GET', new)
        temp_file = open('../download/new_download.zip', 'wb')
        temp_file.write(new_download.data)
        temp_file.close()
        new_download.release_conn()
        url_file = open('new_url.txt', 'w')
        url_file.write(new)
    if (file_esr != esr): #Check if the Extended Support Release version is update to date --> Designed for legacy systems --> Used much less than the new version
        print("YOU HAVE AN OUTDATED ESR VERSION, DOWNLOADING NEW VERSION")
        esr_download = http.request('GET', esr)
        temp_file = open('../download/esr_download.zip', 'wb')
        temp_file.write(esr_download.data)
        temp_file.close()
        esr_download.release_conn()
        url_file = open('esr_url.txt', 'w')
        url_file.write(esr)
    if(file_esr == esr and file_new == new): #You have both up to date YAY
        print("YOU HAVE AN UP-TO-DATE VERSION")

#close the file handlers to return memory space back to the Operating System
new_url.close()
esr_url.close()