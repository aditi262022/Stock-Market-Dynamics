
import pandas as pd
import matplotlib.pyplot as plt

def plot_crypto_data(data_dec, predicted_data_jan, title):
    # Set up the plot
    plt.figure(figsize=(12, 6))

    # Plot actual close price for December 2023
    plt.plot(data_dec['Date'], data_dec['Close'], label='December 2023 Actual Close Price', color='blue')

    # Plot predicted close price for the first week of January 2024
    plt.plot(predicted_data_jan['Date'], predicted_data_jan['Predicted_Close_Price'], label='January 2024 Predicted Close Price', color='orange')

    # Initialize arrow color
    arrow_color = 'black'

    # Add arrows for buy, sell, or neutral based on the difference between predicted close price and previous day's close price
    for index, row in predicted_data_jan.iterrows():
        if index == 0:
            arrow_direction = '--'  # Placeholder for the first data point
        else:
            arrow_color = 'green' if row['Predicted_Close_Price'] - predicted_data_jan.iloc[index - 1]['Predicted_Close_Price'] > 0 else ('red' if row['Predicted_Close_Price'] - predicted_data_jan.iloc[index - 1]['Predicted_Close_Price'] < 0 else 'black')
            arrow_direction = '↑' if arrow_color == 'green' else ('↓' if arrow_color == 'red' else "--")
        plt.annotate(arrow_direction, (row['Date'], row['Predicted_Close_Price']), textcoords="offset points", xytext=(0,10),
                     ha='center', fontsize=12, color=arrow_color)

    # Format the axes
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Price (INR)')
    plt.xticks(rotation=45)
    plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y-%m-%d'))  # Format x-axis dates

    # Add legend
    plt.legend()

    # Show the plot
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

# Load historical data for December 2023
btc_data_dec = pd.read_csv('btc_usd_data_inr.csv')
eth_data_dec = pd.read_csv('eth_usd_data_inr.csv')
xrp_data_dec = pd.read_csv('xrp_usd_data_inr.csv')

# Convert 'Date' column to datetime
btc_data_dec['Date'] = pd.to_datetime(btc_data_dec['Date'])
eth_data_dec['Date'] = pd.to_datetime(eth_data_dec['Date'])
xrp_data_dec['Date'] = pd.to_datetime(xrp_data_dec['Date'])

# Filter data for December 2023
btc_data_dec = btc_data_dec[(btc_data_dec['Date'] >= '2023-12-01') & (btc_data_dec['Date'] <= '2023-12-31')]
eth_data_dec = eth_data_dec[(eth_data_dec['Date'] >= '2023-12-01') & (eth_data_dec['Date'] <= '2023-12-31')]
xrp_data_dec = xrp_data_dec[(xrp_data_dec['Date'] >= '2023-12-01') & (xrp_data_dec['Date'] <= '2023-12-31')]

# Load predicted data for January 2024
btc_predicted_data_jan = pd.read_csv('btc_predicted_data.csv')
eth_predicted_data_jan = pd.read_csv('eth_predicted_data.csv')
xrp_predicted_data_jan = pd.read_csv('xrp_predicted_data.csv')

# Convert 'Date' column to datetime
btc_predicted_data_jan['Date'] = pd.to_datetime(btc_predicted_data_jan['Date'])
eth_predicted_data_jan['Date'] = pd.to_datetime(eth_predicted_data_jan['Date'])
xrp_predicted_data_jan['Date'] = pd.to_datetime(xrp_predicted_data_jan['Date'])

# Filter predicted data for the first week of January 2024
btc_predicted_data_jan = btc_predicted_data_jan[(btc_predicted_data_jan['Date'] >= '2024-01-01') & (btc_predicted_data_jan['Date'] <= '2024-01-08')]
eth_predicted_data_jan = eth_predicted_data_jan[(eth_predicted_data_jan['Date'] >= '2024-01-01') & (eth_predicted_data_jan['Date'] <= '2024-01-08')]
xrp_predicted_data_jan = xrp_predicted_data_jan[(xrp_predicted_data_jan['Date'] >= '2024-01-01') & (xrp_predicted_data_jan['Date'] <= '2024-01-08')]

# Plot Bitcoin data
plot_crypto_data(btc_data_dec, btc_predicted_data_jan, 'Bitcoin Actual Close Price for December 2023 and Predicted Close Price for January 2024')

# Plot Ethereum data
plot_crypto_data(eth_data_dec, eth_predicted_data_jan, 'Ethereum Actual Close Price for December 2023 and Predicted Close Price for January 2024')

# Plot Ripple data
plot_crypto_data(xrp_data_dec, xrp_predicted_data_jan, 'XRP Actual Close Price for December 2023 and Predicted Close Price for January 2024')



