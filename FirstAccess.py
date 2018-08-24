# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 08:08:44 2018

@author: Assembly
"""

import pandas as pd
import oandapyV20
from oandapyV20 import API
import oandapyV20.endpoints.accounts as accounts

accountIDs = [ '101-001-5729740-0'+i for i in ['05','06','07','08','11','12'] ]
access_token = '10205fa114f1778b74e3949320bcb275-b8fea4f40cc338ae9d44bd54f3154843'
client = API(access_token=access_token)

total = 0
for i in accountIDs:
    r = accounts.AccountDetails(accountID=i)
    res = client.request(r)
    total += float(res['account']['NAV'])
print(total)


