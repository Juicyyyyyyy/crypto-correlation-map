import pandas as pd


def calculate_returns(df):
	# Ensure the data is sorted by timestamp
	df = df.sort_values('timestamp')

	# Calculate the percentage change in closing price
	df['return'] = df['close'].pct_change()

	# Drop the rows with missing values (this will be the first row)
	df = df.dropna()

	return df


def calculate_correlations(dfs):
	# Merge all dataframes into one, using timestamp as index
	merged_df = pd.concat(dfs, axis=1)

	# Calculate the correlation matrix
	corr_matrix = merged_df.corr()

	return corr_matrix
