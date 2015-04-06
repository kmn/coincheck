import time
import hmac
import hashlib
import requests
import settings
import json
from utils import make_header

"""
document: https://coincheck.jp/documents/exchange/api
"""

def get_info():
    ''' show user information
    '''
    url= 'https://coincheck.jp/api/accounts'
    headers = make_header(url)
    r = requests.get(url,headers=headers)
    return r.text

def get_balance():
    ''' confirm balance
    '''
    url = 'https://coincheck.jp/api/accounts/balance'
    headers = make_header(url)
    r = requests.get(url,headers=headers)
    return r.text

if __name__ == '__main__':
    pass
    #print(get_info())
    #print(get_balance())
