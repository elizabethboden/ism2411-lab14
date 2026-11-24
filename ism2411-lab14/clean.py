# 1. I think filling in missing values is the hardest decision because the 
# average might not always be close to what the actual value was. I would
# want to know why the information was missing before deciding if using the 
# average was the best choice.
# 2. I think my comments explain why I made each decision. I dropped rows that
# were missing order IDs or dates because they are important for identifying and 
# tracking sales. I filled missing quantities with the average to avoid losing 
# entire sales records. I also removed duplicate rows and the 9,999 quantity because
# they did not represent valid sales records. 
# 3. I was surprised by how high the maximum revenue was compared to the median.
# The maximum was 59,994, while the median was only 145.49. I didn't expect there
# to be such a big difference between the two. 

print("---Exercise 1---")
import pandas as pd
df = pd.read_csv("data/messy_sales.csv")
print(df.info())
print(df.isnull().sum())
# Column Order ID has 0.65% missing values.
# Column Unit Price is dtype object but should be float because it contains prices.
# Column Customer ID has 7.54% missing values.

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

print("---Exercise 5---")
print("Number of duplicates:", df.duplicated().sum())
df = df.drop_duplicates()
print("Shape after removing duplicates:", df.shape)

print("---Exercise 6---")
print(df.describe())
# The negative revenue could represent customer returns, so I am keeping these rows
# The maximum revenue of 59,994 is much higher than the median of 145.49, possibly because of a large order
# Remove rows with a quantity of 9,999 because this is a placeholder, not a real sale
df = df[df["quantity_sold"] != 9999]
print("Shape after removing placeholder quantities:", df.shape)

print("---Exercise 7---")
df.to_csv("data/clean_sales.csv", index=False)
df = pd.read_csv("data/clean_sales.csv")
print(df.info())
df = pd.read_csv("data/clean_sales.csv", parse_dates=["order_date"])
print(df.info())