# -*- coding: utf-8 -*
import sys
import string
import chardet
import requests
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding("utf-8")
ipath="C:\\Users\\Administrator\\Desktop\\小学\\青年路小学.txt"
path=unicode(ipath,'utf-8')
file1=open(path)
i=0
j=0
for line in file1:
    data=line.split('*')[1]
    i=i+float(data)
    j=j+1
print i
print j
p1=i/j
print p1
print '-----------------------------------------------'
ipath1="C:\\Users\\Administrator\\Desktop\\小学\\青年路小学_around.txt"
path1=unicode(ipath1,'utf-8')
file2=open(path1)
i=0
j=0
for line1 in file2:
    data=line1.split('*')[1]
    i=i+float(data)
    j=j+1
print i
print j
p2=i/j
print p2
print (p1-p2)/p2*100