"""均線交叉「訊號」範例：只印出訊號，不會下單。
Moving-average crossover *signal* example: prints signals only, never places orders.
"""
import logging
import time

import ccxt
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
ex = ccxt.binance({"enableRateLimit": True})
SYMBOL, TIMEFRAME, FAST, SLOW = "ETH/USDT", "15m", 20, 60
last_state = None

while True:
    try:
        bars = ex.fetch_ohlcv(SYMBOL, TIMEFRAME, limit=SLOW + 5)   # 只抓需要的 K 線數量 / fetch only what we need
        df = pd.DataFrame(bars, columns=["ts", "open", "high", "low", "close", "volume"])
        fast = df["close"].rolling(FAST).mean().iloc[-1]
        slow = df["close"].rolling(SLOW).mean().iloc[-1]
        state = "above" if fast > slow else "below"
        if last_state and state != last_state:
            logging.info("SIGNAL %s: fast MA crossed %s slow MA (%.2f vs %.2f)", SYMBOL, state, fast, slow)
        else:
            logging.info("%s fast %.2f slow %.2f (%s)", SYMBOL, fast, slow, state)
        last_state = state
    except Exception as e:
        logging.warning("error: %s", e)
        time.sleep(30)
    time.sleep(60)
