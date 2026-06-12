import pandas as pd

# Read raw data
df = pd.read_csv("data/raw/orders.csv")

# Create a new column
df["tax"] = df["amount"] * 0.18

# Create final amount column
df["final_amount"] = df["amount"] + df["tax"]

# Save processed data
df.to_csv("data/processed/orders_processed.csv", index=False)

print("Transformation completed successfully")
print(df.head())