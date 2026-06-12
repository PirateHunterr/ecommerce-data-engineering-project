import pandas as pd

# Sample ecommerce data
data = {
    "order_id": [101, 102, 103],
    "customer_name": ["John", "Alice", "Bob"],
    "amount": [1200, 1500, 900]
}

df = pd.DataFrame(data)

# Save to raw layer
df.to_csv("data/raw/orders.csv", index=False)

print("Data successfully loaded to raw layer")

