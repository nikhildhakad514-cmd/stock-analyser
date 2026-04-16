import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("stock_data.csv")

# Convert date
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

# Plot price
plt.figure()
plt.plot(data['Close'])
plt.title("Stock Price Trend")
plt.xlabel("Date")
plt.ylabel("Price")
plt.savefig("price_plot.png")
plt.close()

# Returns
data['Returns'] = data['Close'].pct_change()

plt.figure()
plt.plot(data['Returns'])
plt.title("Daily Returns")
plt.xlabel("Date")
plt.ylabel("Returns")
plt.savefig("returns_plot.png")
plt.close()

# Volatility
print("Volatility:", data['Returns'].std())
