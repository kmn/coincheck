import requests
import ast

"""
document: https://coincheck.com/documents/exchange/api
"""

base_url = "https://coincheck.com"
api_urls = { 'ticker'     : '/api/ticker',
             'trades'     : '/api/trades',
             'order_books': '/api/order_books'
             }

class Market(object):
    def __init__(self):
        pass


    def public_api(self,url,offset=0):
        ''' template function of public api'''
        params = {}
        if(offset>0):
            params = {'offset':offset}
            if(offset>99):
                offset=99
        try :
            url in api_urls
            return ast.literal_eval(requests.get(base_url + api_urls.get(url),params=params).text)
        except Exception as e:
            print(e)

    def ticker(self):
        '''get latest information of coincheck market'''
        return self.public_api('ticker')

    def trades(self,offset = 0):
        '''get latest deal history of coincheck market'''
        return self.public_api('trades',offset)

    def orderbooks(self):
        '''get latest asks/bids information of coincheck market'''
        return self.public_api('order_books')


if __name__ == '__main__':
    pass
