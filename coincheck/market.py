import requests

"""
document: https://coincheck.jp/documents/exchange/api
"""

base_url = "https://coincheck.jp"
api_urls = { 'ticker'     : '/api/ticker',
             'trades'     : '/api/trades',
             'order_books': '/api/order_books'
             }

def public_api(url):
    ''' template function of public api'''
    try :
        url in api_urls
        return requests.get(base_url + api_urls.get(url)).text
    except Exception as e:
        print(e)

def ticker():
    '''get latest information of coincheck market'''
    return public_api('ticker') 

def trades():
    '''get latest deal history of coincheck market'''
    return public_api('trades') 

def orderbooks():
    '''get latest asks/bids information of coincheck market'''
    return public_api('order_books') 


if __name__ == '__main__':
    pass
    #print('ticker: ' + ticker())
    #print('trades: ' + trades())
    #print('order_books: ' + orderbooks())
