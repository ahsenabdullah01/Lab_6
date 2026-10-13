import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create a messy product inventory dataset
data = {
    "Product": [
        "Cola",
        "Chips",
        "Milk",
        "Biscuits",
        "Juice",
        "Yogurt",
        "Water",
        "Cookies",
        "Cheese",
        "Soda",
    ],
    "Category": [
        "beverages ",
        "SNACKS",
        " Dairy",
        "Snacks",
        "BEVERAGES",
        "dairy ",
        " Beverages",
        "snacks ",
        "DAIRY",
        "Beverages",
    ],
    "Price": [
        "Rs. 1,250",
        "Rs. 90",
        "Rs. 450",
        "Rs. 120",
        "Rs. 1,800",
        "Rs. 300",
        "Rs. 50",
        "Rs. 150",
        "Rs. 600",
        "Rs. 1,000",
    ],
    "Stock": [40, 120, 60, 100, 35, 55, 200, 90, 45, 50],
}

df = pd.DataFrame(data)

print("Original Inventory:")
print(df)

# Step 2: Clean category names
df["Category"] = df["Category"].str.strip().str.title()

# Step 3: Remove currency prefix and commas
df["Price"] = (
    df["Price"]
    .str.replace("Rs. ", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)

# Step 4: Label encode the category
df["Category_Code"] = df["Category"].astype("category").cat.codes

print("\nCleaned Inventory:")
print(df)

# Step 5: Calculate average price per category
avg_price = df.groupby("Category")["Price"].mean()

print("\nAverage Price by Category:")
print(avg_price)

# Step 6: Calculate total stock per category
stock_by_category = df.groupby("Category")["Stock"].sum()

print("\nStock by Category:")
print(stock_by_category)

# Step 7: Create side-by-side plots
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Bar chart: Average price per category
axes[0].bar(avg_price.index, avg_price.values)
axes[0].set_title("Average Price by Category")
axes[0].set_xlabel("Category")
axes[0].set_ylabel("Average Price (Rs.)")
axes[0].tick_params(axis="x", rotation=20)

# Pie chart: Share of total stock
axes[1].pie(
    stock_by_category.values,
    labels=stock_by_category.index,
    autopct="%1.1f%%",
    startangle=90,
)
axes[1].set_title("Stock Share by Category")

plt.tight_layout()

# Step 8: Save the figure
plt.savefig("inventory_plots.png", dpi=300)
plt.show()

print("\nSaved inventory_plots.png")
