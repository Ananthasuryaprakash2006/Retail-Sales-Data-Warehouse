import pandas as pd
from sqlalchemy import create_engine
import urllib
import sys

# Enable UTF-8 output
sys.stdout.reconfigure(encoding="utf-8")

# ======================================
# SQL Server Configuration
# ======================================

SERVER = r"SURYA\SQLEXPRESS"
DATABASE = "RetailDW"

params = urllib.parse.quote_plus(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE};"
    "Trusted_Connection=yes;"
)

engine = create_engine(
    f"mssql+pyodbc:///?odbc_connect={params}"
)

# ======================================
# Read Bronze Table
# ======================================

df = pd.read_sql("SELECT * FROM bronze.superstore_raw", engine)

print("Bronze Layer Read Successfully!")
print(f"Rows : {len(df)}")

# ======================================
# Rename Columns
# ======================================

df.rename(columns={
    "Customer.ID": "Customer_ID",
    "Customer.Name": "Customer_Name",
    "Order.Date": "Order_Date",
    "Order.ID": "Order_ID",
    "Order.Priority": "Order_Priority",
    "Product.ID": "Product_ID",
    "Product.Name": "Product_Name",
    "Ship.Date": "Ship_Date",
    "Ship.Mode": "Ship_Mode",
    "Shipping.Cost": "Shipping_Cost",
    "Sub.Category": "Sub_Category",
    "Row.ID": "Row_ID",
    "记录数": "Record_Count"
}, inplace=True)

print("Columns Renamed Successfully!")

# ======================================
# Convert Date Columns
# ======================================

df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["Ship_Date"] = pd.to_datetime(df["Ship_Date"])

print("Date Columns Converted!")

# ======================================
# Remove Duplicates
# ======================================

before = len(df)

df.drop_duplicates(inplace=True)

after = len(df)

print(f"Duplicates Removed : {before - after}")

# ======================================
# Load into Silver Layer
# ======================================

print("Loading into silver.superstore_clean...")

df.to_sql(
    name="superstore_clean",
    schema="silver",
    con=engine,
    if_exists="replace",
    index=False,
    chunksize=1000
)

print("Silver Layer Created Successfully!")

print("\nFinal Shape:", df.shape)