import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("stock_data.csv")

# Show first rows
print(data.head())

# Convert Date column
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

# Plot Closing Price
plt.figure()
plt.plot(data['Close'])
plt.title("Stock Price Trend")
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()

# Calculate Returns
data['Returns'] = data['Close'].pct_change()

# Plot Returns
plt.figure()
plt.plot(data['Returns'])
plt.title("Daily Returns")
plt.xlabel("Date")
plt.ylabel("Returns")
plt.show()

# Risk (Volatility)
volatility = data['Returns'].std()
print("Volatility (Risk):", volatility)
