import sys,os
current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(current_dir, '../'))

from coincheck.market import Market

def test_ticker():
    m1 = Market()
    return m1.ticker()

def test_trades():
    m1 = Market()
    return m1.trades()

def test_orderbooks():
    m1 = Market()
    return m1.orderbooks()


if __name__ == '__main__':
    print(test_ticker())
    test_trades()
    test_orderbooks()
