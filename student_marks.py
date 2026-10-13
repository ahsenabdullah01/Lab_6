import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create the messy student dataset
data = {
    "Name": [" ali", "SARA ", "bilal", " Ayesha", "HAMZA", "zain ", "Noor", " usman "],
    "Marks": ["72", "85", "absent", "64", "90", "78", "81", "69"],
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Step 2: Clean student names
df["Name"] = df["Name"].str.strip().str.title()

# Step 3: Convert marks to numeric values
df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")

# Step 4: Replace the absent mark with the mean
mean_marks = df["Marks"].mean()
df["Marks"] = df["Marks"].fillna(mean_marks)

# Step 5: Display cleaned dataset
print("\nCleaned Student Data:")
print(df)

# Step 6: Create a bar plot
plt.figure(figsize=(9, 5))
plt.bar(df["Name"], df["Marks"])

plt.title("Student Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.xticks(rotation=30)
plt.tight_layout()

# Step 7: Save the plot in the Lab_6 folder
plt.savefig("marks_bar.png", dpi=300)
plt.show()

print("\nSaved marks_bar.png")
