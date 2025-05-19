# Import Library
import pandas as pd

# Load Data
df = pd.read_csv("./data/DataCoSupplyChainDataset_Cleaned.csv")
print(df.head())

### Analyst Profit ###
# # Check by Category and Shipping Method
profit_cat = df.groupby(["Category Name", "Shipping Mode"])["Order Profit Per Order"].sum().sort_values(ascending=False).reset_index()
print(profit_cat)

# # Save Profit Analyst
# profit_cat.to_csv("./powerbi/ProfitAnalyst_Summary.csv", index=False)

# <------------------------------->

# ### Customer Segmentation ###
# Checking Correlation Between Sales per Customer and Profit
cust_seg = df.groupby("Customer Id")[["Sales per customer", "Order Profit Per Order"]].sum().reset_index()
print(cust_seg)

# Initiate Quantile
qt = [0.33, 0.66]

# Calculate Quantile
Sales_Seg = cust_seg["Sales per customer"].quantile(qt)
Profit_Seg = cust_seg["Order Profit Per Order"].quantile(qt)

# Make Segmentation Function
def seg_val(value, quantiles):
    if value <= quantiles[0.33]:
        return "Low"
    elif value <= quantiles[0.66]:
        return "Medium"
    return "High"

# Apply Segmentation Function
cust_seg["Sales Segment"] = cust_seg["Sales per customer"].apply(lambda x: seg_val(x, Sales_Seg))
cust_seg["Profit Segment"] = cust_seg["Order Profit Per Order"].apply(lambda x: seg_val(x, Profit_Seg))
print(cust_seg)


# # Save Customer Segmentation
# cust_seg.to_csv("./powerbi/CustomerSegmentation_Summary.csv", index=False)

# <------------------------------->

### Shipping Delay ###
# Delay by Region
delay_by_region = df.groupby("Order Region")["shipping delays (DateOrders)"].mean().sort_values().reset_index()
print(delay_by_region)

# Delay by Shipping Method
delay_by_mode = df.groupby("Shipping Mode")["shipping delays (DateOrders)"].mean().sort_values().reset_index()
print(delay_by_mode)

# # Save Shipping Delay
# shippingDelays_Summary = df.groupby(["Order Region", "Shipping Mode"])["shipping delays (DateOrders)"].mean().sort_values().reset_index()
# shippingDelays_Summary.to_csv("./powerbi/shippingDelays_Summary_Summary.csv", index=False)