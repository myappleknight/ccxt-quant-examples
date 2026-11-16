# ELH Quant Examples — ccxt 量化交易範例（可直接 24 小時寄養）

Small, readable **Python + [ccxt](https://github.com/ccxt/ccxt)** examples that follow good habits for long-running trading bots:
rate limiting, retry on errors, bounded memory, API keys from environment variables, and a dry-run default.

簡單好讀的 Python ccxt 範例，照長期執行的好習慣撰寫：開啟限速、出錯自動重試、記憶體不會一直變大、金鑰從環境變數讀取、預設只模擬不下單。

| Example | What it does | Needs API key |
| --- | --- | --- |
| [`examples/price_monitor.py`](examples/price_monitor.py) | Poll a ticker every 10 s, keep the last hour in memory | No |
| [`examples/ma_cross_signal.py`](examples/ma_cross_signal.py) | Moving-average crossover **signals** (no orders) with pandas | No |
| [`examples/grid_dry_run.py`](examples/grid_dry_run.py) | Grid trading, **dry-run by default** | Only with `DRY_RUN=0` |

```bash
pip install ccxt pandas
python examples/price_monitor.py
```

## Run them 24/7 / 讓程式 24 小時執行

These scripts are written to pass the review of [ELH VPN Cloud — Python quant script hosting](https://vpn.easylifehub.net/python-quant-hosting/):
upload a `.py` file, it runs in an isolated sandbox on a server in **Taipei, Taiwan** that can only reach exchange APIs.
One free 3-minute trial per day with a memory/traffic report. Measured peak memory: `price_monitor.py` ≈ 200 MB (ccxt), `ma_cross_signal.py` ≈ 230 MB (ccxt + pandas).

這些範例可以直接上傳到 [ELH VPN Cloud 的 Python 量化腳本寄養](https://vpn.easylifehub.net/python-quant-hosting/) 免費試跑。

Guides (Traditional Chinese): [ccxt 入門](https://vpn.easylifehub.net/ccxt-python-price-example/) ·
[API 金鑰安全設定](https://vpn.easylifehub.net/exchange-api-key-safety/) ·
[量化程式要放哪裡跑](https://vpn.easylifehub.net/quant-bot-where-to-run/) ·
English: [Run your Python trading bot 24/7 from Taiwan](https://vpn.easylifehub.net/python-trading-bot-hosting-taiwan/)

## Safety / 安全

- Use a **sub-account** API key with **trading only, withdrawals disabled**, and restrict it to your server's IP.
- 金鑰請用子帳號、只開交易、不開提領，並設定 IP 白名單。

**Disclaimer**: educational examples only, not investment advice. Trading involves risk of loss; you are responsible for your own trades.
範例僅供學習，不構成投資建議；交易有虧損風險，請自行負責。

License: MIT
