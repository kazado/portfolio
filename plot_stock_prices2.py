import pandas as pd
import matplotlib.pyplot as plt

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

# Plot Up and Down Probabilities for TSLA with baseline
plt.figure(figsize=(10, 5))
plt.plot(tsla_df_trimmed["Timestamp"], tsla_df_trimmed["UpProbability"], label="Up Probability", color="green")
plt.plot(tsla_df_trimmed["Timestamp"], tsla_df_trimmed["DownProbability"], label="Down Probability", color="red")
plt.axhline(0.5, color="blue", linestyle="--", label="Indifference (p=0.5)")
plt.xlabel("Date")
plt.ylabel("Probability")
plt.title("TSLA Up and Down Probabilities Over Time")
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("tsla_probabilities_with_baseline.png")
# plt.show()

# Plot Displacement Energy for TSLA with baseline
plt.figure(figsize=(10, 5))
plt.plot(tsla_df_trimmed["Timestamp"], tsla_df_trimmed["DisplacementEnergy"], label="Displacement Energy", color="blue")
plt.axhline(0.0, color="red", linestyle="--", label="No Energy Change (E=0.0)")
plt.xlabel("Date")
plt.ylabel("Displacement Energy")
plt.title("TSLA Displacement Energy Over Time")
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("tsla_displacement_energy_with_baseline.png")
# plt.show()

# Double-sided plot for Temperature and Free Energy
fig, ax1 = plt.subplots(figsize=(10, 5))

color = 'tab:red'
ax1.set_xlabel('Date')
ax1.set_ylabel('Temperature', color=color)
ax1.plot(tsla_df_trimmed["Timestamp"], tsla_df_trimmed["Temp"], color=color, label="Temperature")
ax1.tick_params(axis='y', labelcolor=color)
ax1.tick_params(axis='x', rotation=45)
ax1.grid(True)
ax1.legend(loc='upper left')
fig.tight_layout()

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('Free Energy', color=color)  # we already handled the x-label with ax1
ax2.plot(tsla_df_trimmed["Timestamp"], tsla_df_trimmed["FreeEnergy"], color=color, label="Free Energy")
ax2.tick_params(axis='y', labelcolor=color)
ax2.legend(loc='upper right')

plt.title("TSLA Temperature and Free Energy Over Time")
plt.savefig("tsla_temp_free_energy.png")
# plt.show()