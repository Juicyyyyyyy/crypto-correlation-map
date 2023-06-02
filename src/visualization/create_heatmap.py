import seaborn as sns
import matplotlib.pyplot as plt

def create_heatmap(corr_matrix, title='Crypto-Asset Correlation Heatmap'):
    # Create the heatmap using seaborn
    plt.figure(figsize=(15, 15))  # Increase figure size
    sns.heatmap(corr_matrix, vmin=-1, vmax=1, center=0, cmap='coolwarm', annot=True, fmt=".2f", annot_kws={"size": 10})

    # Add title and labels
    plt.title(title, fontsize=20)
    plt.xlabel('Cryptocurrency', fontsize=15)
    plt.ylabel('Cryptocurrency', fontsize=15)

    # Rotate the tick labels for better readability
    plt.xticks(rotation=45)
    plt.yticks(rotation=45)

    # Show the plot
    plt.show()
