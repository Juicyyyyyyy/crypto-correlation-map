from src.data_collection.fetch_data import fetch_historical_data
from src.data_processing.calculate_returns import calculate_returns, calculate_correlations
from src.visualization.create_heatmap import create_heatmap


"""
symbols = ['BTC/USDT', 'ETH/USDT', 'ADA/USDT', 'XRP/USDT', 'DOT/USDT']
timeframe = '1d'
since = 1672444800000  # Start time (1st Jan 2023)
till = 1677705599000  # End time (30th Jun 2023)

# Fetch historical data, calculate returns, and merge the return data
# Fetch historical data, calculate returns, and add the return series to the 'returns' dictionary
returns = {}
for symbol in symbols:
    ohlcv = fetch_historical_data(symbol, timeframe, since, till)
    ohlcv_with_returns = calculate_returns(ohlcv)
    returns[symbol] = ohlcv_with_returns['return']
    
correlations = calculate_correlations(returns)
create_heatmap(correlations)
"""

def calculate_returns_for_symbols(symbols, timeframe, since, till):
    returns = {}
    for symbol in symbols:
        ohlcv = fetch_historical_data(symbol, timeframe, since, till)
        ohlcv_with_returns = calculate_returns(ohlcv)
        returns[symbol] = ohlcv_with_returns['return']
    return returns
