print("---Exercise 1---")
import pandas as pd
df = pd.read_csv("data/messy_sales.csv")
print(df.info())
print(df.isnull().sum())
# Column Order ID has 31 missing values 
# Column Unit Price is stored as a string but should be a float
# Column Customer ID has 362 missing values

print("---Exercise 2---")
df.columns = df.columns.str.lower().str.replace(" ", "_")
print(df.columns.tolist())

print("---Exercise 3---")
# Print the original shape 
print("Shape before:", df.shape)
# Drop rows that are missing an order ID or date because we need these to identify each sale
df = df.dropna(subset=["order_id", "order_date"])
# Fill missing quantities with the column mean so we don't have to remove those sales 
df["quantity_sold"] = df["quantity_sold"].fillna(df["quantity_sold"].mean())
# Print the shape after cleaning 
print("Shape after:", df.shape)
# Check for missing values 
print(df.isnull().sum())

print("---Exercise 4---")
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
print("Dates that became NaT:", df["order_date"].isnull().sum())
df["unit_price"] = df["unit_price"].str.replace("$", "", regex=False).str.replace(",", "", regex=False)
df["unit_price"] = df["unit_price"].astype(float)
df["quantity_sold"] = df["quantity_sold"].astype(int)
df["revenue"] = (df["unit_price"] * df["quantity_sold"]).round(2)
print(df.dtypes) 
