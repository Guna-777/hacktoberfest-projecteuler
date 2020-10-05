# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 16:35:09 2020


"""


"""dict={'1','Lernen','2','Hub'}
dict={}
dict={'name','lernen'} """

dict={'name':'lernen','teaches':'programming','since':'2018'}
dict['name']='Lernen Hub'
print(dict['name'])
print(dict['teaches'])

dict['since']='2001'
del dict['since']
print(dict.get('since'))
