import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create a messy 15-day weather dataset
data = {
    "Date": [
        "2026-01-01",
        "2026-01-02",
        "2026-01-03",
        "2026-01-04",
        "2026-01-05",
        "2026-01-06",
        "2026-01-07",
        "2026-01-08",
        "2026-01-09",
        "2026-01-10",
        "2026-01-11",
        "2026-01-12",
        "2026-01-13",
        "2026-01-14",
        "2026-01-15",
        "2026-01-01",  # Duplicate row
    ],
    "City": [
        " lahore",
        "ISLAMABAD ",
        "Karachi",
        "lahore ",
        "Islamabad",
        "KARACHI",
        "Lahore",
        "islamabad",
        " Karachi",
        "LAHORE",
        "Karachi",
        "Islamabad",
        "lahore",
        "KARACHI ",
        "islamabad",
        " lahore",
    ],
    "Temperature": [
        "22C",
        "24C",
        "30C",
        "28C",
        "26C",
        "31C",
        "33C",
        "29C",
        "27C",
        "25C",
        "32C",
        "30C",
        "23C",
        "26C",
        "28C",
        "22C",
    ],
    "Humidity": [55, 60, None, 65, 58, None, 50, 62, 57, 68, None, 54, 59, 63, 56, 55],
    "Condition": [
        "sunny",
        " Cloudy",
        "RAINY",
        "Sunny ",
        "cloudy",
        " rainy ",
        "SUNNY",
        "Cloudy ",
        "sunny",
        "CLOUDY",
        "Rainy",
        " Sunny",
        "cloudy",
        "SUNNY ",
        "Cloudy",
        "SUNNY",
    ],
}

df = pd.DataFrame(data)

print("Original dataset:")
print(df.head())

# Step 2: Clean City and Condition
df["City"] = df["City"].str.strip().str.title()
df["Condition"] = df["Condition"].str.strip().str.title()

# Step 3: Convert Temperature to numeric
df["Temperature"] = df["Temperature"].str.replace("C", "", regex=False).astype(float)

# Step 4: Convert Date strings to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Step 5: Remove duplicate rows
df = df.drop_duplicates().reset_index(drop=True)

print("\nRows after dropping duplicates:", len(df))

# Step 6: Fill missing humidity using the median
humidity_median = df["Humidity"].median()

df["Humidity"] = df["Humidity"].fillna(humidity_median)

print("Missing Humidity filled with median:", humidity_median)
print("Remaining missing values:")
print(df.isnull().sum())

# Step 7: One-hot encode Condition
df_encoded = pd.get_dummies(df, columns=["Condition"], dtype=int)

condition_columns = [col for col in df_encoded.columns if col.startswith("Condition_")]

print("\nOne-hot encoded Condition columns:")
print(df_encoded[condition_columns].head())

# Step 8: Calculate condition counts
condition_counts = df["Condition"].value_counts()

print("\nCondition counts:")
print(condition_counts)

# Step 9: Calculate correlation
correlation = df["Temperature"].corr(df["Humidity"])

print("\nCorrelation (Temperature, Humidity):", round(correlation, 3))

# Step 10: Create a 2 x 2 dashboard
fig, axes = plt.subplots(2, 2, figsize=(13, 9))

# Plot 1: Temperature over time
axes[0, 0].plot(df["Date"], df["Temperature"], marker="o")
axes[0, 0].set_title("Temperature Over Date")
axes[0, 0].set_xlabel("Date")
axes[0, 0].set_ylabel("Temperature (C)")
axes[0, 0].tick_params(axis="x", rotation=45)

# Plot 2: Temperature vs Humidity
axes[0, 1].scatter(df["Temperature"], df["Humidity"])
axes[0, 1].set_title("Temperature vs Humidity")
axes[0, 1].set_xlabel("Temperature (C)")
axes[0, 1].set_ylabel("Humidity")

# Plot 3: Condition distribution
axes[1, 0].pie(
    condition_counts.values,
    labels=condition_counts.index,
    autopct="%1.1f%%",
    startangle=90,
)
axes[1, 0].set_title("Weather Condition Distribution")

# Plot 4: Temperature histogram
axes[1, 1].hist(df["Temperature"], bins=5, edgecolor="black")
axes[1, 1].set_title("Temperature Distribution")
axes[1, 1].set_xlabel("Temperature (C)")
axes[1, 1].set_ylabel("Number of Days")

# Overall dashboard title
fig.suptitle("Weather Overview", fontsize=16)

plt.tight_layout()

# Step 11: Save dashboard
plt.savefig("weather_dashboard.png", dpi=300)
plt.show()

print("\nSaved weather_dashboard.png")
