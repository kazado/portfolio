import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import AutoDateLocator, AutoDateFormatter
from matplotlib.font_manager import FontProperties

# Define column names
columns = [
    "Symbol", "Timestamp", "Close", "UpProbability", "DownProbability",
    "DisplacementEnergy", "FreeEnergy", "Temp", "Noise", "Resistance",
    "Trend", "ProbUp", "ProbDown"
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

# Prepare data for the specific Temperature-Free Energy plot style
dates = tsla_df_trimmed["Timestamp"].tolist()
learning = 0  # We are starting from the beginning of the trimmed data
temperature_data = tsla_df_trimmed["Temp"].tolist()
free_energy_data = tsla_df_trimmed["FreeEnergy"].tolist()

# Create the double-sided plot for Temperature and Free Energy (Matching Style)
fig5, ax5 = plt.subplots(figsize=(10, 5))
plt.title(Title + ', Temperature-Free Energy')
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

ax6.set_ylabel('Free energy')
ax6.plot_date(dates[learning:len(dates)], free_energy_data[learning:len(dates)], 'b-', label='free energy')
ax6.tick_params(axis='y')

fontP = FontProperties(size='small')
ax5.legend(loc='upper center', bbox_to_anchor=(0.14, 0.98), ncol=3, prop=fontP)
ax6.legend(loc='upper center', bbox_to_anchor=(0.5, 0.3), ncol=3, prop=fontP)

fig5.tight_layout()  # otherwise the right y-label is slightly clipped
plt.savefig(f"{Title.replace(' ', '_')}_temp_free_energy_matching.png")
plt.show()