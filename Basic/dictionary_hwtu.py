# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 15:09:44 2024

@author: maece
"""

keys = ['a','b','c','d','e']
dic={}
for i in range(5):
    dic[keys[i]]=i;
    
print(dic)
print(dic['b']);
dic.get('b')