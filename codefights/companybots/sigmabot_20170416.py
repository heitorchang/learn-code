from operator import itemgetter

def serverFarm(jobs, servers):
    jobs = [-j for j in jobs]
    e = list(enumerate(jobs))
    srv = [[i, [], 0] for i in range(servers)]
    jobs = sorted(e, key=itemgetter(1,0))

    for j in jobs:
        srv[0][1].append(j[0])
        srv[0][2] += -j[1]
        srv = sorted(srv, key=itemgetter(2,0))
        srv = sorted(srv, key=itemgetter(0))

    result = []
    for s in srv:
        result.append(s[1])
    return result

from datetime import datetime
from collections import defaultdict, namedtuple

Trade = namedtuple("Trade", "d symbol price")

def OHLC(prices):
    O = prices[0]
    H = max(prices)
    L = min(prices)
    C = prices[-1]
    return ["{:.2f}".format(s) for s in [O, H, L, C]]
    
def dailyOHLC(timestamp, instrument, side, price, size):
    n = len(timestamp)
    byDate = defaultdict()
    trades = []
    dates = []
    for i in range(len(timestamp)):
        t = timestamp[i]
        tradeDate = datetime.fromtimestamp(t).strftime("%Y-%m-%d")
        if tradeDate not in dates:
            dates.append(tradeDate)

        byDate[tradeDate] = defaultdict(list)
        trades.append(Trade(tradeDate, instrument[i], price[i]))

    for t in trades:
        byDate[t.d][t.symbol].append(t.price)

    report = []
    for d in dates:
        pr('d')
        symbols = byDate[d].keys()
        symbols = sorted(symbols)
        pr('symbols')
        for s in symbols:
            ohlc = OHLC(byDate[d][s])
            report.append([d, s] + ohlc)
    return report
        

def test():
    # testeql(serverFarm([15, 30, 15, 5, 10], 3), [[1],[0,4],[2,3]])
    testeql(dailyOHLC([1450625399, 1450625400, 1450625500, 1450625550, 1451644200, 1451690100, 1451691000], [
        "HPQ", 
        "HPQ", 
        "HPQ", 
        "HPQ", 
        "AAPL", 
        "HPQ", 
        "GOOG"], ["sell", 
                  "buy", 
                  "buy", 
                  "sell", 
                  "buy", 
                  "buy", 
                  "buy"], [10, 20.3, 35.5, 8.65, 20, 10, 100.35], [10, 1, 2, 3, 5, 1, 10]), [
                      ["2015-12-20","HPQ","10.00","35.50","8.65","8.65"], 
                      ["2016-01-01","AAPL","20.00","20.00","20.00","20.00"], 
                      ["2016-01-01","GOOG","100.35","100.35","100.35","100.35"], 
                      ["2016-01-01","HPQ","10.00","10.00","10.00","10.00"]]) 
