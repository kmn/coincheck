import time
import hmac
import hashlib
import requests
import settings
from utils import make_header

"""
document: https://coincheck.jp/documents/exchange/api
"""


def create(rate, amount, order_type, pair):
    ''' create new order function
    :param rate: float
    :param amount: float
    :param order_type: str; set 'buy' or 'sell'
    :param pair: str; set 'btc_jpy' 
    '''
    nonce = str(time.time()).split('.')[0]
    key    = settings.access_key
    secret = settings.secret_key
    payload = { 'rate': rate,
                'amount': amount,
                'order_type': order_type,
                'pair': pair
                }
    url= 'https://coincheck.jp/api/exchange/orders'
    body = 'rate={rate}&amount={amount}&order_type={order_type}&pair={pair}'.format(**payload)
    message = nonce + url + body
    signature = hmac.new(secret.encode('utf-8'), message.encode('utf-8'), hashlib.sha256).hexdigest()
    headers = {
       'ACCESS-KEY'      : key,
       'ACCESS-NONCE'    : nonce,
       'ACCESS-SIGNATURE': signature
    }
    r = requests.post(url,headers=headers,data=body)
    return r.text

def buy_btc_jpy(**kwargs):
    return create(order_type='buy', pair='btc_jpy',**kwargs) 

def sell_btc_jpy(**kwargs):
    return create(order_type='sell', pair='btc_jpy',**kwargs) 

def list():
    ''' list all open orders func
    '''
    url= 'https://coincheck.jp/api/exchange/orders/opens'
    headers = make_header(url)
    r = requests.get(url,headers=headers)
    return r.text

def cancel(order_id):
    ''' cancel the specified order
    :param order_id: order_id to be canceled
    '''
    url= 'https://coincheck.jp/api/exchange/orders/' + order_id
    headers = make_header(url)
    r = requests.delete(url,headers=headers)
    return r.text

def history():
    ''' show payment history
    '''
    url= 'https://coincheck.jp/api/exchange/orders/transactions'
    headers = make_header(url)
    r = requests.get(url,headers=headers)
    return r.text

if __name__ == '__main__':
    pass
    #print(buy_btc_jpy(rate=20000, amount=0.1))
    #print(sell_btc_jpy(rate=40000,amount=0.1))
    #print(list())
    #print(history())
    #print(cancel('659546'))
