# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 19:51:25 2019

@author: ayush
"""

import re
#example
Nameage = '''Ayush is 23 and Yadvi is 22.
Aditi is 24 and Arjun is 24 too.'''
print Nameage
ages = re.findall(r'\d{1,3}',Nameage)
names = re.findall(r'[A-Z][a-z]*', Nameage )
ageDict = {}
x = 0
for i in names:
    ageDict[i] = ages[x]
    x += 1
    print(ageDict)

#finding a word in a string with the help of regular expression
if re.search("inform", "we need to inform him with latest information."):
    print "There is inform."    

#finding a list of matches
allinform = re.findall("inform","We need to inform him with the latest information.")
for i in allinform:
    print i
#finding words with similar patterns
str = "sat,cat,bat,dat,fat,hat,mat,pat"
allstr = re.findall("[a-z]*at",str)
for i in allstr:
    print i

#match series of range of characters
somestr = re.findall("[a-h]at",str)
for i in somestr:
    print i
#replacing
regex = re.compile("[p]at")
str = regex.sub("food",str)
print str 
#printing with spaces
randomstr = '''Keep the blue flag
flying high
abeeyy chall kuch bhi.'''

#print randomstr

regex = re.compile("\n")
randomstr = regex.sub(" ", randomstr)
print randomstr
#finding number of matches in a given string
# \d -> for numbers and \D -> for strings
random1 = " 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20"
#rint "Matches:",re.findall("\d{12}", random1)
random2 = "ayush is a good boy."
#rint "Matches:", re.findall("\D{ayush}",random2)
#---------------------------------------------------------------------------------------
#problem 
# \w [a-zA-Z0-0_]
#identifying phone numbers
phone = "412-555-1212"
if re.search("\w{3}-\w{3}-{4}", phone):
    print "It is a phone number."
#verifying an wemail address
emails = "sk@aol.com md@.com @seo.com dc@.com"
print( "EmailMatches:", len(re.findall("[\w._%+-]{},}@[\w.-]{2,20}.[A-Za-z]{2-3}",emails)))
#web scraping
#importing libraries
import urllib.request
from re import findall

url = "https://www.youtube.com/watch?v=zN8rwVXwRUE"

response = urllib.request.urlopen(url)

html = response.read()
htmlstr = html.decode()

pdata = findall("\(d{3}\) \d{3}-\d{4}", htmlstr)

for i in pdata:
    print (i)
    
    