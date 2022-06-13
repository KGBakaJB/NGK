# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 21:19:50 2022

@author: Кирилл
"""
import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.trekkingclub.ru/zyvalinka/index.php')

soup = BeautifulSoup(r.content, 'lxml')

find = soup.find('b').find_next().text
list_str = []

for i in find.split('\n\n\n\n'):
    if len(i) != 0:
        list_str.append(i)
list_str = list_str[4:]   
list_str[-1] = list_str[-1].split('\n\n')[0]  
print(list_str[0])

input()