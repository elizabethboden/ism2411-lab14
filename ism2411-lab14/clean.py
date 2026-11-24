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
