import time
import hmac
import hashlib
import requests
import json
from coincheck.utils import make_header
import simplejson as json

"""
document: https://coincheck.jp/documents/exchange/api
"""
class Account(object):
    
    def __init__(self,
                 access_key=None,
                 secret_key=None):
        self.access_key = access_key
        self.secret_key = secret_key

    def get_info(self):
        ''' show user information
        '''

        url= 'https://coincheck.jp/api/accounts'
        headers = make_header(url,
                              access_key = self.access_key,
                              secret_key = self.secret_key)

        r = requests.get(url,
                         headers = headers)
        return json.loads(r.text)
    
    def get_balance(self):
        ''' confirm balance
        '''
        url = 'https://coincheck.jp/api/accounts/balance'
        headers = make_header(url,
                              access_key = self.access_key,
                              secret_key = self.secret_key)
        r = requests.get(url,
                         headers = headers)
        return json.loads(r.text)
    
if __name__ == '__main__':
    pass
    #a = Account(access_key=settings.access_key, secret_key=settings.secret_key)
    #print(a.get_balance())
    #b = Account(access_key=settings.access_key, secret_key=settings.secret_key)
    #print(b.get_balance())
