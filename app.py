from src.data_collection.fetch_data import fetch_historical_data
from src.data_processing.calculate_returns import calculate_returns, calculate_correlations
from src.visualization.create_heatmap import create_heatmap

# Define the cryptocurrencies you're interested in and the time period
symbols = ['BTC/USDT', 'ETH/USDT', 'ADA/USDT', 'XRP/USDT', 'DOT/USDT', 'UNI/USDT', 'LTC/USDT', 'LINK/USDT', 'BCH/USDT', 'XLM/USDT', 'USDC/USDT', 'DOGE/USDT', 'AAVE/USDT', 'ATOM/USDT', 'AVAX/USDT', 'BNB/USDT', 'EOS/USDT', 'ETC/USDT', 'FIL/USDT', 'MKR/USDT', 'NEO/USDT', 'SNX/USDT', 'SOL/USDT', 'TRX/USDT', 'VET/USDT', 'XEM/USDT', 'YFI/USDT', 'ZEC/USDT']
  # Add more symbols as per your interest
timeframe = '1d'
since = 1672444800000  # Start time (1st Jan 2023)
till = 1677705599000  # End time (30th Jun 2023)

# Fetch historical data, calculate returns, and merge the return data
# Fetch historical data, calculate returns, and add the return series to the 'returns' dictionary
returns = {}
for symbol in symbols:
    ohlcv = fetch_historical_data(symbol, timeframe, since, till)
    ohlcv_with_returns = calculate_returns(ohlcv)
    returns[symbol] = ohlcv_with_returns['return']  # we only want to keep the 'return' series

# Calculate correlations and create heatmap
correlations = calculate_correlations(returns)
create_heatmap(correlations)
