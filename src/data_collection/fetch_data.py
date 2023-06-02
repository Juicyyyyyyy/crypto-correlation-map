import ccxt
import pandas as pd

def fetch_historical_data(symbol, timeframe, since, till):
    exchange = ccxt.binance({
        'enableRateLimit': True,  # this option is required to minimize the risk of being banned by the exchange
    })

    # Fetch OHLCV (Open, High, Low, Close, Volume) data
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe, since, till)

    # Convert to DataFrame
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

    return df
