from coincheck import order,market
import settings
from nose.tools import *
import os,sys
import time

market_info = market.Market().ticker()

def get_n_min_dai(minute=0,tz='UTC'):
    '''
    return :minute: before time.
    '''
    from datetime import datetime,timedelta
    from pytz import timezone
    return (datetime.now(timezone(tz)) -timedelta(minutes=minute)).strftime('%Y-%m-%dT%H:%M')[:-1]

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
    cancel orders in odered in last 10 minute.
    '''
    o1 = order.Order(access_key=settings.access_key, secret_key=settings.secret_key)
    order_id_list_to_be_canceled = [ x.get('id') for x  in o1.list().get('orders') if get_n_min_dai(10) in x.get('created_at') ]
    order_id_list_to_be_canceled += [ x.get('id') for x  in o1.list().get('orders') if get_n_min_dai(0) in x.get('created_at') ]
    if not order_id_list_to_be_canceled == []:
        [ ok_(o1.cancel(str(i)).get('success')) for i in order_id_list_to_be_canceled ]

def test_history():
    ''' 
    show payment history
    '''
    o1 = order.Order(access_key=settings.access_key, secret_key=settings.secret_key)
    ok_(o1.history().get('success'))
