import sys,os
current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(current_dir, '../'))

from coincheck.account import Account
from coincheck import settings

def test_get_info():
    a1 = Account(access_key=settings.access_key, secret_key=settings.secret_key)
    return a1.get_info()

def test_get_balance():
    a1 = Account(access_key=settings.access_key, secret_key=settings.secret_key)
    return a1.get_balance()


if __name__ == '__main__':
    test_get_info()
    test_get_balance()
