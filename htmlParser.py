# -*- coding: utf-8 -*-
"""
Created on Mon May 18 11:14:49 2020

@author: Daniel
"""

from bs4 import BeautifulSoup
import re
import pandas as pd
import sys

googleData = open("./DC_Raw_SearchData.html", encoding='utf8')

print('Loading HTML')

soup = BeautifulSoup(googleData, "html.parser")

text = soup.get_text()

textSplit = text.split("Searched for")

textSplit = textSplit[1:]

Month = {
        'Jan':1,
        'Feb':2,
        'Mar':3,
        'Apr':4,
        'May':5,
        'Jun':6,
        'Jul':7,
        'Aug':8,
        'Sep':9,
        'Oct':10,
        'Nov':11,
        'Dec':12
        }

searchTerm = []
searchMonth = []
searchDay = []
searchYear = []

count = 0

print('Starting')

for x in textSplit:
    try:
        tempSplit = x.split(",")
        
        if len(tempSplit)==1:
            continue
        
        #print(tempSplit)
        searchTerm_Date = re.findall('[a-zA-Z][^0-9A-Z]*', tempSplit[0])[0]
        
        #print(searchTerm_Date)
        
        day = re.findall(r'(\w+?)(\d+)', tempSplit[0])[0][1].split(" ")[0]
        #print(day)
        
        month = re.findall('[a-zA-Z][^A-Z]*', tempSplit[0])[1].split(" ")[0]
        #print(month)
        
        year = re.findall('[a-zA-Z][^A-Z]*', tempSplit[0])[1].split(" ")[1]
        #print(year)
        
        if isinstance(int(day), int)&isinstance(Month[month], int)&isinstance(int(year), int):
            searchTerm.append(searchTerm_Date)
            searchDay.append(int(day))
            searchMonth.append(Month[month])
            searchYear.append(int(year))
        
        
    except Exception:
        continue
    
    count += 1
    
    print('Row: ' + str(count))
    sys.stdout.flush()
    
    
searchDict = {
        'searchTerm':searchTerm,
        'searchDay':searchDay,
        'searchMonth':searchMonth,
        'searchYear':searchYear
        }

searchDF = pd.DataFrame(searchDict)

searchDF.to_csv(path_or_buf = 'D_searchData.csv',index=False)
