import ccxt
import pandas as pd

exchange = ccxt.binance()

def get_data(symbol="BTC/USDT", timeframe="1m", limit=100):
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
    df = pd.DataFrame(ohlcv, columns=["time", "open", "high", "low", "close", "volume"])
    return df

if __name__ == "__main__":
    df = get_data()
    print(df.tail())
