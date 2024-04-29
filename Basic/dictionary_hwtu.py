# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 15:09:44 2024

@author: maece
"""

keys = ['a','b','c','d','e']
valores=[5,4,3,2,1]
dic={}
for i in range(5):
    dic[keys[i]]=valores[i];

    

print(dic)
print(dic['b']);
dic.get('b')


val2=list(dic.keys())
val3=list(dic.values())
