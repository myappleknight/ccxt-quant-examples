"""每 10 秒抓一次 BTC/USDT 價格，只保留最近 1 小時資料（記憶體不會一直變大）。
Poll BTC/USDT every 10 s with ccxt; keeps only the last hour of prices in memory.
不需要 API 金鑰 / No API key needed.
"""
import logging
import time
from collections import deque

import ccxt

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
EXCHANGE = "binance"     # binance / okx / bybit / bitget / gateio ...
SYMBOL = "BTC/USDT"

ex = getattr(ccxt, EXCHANGE)({"enableRateLimit": True})
prices = deque(maxlen=360)

while True:
    try:
        last = ex.fetch_ticker(SYMBOL)["last"]
        prices.append(last)
        logging.info("%s %s %.2f (avg %.2f over %d samples)", EXCHANGE, SYMBOL, last, sum(prices) / len(prices), len(prices))
    except Exception as e:  # 網路或交易所暫時出錯：等一下再試 / transient error: back off
        logging.warning("fetch failed: %s; retry in 30 s", e)
        time.sleep(30)
    time.sleep(10)
