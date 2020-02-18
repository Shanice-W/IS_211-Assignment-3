#!/usr/bin/env python
# coding: utf-8

# In[2]:


import argparse
import urllib2
import csv
import re


# In[3]:


def downloadData(url):
    csvData=urllib2.urlopen(url)
    return csvData


# In[141]:


def processData(data):
    total_hits += 0
    imagehits += 0
    browsers = {'Firefox':0,
                'Google Chrome':0,
                'Internet Explorer':0,
                'Safari':0}
                
    for row in csv.reader(data):
        if re.search(r'\.(jpg|jpeg|gif|png)$', row [0], re.IGNORECASE):
            imagehits +=1
            total_hits +=1
        if re.search("Firefox", row [2]):
            browsers['Firefox'] +=1
        if re.search("Google Chrome", row [2]):
            browsers['Google Chrome'] +=1
        elif re.search("MSIE", row [2]):
            browsers['Internet Explorer'] +=1
        elif re.search("Safari", row [2]):
            browsers['Safari'] += 1
        

image_percent = (float(imagehits) / total_hits) * 100
top_browser = max(b for b in browsers.items())

print "The browser results are: {}".format(browsers)
print 'Image requests account for {}% of all requests. The most popular browser was {}.'.format(
image_percent, top_browser)


# In[7]:


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', help="Enter URL Link to CSV File")
    args = parser.parse_args()

    if args.url:
        try:
            inf = downloadData(args.url)
            processData(inf)
        except urllib2.URLError as url_err:
            print ('URL is INVALID')
            raise url_err
    else:
        print ('Please enter a valid URL.')

