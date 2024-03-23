import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# Load historical data for December 2023
btc_data = pd.read_csv('btc_usd_data_inr.csv')
eth_data = pd.read_csv('eth_usd_data_inr.csv')
xrp_data = pd.read_csv('xrp_usd_data_inr.csv')

# Convert 'Date' column to datetime
btc_data['Date'] = pd.to_datetime(btc_data['Date'])
eth_data['Date'] = pd.to_datetime(eth_data['Date'])
xrp_data['Date'] = pd.to_datetime(xrp_data['Date'])


# Filter data for December 2023
btc_data_dec = btc_data[(btc_data['Date'] >= '2023-12-01') & (btc_data['Date'] <= '2023-12-31')]
eth_data_dec = eth_data[(eth_data['Date'] >= '2023-12-01') & (eth_data['Date'] <= '2023-12-31')]
xrp_data_dec = xrp_data[(xrp_data['Date'] >= '2023-12-01') & (xrp_data['Date'] <= '2023-12-31')]

# Train ARIMA model
btc_model = ARIMA(btc_data_dec['Close'], order=(5, 1, 0))
btc_model_fit = btc_model.fit()

eth_model = ARIMA(eth_data_dec['Close'], order=(5, 1, 0))
eth_model_fit = eth_model.fit()

xrp_model = ARIMA(xrp_data_dec['Close'], order=(5, 1, 0))
xrp_model_fit = xrp_model.fit()

# Forecast next week data
btc_forecast = btc_model_fit.forecast(steps=7)
eth_forecast = eth_model_fit.forecast(steps=7)
xrp_forecast = xrp_model_fit.forecast(steps=7)

# Create DataFrame for predicted data
future_dates = pd.date_range(start='2024-01-01', periods=7)
btc_predicted_data = pd.DataFrame({'Date': future_dates, 'Predicted_Close_Price': btc_forecast})

future_dates = pd.date_range(start='2024-01-01', periods=7)
eth_predicted_data = pd.DataFrame({'Date': future_dates, 'Predicted_Close_Price': eth_forecast})

future_dates = pd.date_range(start='2024-01-01', periods=7)
xrp_predicted_data = pd.DataFrame({'Date': future_dates, 'Predicted_Close_Price': xrp_forecast})

btc_predicted_data.reset_index(drop=True, inplace=True)
btc_predicted_data.index += 1

eth_predicted_data.reset_index(drop=True, inplace=True)
eth_predicted_data.index += 1

xrp_predicted_data.reset_index(drop=True, inplace=True)
xrp_predicted_data.index += 1

# Save predicted data to CSV file
btc_predicted_data.to_csv('btc_predicted_data.csv')
eth_predicted_data.to_csv('eth_predicted_data.csv')
xrp_predicted_data.to_csv('xrp_predicted_data.csv')

# Print predicted data
print("Predicted Close Prices for the next week (from January 1, 2024) for Bitcoin:")
print(btc_predicted_data)

print("Predicted Close Prices for the next week (from January 1, 2024) for Ethereum:")
print(eth_predicted_data)

print("Predicted Close Prices for the next week (from January 1, 2024) for Ripple:")
print(xrp_predicted_data)


# Visualize the results
# Bitcoin
plt.plot(btc_data_dec['Date'], btc_data_dec['Close'], label='Actual Close Prices', color='blue')
plt.plot(btc_predicted_data['Date'], btc_predicted_data['Predicted_Close_Price'], label='Predicted Close Prices', color='orange')
plt.title('Bitcoin Actual vs Predicted Close Prices for December 2023 & Next Week')
plt.xlabel('Date')
plt.ylabel('Price (INR)')
plt.legend()
plt.grid(True)
plt.show()

#Ethereum
plt.plot(eth_data_dec['Date'], eth_data_dec['Close'], label='Actual Close Prices', color='blue')
plt.plot(eth_predicted_data['Date'], eth_predicted_data['Predicted_Close_Price'], label='Predicted Close Prices', color='orange')
plt.title(' Ethereum Actual vs Predicted Close Prices for December 2023 and Next Week')
plt.xlabel('Date')
plt.ylabel('Price (INR)')
plt.legend()
plt.grid(True)
plt.show()

#Ripple
plt.plot(xrp_data_dec['Date'], xrp_data_dec['Close'], label='Actual Close Prices', color='blue')
plt.plot(xrp_predicted_data['Date'], xrp_predicted_data['Predicted_Close_Price'], label='Predicted Close Prices', color='orange')
plt.title('Ripple Actual vs Predicted Close Prices for December 2023 and Next Week')
plt.xlabel('Date')
plt.ylabel('Price (INR)')
plt.legend()
plt.grid(True)
plt.show()



