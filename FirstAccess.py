# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 08:08:44 2018

@author: Assembly
"""
import time
import requests
from oandapyV20 import API
import oandapyV20.endpoints.accounts as accounts

accountIDs = [ '101-001-5729740-0'+i for i in ['05','06','07','08','11','12'] ]
access_token = '10205fa114f1778b74e3949320bcb275-b8fea4f40cc338ae9d44bd54f3154843'
client = API(access_token=access_token)
path = r'C:\Users\assembly\Desktop\PythonFolder\DataPipeline'

url = 'https://api.powerbi.com/beta/8bf2e8dc-0738-49a0-9278-f0c7c067a1ca/datasets/93557faf-50d0-41d2-87d4-cfc1cb6de921/rows?key=%2FOMBGKDciezTIrWtQPplOSprqOebnuf6DtvIG4nAnPNOgs34NjIpcCL1CTO%2By6X5cin9i%2BSlltcEw9LVClFDOA%3D%3D'

count = 0
while(True):
    total = 0
    count += 1
    NAV = []
    for i in accountIDs:
        r = accounts.AccountDetails(accountID=i)
        res = client.request(r)
        NAV.append(float(res['account']['NAV'])-1000)
        alias = res['account']['alias']
    total = sum(NAV)
    NAV = [ str(round(i,2)) for i in NAV ]
    data = '''[{{"item" :{0},"test 1" :{1},"test 2" :{2},"test 3" :{3},"test 4" :{4},"test 5" :{5},"test 6" :{6},"total" :{7}}}]'''.format(count,NAV[0],NAV[1],NAV[2],NAV[3],NAV[4],NAV[5],str(round(total,2)))
    response = requests.post(url, data=data)
    print(data,response)
    time.sleep(59.6)

#for j in range(5):
#    for i in range(1,1000):
#        data = '''[{{"item" :{0},"test 1" :{1},"test 2" :{2},"test 3" :{3},"test 4" :{4},"test 5" :{5},"test 6" :{6},"total" :{7}}}]'''.format(i,0,0,0,0,0,0,0)
#        response = requests.post(url, data=data)
#        print(i*(j+1),response)
#    time.sleep(1)

