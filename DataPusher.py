# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 11:08:22 2018

@author: Assembly
"""


import requests

url = 'https://api.powerbi.com/beta/8bf2e8dc-0738-49a0-9278-f0c7c067a1ca/datasets/4f715521-b88b-41e1-9c73-de1f659a10e8/rows?key=1WkBIDZKZyCTWvYBOzoe%2BAG8f0dMlLdZpVl8olsfDHbmihMIJmmzBQMea22bDH%2BQqpmkR9wUoVCgy7X2%2BAOtQg%3D%3D'
data = '''[
{
"item" :50,
"val" :-20.8
}
]'''
response = requests.post(url, data=data)
print(response)







