from coincheck import order,market
import settings
from nose.tools import *
import os,sys
import time

market_info = market.Market().ticker()


def test_buy_btc_jpy():
    '''
    buy BTC
    '''
    time.sleep(1)
    buy_value = market_info.get('ask') / 2
    o1 = order.Order(access_key=settings.access_key, secret_key=settings.secret_key)
    ok_(o1.buy_btc_jpy(amount=0.01,rate= buy_value).get('success'))

def test_sell_btc_jpy():
    '''
    sell BTC
    '''
    time.sleep(1)
    sell_value = 2 * market_info.get('bid') 
    o1 = order.Order(access_key=settings.access_key, secret_key=settings.secret_key)
    ok_(o1.sell_btc_jpy(amount = 0.01, rate = sell_value).get('success'))

def test_list():
    '''
    list all open orders
    '''
    o1 = order.Order(access_key=settings.access_key, secret_key=settings.secret_key)
    ok_(o1.list().get('success'))

def test_cancel():
    '''
    cancel all orders
    '''
    order_list = order.Order(access_key=settings.access_key, secret_key=settings.secret_key).list().get('orders')
    for i in order_list:
        o1 = order.Order(access_key=settings.access_key, secret_key=settings.secret_key)
        ok_(o1.cancel(str(i.get('id'))).get('success') )

def test_history():
    ''' 
    show payment history
    '''
    o1 = order.Order(access_key=settings.access_key, secret_key=settings.secret_key)
    ok_(o1.history().get('success'))

if __name__ == '__main__':
    #print(test_buy_btc_jpy())
    #print(market_info.get('ask')/2)
    #print(test_list())
    print(test_cancel())
    #print(test_history())
