import requests

"""
document: https://coincheck.jp/documents/exchange/api
"""

base_url = "https://coincheck.jp"
api_urls = { 'ticker'     : '/api/ticker',
             'trades'     : '/api/trades',
             'order_books': '/api/order_books'
             }

class Market(object):
    def __init__(self):
        pass


    def public_api(self,url):
        ''' template function of public api'''
        try :
            url in api_urls
            return requests.get(base_url + api_urls.get(url)).text
        except Exception as e:
            print(e)
    
    def ticker(self):
        '''get latest information of coincheck market'''
        return self.public_api('ticker') 
    
    def trades(self):
        '''get latest deal history of coincheck market'''
        return self.public_api('trades') 
    
    def orderbooks(self):
        '''get latest asks/bids information of coincheck market'''
        return self.public_api('order_books') 


if __name__ == '__main__':
    pass
    m1 = Market()
    print('ticker: ' + m1.ticker())
    print('trades: ' + m1.trades())
    print('order_books: ' + m1.orderbooks())
