from src.data_collection.fetch_data import fetch_historical_data
from src.data_processing.calculate_returns import calculate_returns, calculate_correlations
from src.visualization.create_heatmap import create_heatmap


def calculate_returns_for_symbols(symbols, timeframe, since, till):
    returns = {}
    for symbol in symbols:
        ohlcv = fetch_historical_data(symbol, timeframe, since, till)
        ohlcv_with_returns = calculate_returns(ohlcv)
        returns[symbol] = ohlcv_with_returns['return']
    return returns

returns = calculate_returns_for_symbols(['BTC/USDT', 'ETH/USDT', 'ADA/USDT', 'XRP/USDT', 'DOT/USDT'], '1d', 1672444800000, 1677705599000)

correlations = calculate_correlations(returns)
create_heatmap(correlations)
