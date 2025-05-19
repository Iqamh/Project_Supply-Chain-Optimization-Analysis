# Import Library
import pandas as pd

# Load Data
df = pd.read_csv("./data/DataCoSupplyChainDataset.csv", encoding="latin1")
print(df.head())

# Check Information Data
print(df.info())
print(df.isnull().sum())

# Cleaning and Preprocessing Data
df["order date (DateOrders)"] = pd.to_datetime(df["order date (DateOrders)"])
df["shipping date (DateOrders)"] = pd.to_datetime(df["shipping date (DateOrders)"])
df["shipping delays (DateOrders)"] = (df["shipping date (DateOrders)"]-df["order date (DateOrders)"]).dt.days

# Save Cleaned Data
df.to_csv("./data/DataCoSupplyChainDataset_Cleaned.csv", index=False)

### Customer Segmentation ###
