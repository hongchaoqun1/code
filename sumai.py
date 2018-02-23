# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 11:34:46 2018

@author: hong
"""

from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
import pandas as pd
import re
import time
from selenium.webdriver.common.keys import Keys

p_name=[]
def get_name(soup):
    lists=[]
    pro_name=soup.find_all('a',{'class':'product'})
    for i in pro_name:
        x=i.text
        if x:
            lists.append(x)
        else:
            lists.append("none")
    return lists
            
p_url=[]
def get_url(soup):
    lists=[]
    pro_url=soup.find_all('a',{"class":"product"})
    for i in pro_url:
        x=i.attrs['href']
        if x:
            x='https:'+x
            lists.append(x)
        else:
            lists.append('none')      
    return lists
   
p_orders=[]         
def get_orders(soup):
    lists=[]
    orders=soup.find_all('em',{'title':'Total Orders'})
    for i in orders:
        x=i.text
        y=re.findall("\d+",x)
        z=y[0]
        if z:
            lists.append(z)
        else:
            lists.append('none')      
    return lists

p_price=[]
def get_price(soup):
    lists=[]
    orders=soup.find_all('span',{'itemprop':'price'})
    for i in orders:
        x=i.text
        if x:
            lists.append(x)
        else:
            lists.append('none')      
    return lists
#price=soup.find_all('span',{'class':'value'})

p_score=[]
def get_score(soup):
    lists=[]
    orders=soup.find_all('img',{'class':'score-icon'})
    for i in orders:
        x=i.attrs['src']
        y=re.findall(r"https.*?icon/(.*?)-s.gif",x)
        if y:
            lists.append(y[0])
        else:
            lists.append('none')      
    return lists
#score=soup.find_all('img',{'class':'score-icon'})

back_num=[]
def get_back_num(soup):
    lists=[]
    orders=soup.find_all('div',{'class':'rate-history'})
    for i in orders:
        b=i.find("a",{"class":'rate-num'})
        if b:
            x=b.text
            y=re.findall(r"\d+",x)
            lists.append(y[0])
        else:
            lists.append('none')      
    return lists
#back_num=soup.find_all('a',{'class':'rate-num'})

p_store_name=[]
def get_store_name(soup):
    lists=[]
    orders=soup.find_all('a',{'class':'store'})
    for i in orders:
        x=i.text
        if x:
            lists.append(x)
        else:
            lists.append('none')      
    return lists
#store=soup.find_all('a',{'class':'store'})

#driver.get("https://www.aliexpress.com/category/40602/blankets/2.html?site=glo&g=y&needQuery=n&tag=")

#html=driver.page_source
#soup=BeautifulSoup(html)
#print(driver.title)
#driver.quit()

def spider(i):
    no=repr(i)
    driver=webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'])
    driver.set_window_size(2000, 1500)
    driver.get("https://www.aliexpress.com/category/40602/blankets/"+no+".html?site=glo&g=y&needQuery=n&tag=")
    html=driver.page_source
    driver.close()
    return html

num=4
for i in range(96):
    if num%7==0:
        print("休息一下吧！")
        time.sleep(100)
        
    num=num+1
    print("这是第"+str(num)+"页，开始爬")
    page=spider(num)
    soup=BeautifulSoup(page)

    p_name=get_name(soup)
    p_url=get_url(soup)
    p_orders=get_orders(soup)
    p_price=get_price(soup)
    p_score=get_score(soup)
    back_num=get_back_num(soup)
    p_store_name=get_store_name(soup)
    
    print('开始插入数据')

    dic={"p_name":p_name,"p_url":p_url,"p_orders":p_orders,"p_price":p_price,"p_score":p_score,"back_num":back_num,"p_store_name":p_store_name}
    output=pd.DataFrame(dic)
    
    output.to_csv("s"+repr(num)+".csv")
    print('写入完成...,\n')
    time.sleep(7)