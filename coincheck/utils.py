import time
import hmac
import hashlib
import settings

def make_header(url,
                access_key=None,
                secret_key=None):
    ''' create request header function
    :param url: URL for the new :class:`Request` object.
    '''
    nonce = str(time.time()).split('.')[0]
    url    = url
    message = nonce + url
    signature = hmac.new(secret_key.encode('utf-8'), message.encode('utf-8'), hashlib.sha256).hexdigest()
    headers = {
       'ACCESS-KEY'      : access_key,
       'ACCESS-NONCE'    : nonce,
       'ACCESS-SIGNATURE': signature
    }
    return headers
