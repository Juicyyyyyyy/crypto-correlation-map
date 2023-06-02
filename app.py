from src.data_collection.fetch_data import fetch_historical_data
from src.data_processing.calculate_returns import calculate_returns, calculate_correlations
from src.visualization.create_heatmap import create_heatmap

# Define the cryptocurrencies you're interested in and the time period
symbols = ['BTC/USDT', 'ETH/USDT', 'ADA/USDT']  # Add more symbols as per your interest
timeframe = '1d'
since = 1672444800000  # Start time (1st Jan 2023)
till = 1677705599000  # End time (30th Jun 2023)

# Fetch historical data, calculate returns, and merge the return data
returns = {}
for symbol in symbols:
    ohlcv = fetch_historical_data(symbol, timeframe, since, till)
    returns[symbol] = calculate_returns(ohlcv)

# Calculate correlations
correlations = calculate_correlations(returns)

# Create heatmap
create_heatmap(correlations)