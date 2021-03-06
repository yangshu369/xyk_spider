#coding:utf-8
__author__ = 'ys'
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import thread
import json


from crawler.EciticCrawler import *
from crawler.SpdbCrawler import *
from crawler.AgriculturalCrawler import *
from crawler.CibCrawler import *
from crawler.CgbCrawler import *
from model.XykSpider import *
import traceback


db = XykSpider()
#中信银行
ecitic = EciticCrawler()
ecitic.request(ecitic.url)
list = ecitic.get();
for item in list:
    if db.check(ecitic.bank_id, item['name'], item['url']):
        continue
    db.add(ecitic.bank_id, item['name'], item['date'], item['url'], item['beginDate'], item['endDate'])

#浦发银行
spdb = SpdbCrawler()
for url in spdb.urlList:
    spdb.request(url, False)
    list = spdb.get()
    for item in list:
        if db.check(spdb.bank_id, item['name'], item['url']):
            continue
        db.add(spdb.bank_id, item['name'], item['date'], item['url'], item['beginDate'], item['endDate'])

#农业银行
agricu = AgriculturalCrawler()
for url in agricu.urlList:
    list = agricu.request(url, False)
    list = agricu.get()
    for item in list:
        if db.check(agricu.bank_id, item['name'], item['url']):
            continue
        db.add(agricu.bank_id, item['name'], item['date'], item['url'], item['beginDate'], item['endDate'])

#兴业银行
cib = CibCrawler()
for url in cib.urlList:
     cib.request(url)
     list = cib.get()
     for item in list:
        if db.check(cib.bank_id, item['name'], item['url']):
            continue
        db.add(cib.bank_id, item['name'], item['date'], item['url'], item['beginDate'], item['endDate'])

#广发银行
cgb = CgbCrawler()
for url in cgb.urlList:
    cgb.request(url, False)
    list = cgb.get()
    for item in list:
        if db.check(cgb.bank_id, item['name'], item['url']):
            continue
        db.add(cgb.bank_id, item['name'], item['date'], item['url'], item['beginDate'], item['endDate'])

