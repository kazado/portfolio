import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import AutoDateLocator, AutoDateFormatter
from matplotlib.font_manager import FontProperties

# Define column names
columns = [
    "Symbol", "Timestamp", "Close", "UpProbability", "DownProbability",
    "DisplacementEnergy", "WrongEnergy", "Temp", "Noise", "Resistance",
    "FreeEnergy", "ProbUp", "ProbDown"
]

# Load the CSV file
df = pd.read_csv("Corey_Portfolio_2025-03-10_Binary_Analysis_20250409-024932.csv",
                 sep=",", header=None, names=columns)

# Convert Timestamp to datetime
df["Timestamp"] = pd.to_datetime(df["Timestamp"], format="%m/%d/%y")

# Filter data for TSLA
tsla_df = df[df["Symbol"] == "TSLA"].copy()

# Start plotting from the 21st data point (index 20)
start_index = 20
tsla_df_trimmed = tsla_df.iloc[start_index:]

Title = "Corey Portfolio" # Setting a consistent title

# 1. Displacement Energy Over Time
plt.figure(figsize=(10, 5))
plt.plot(tsla_df_trimmed["Timestamp"], tsla_df_trimmed["DisplacementEnergy"], label="Displacement Energy", color="black")
plt.axhline(0.0, color="brown", linestyle="--", label="No Energy Change (E=0.0)")
plt.xlabel("Date")
plt.ylabel("Displacement Energy")
plt.title(f"{Title}, Energy")
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig(f"{Title.replace(' ', '_')}_displacement_energy.png")
plt.show()

# 2. Up/Down Probabilities Over Time
plt.figure(figsize=(10, 5))
plt.plot(tsla_df_trimmed["Timestamp"], tsla_df_trimmed["ProbUp"], label="Up Probability", color="green")
plt.plot(tsla_df_trimmed["Timestamp"], tsla_df_trimmed["ProbDown"], label="Down Probability", color="red")
plt.axhline(0.5, color="black", linestyle="--", label="Indifference (p=0.5)")
plt.xlabel("Date")
plt.ylabel("Probabilities")
plt.title(f"{Title}, Probabilities")
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig(f"{Title.replace(' ', '_')}_probabilities.png")
plt.show()

# 3. Temperature and Free Energy Over Time (Matching Style)
fig5, ax5 = plt.subplots(figsize=(10, 5))
plt.title(Title + ', Temperature-Free Energy')
dates = tsla_df_trimmed["Timestamp"].tolist()
learning = 0
temperature_data = tsla_df_trimmed["Temp"].tolist()
free_energy_data = tsla_df_trimmed["FreeEnergy"].tolist()
plt.xlim((dates[learning], dates[-1]))

ax5.plot_date(dates[learning:len(dates)], temperature_data[learning:len(dates)], 'r-', label='temperature')
ax5.tick_params(axis='y')
xtick_locator = AutoDateLocator()
xtick_formatter = AutoDateFormatter(xtick_locator)
ax5.xaxis.set_major_locator(xtick_locator)
ax5.xaxis.set_major_formatter(xtick_formatter)

ax5.set_xlabel('Date')
ax5.set_ylabel('Temperature')
ax5.autoscale_view()
ax5.grid(True)
fig5.autofmt_xdate()

ax6 = ax5.twinx()  # instantiate a second axis that shares the same x-axis

ax6.set_ylabel('Free energy', color='blue')
ax6.plot_date(dates[learning:len(dates)], free_energy_data[learning:len(dates)], 'b-', label='free energy')
ax6.tick_params(axis='y')

# Explicitly set y-axis limits for the right axis to ensure negative values are shown
min_free_energy = min(free_energy_data)
max_free_energy = max(free_energy_data)
ax6.set_ylim(min_free_energy * 1.1, max_free_energy * 1.1) # Add a small buffer

fontP = FontProperties(size='small')
ax5.legend(loc='upper center', bbox_to_anchor=(0.14, 0.98), ncol=2, prop=fontP)
ax6.legend(loc='upper center', bbox_to_anchor=(0.5, 0.3), ncol=2, prop=fontP)

fig5.tight_layout()  # otherwise the right y-label is slightly clipped
plt.savefig(f"{Title.replace(' ', '_')}_temp_free_energy_matching.png")
plt.show()

# 4. Prices Over Time (using 'Close' price)
plt.figure(figsize=(10, 5))
plt.plot(tsla_df_trimmed["Timestamp"], tsla_df_trimmed["Close"], color="black", label="Price")
price_baseline = tsla_df_trimmed["Close"].iloc[0] * 1.1 # Example: 10% above initial price
plt.plot(tsla_df_trimmed["Timestamp"], [price_baseline] * len(tsla_df_trimmed), color="red", linestyle="--", label="Initial Price + 10%")
plt.xlabel("Date")
plt.ylabel("Price")
plt.title(f"{Title}, Prices")
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig(f"{Title.replace(' ', '_')}_prices.png")
plt.show()

# 5. Thermal Probabilities (Using ProbUp and ProbDown with a different title)
plt.figure(figsize=(10, 5))
plt.plot(tsla_df_trimmed["Timestamp"], tsla_df_trimmed["ProbUp"], label="Thermal Prob Up", color="green")
plt.plot(tsla_df_trimmed["Timestamp"], tsla_df_trimmed["ProbDown"], label="Thermal Prob Down", color="red")
plt.axhline(0.5, color="black", linestyle="--", label="Indifference")
plt.xlabel("Date")
plt.ylabel("Thermal Probabilities")
plt.title(f"{Title}, Thermal Probabilities")
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig(f"{Title.replace(' ', '_')}_thermal_probabilities.png")
plt.show()