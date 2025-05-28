# Import Library
import pandas as pd

# Load Data
df = pd.read_csv("./data/DataCoSupplyChainDataset.csv", encoding="latin1")
print(df.head())

# Check Information Data
print(df.info())
print(df.isnull().sum())

# Cleaning and Preprocessing Data
df["Customer FullName"] = df[["Customer Fname", "Customer Lname"]].fillna("").agg(" ".join, axis=1).str.strip()

df["order date (DateOrders)"] = pd.to_datetime(df["order date (DateOrders)"])
df["shipping date (DateOrders)"] = pd.to_datetime(df["shipping date (DateOrders)"])
df["shipping delays (DateOrders)"] = (df["shipping date (DateOrders)"]-df["order date (DateOrders)"]).dt.days

df = df.drop(columns=["Latitude", "Longitude", "Order Zipcode", "Product Description", "Customer Fname", "Customer Lname"])

# Save Cleaned Data
df.to_csv("./data/DataCoSupplyChainDataset_Cleaned_new.csv", index=False)