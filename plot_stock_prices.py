import matplotlib.pyplot as plt
import csv
from datetime import datetime

# Define file path for the merged portfolio file
data_file = "Corey_Portfolio_2025-03-10.csv"

# Initialize lists to store data
timestamps = []
stock_data = {}

# Read the CSV file
with open(data_file, 'r') as file:
    reader = csv.reader(file)
    headers = next(reader)  # Read the first row as headers
    stock_symbols = headers[1:]  # Skip the first column (timestamps)
    
    for symbol in stock_symbols:
        stock_data[symbol] = []
    
    for row in reader:
        timestamps.append(datetime.strptime(row[0], '%m/%d/%y'))
        for i, symbol in enumerate(stock_symbols):
            try:
                stock_data[symbol].append(float(row[i+1]))  # Convert to float
            except ValueError:
                stock_data[symbol].append(None)  # Handle missing data if necessary

# Plot the data
plt.figure(figsize=(12, 6))
for symbol in stock_symbols:
    plt.plot(timestamps, stock_data[symbol], label=symbol)

plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.title("Stock Closing Prices Over Time")
plt.legend(title="Stock Symbol")  # Add title to legend
plt.grid()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()