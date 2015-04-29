import time
import hmac
import hashlib
import settings
import datetime
import pytz

def nounce():
    '''
    return utc unix time in second

    TODO: 
    - return utc unix time in micro second
    '''
    return str(int(time.mktime(datetime.datetime.now(pytz.utc).timetuple())))

def make_header(url,
                access_key=None,
                secret_key=None):
    ''' create request header function
    :param url: URL for the new :class:`Request` object.
    '''
    nonce = nounce()
    url    = url
    message = nonce + url
    signature = hmac.new(secret_key.encode('utf-8'), message.encode('utf-8'), hashlib.sha256).hexdigest()
    headers = {
       'ACCESS-KEY'      : access_key,
       'ACCESS-NONCE'    : nonce,
       'ACCESS-SIGNATURE': signature
    }
    return headers

