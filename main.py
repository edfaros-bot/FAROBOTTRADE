import ccxt
import pandas as pd

exchange = ccxt.binance()

def get_data():
    ohlcv = exchange.fetch_ohlcv("BTC/USDT", timeframe="1m", limit=50)
    df = pd.DataFrame(ohlcv, columns=["time", "open", "high", "low", "close", "volume"])
    return df

def run():
    try:
        df = get_data()
        print("✅ Funcionando!")
        print(df.tail())
    except Exception as e:
        print("❌ Erro:", e)

if __name__ == "__main__":
    run()
