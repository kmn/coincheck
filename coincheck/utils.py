import time
import hmac
import hashlib
import settings

def make_header(url):
    ''' create request header function
    :param url: URL for the new :class:`Request` object.
    '''
    nonce = str(time.time()).split('.')[0]
    key    = settings.access_key
    secret = settings.secret_key
    url    = url
    message = nonce + url
    signature = hmac.new(secret.encode('utf-8'), message.encode('utf-8'), hashlib.sha256).hexdigest()
    headers = {
       'ACCESS-KEY'      : key,
       'ACCESS-NONCE'    : nonce,
       'ACCESS-SIGNATURE': signature
    }
    return headers
