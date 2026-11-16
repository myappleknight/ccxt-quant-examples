"""網格交易「模擬」範例：預設 DRY_RUN=1，只在記憶體裡模擬成交，不會真的下單。
Grid-trading *dry-run* example. With DRY_RUN=1 (default) it only simulates fills in memory.
要真的下單：設定環境變數 DRY_RUN=0、BINANCE_API_KEY、BINANCE_API_SECRET（請用只開交易、不開提領的子帳號金鑰）。
To trade for real set DRY_RUN=0 plus BINANCE_API_KEY / BINANCE_API_SECRET (sub-account key, withdrawals disabled).
風險自負，請先用小金額測試。Use at your own risk; test with small amounts first.
"""
import logging
import os
import time

import ccxt

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
DRY_RUN = os.environ.get("DRY_RUN", "1") != "0"
SYMBOL = "BTC/USDT"
LOW, HIGH, LEVELS, QTY = 60000.0, 70000.0, 10, 0.0005

ex = ccxt.binance({
    "enableRateLimit": True,
    "apiKey": os.environ.get("BINANCE_API_KEY", ""),
    "secret": os.environ.get("BINANCE_API_SECRET", ""),
})
step = (HIGH - LOW) / LEVELS
grid = [round(LOW + i * step, 2) for i in range(LEVELS + 1)]
holding = {g: False for g in grid}   # 每一格是否持有 / whether each level holds a position

def order(side, price):
    if DRY_RUN:
        logging.info("[DRY RUN] %s %s %s @ %.2f", side, QTY, SYMBOL, price)
        return
    ex.create_order(SYMBOL, "limit", side, QTY, price)
    logging.info("placed %s %s %s @ %.2f", side, QTY, SYMBOL, price)

logging.info("grid %s levels between %.0f and %.0f, dry_run=%s", LEVELS, LOW, HIGH, DRY_RUN)
while True:
    try:
        last = ex.fetch_ticker(SYMBOL)["last"]
        for g in grid:
            if last <= g and not holding[g]:
                order("buy", g); holding[g] = True
            elif last >= g + step and holding[g]:
                order("sell", g + step); holding[g] = False
        logging.info("last %.2f, positions %d/%d", last, sum(holding.values()), len(grid))
    except Exception as e:
        logging.warning("error: %s", e)
        time.sleep(30)
    time.sleep(15)
