import seaborn as sns
import matplotlib.pyplot as plt

def create_heatmap(corr_matrix, title='Crypto-Asset Correlation Heatmap'):
    # Create the heatmap using seaborn
    plt.figure(figsize=(10, 10))
    sns.heatmap(corr_matrix, vmin=-1, vmax=1, center=0, cmap='coolwarm', annot=True, fmt=".2f")

    # Add title and labels
    plt.title(title)
    plt.xlabel('Cryptocurrency')
    plt.ylabel('Cryptocurrency')

    # Show the plot
    plt.show()
