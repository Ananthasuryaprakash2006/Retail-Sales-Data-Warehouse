import pandas as pd
from sqlalchemy import create_engine
import urllib
import sys

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
# Read Silver Layer
# ======================================

df = pd.read_sql(
    "SELECT * FROM silver.superstore_clean",
    engine
)

print("=" * 60)
print("Silver Layer Loaded Successfully!")
print("=" * 60)

# ======================================
# Enterprise Customer Dimension
# ======================================

dim_customer = (
    df[
        [
            "Customer_ID",
            "Customer_Name",
            "Segment"
        ]
    ]
    .sort_values("Customer_ID")
    .drop_duplicates(subset=["Customer_ID"], keep="first")
    .reset_index(drop=True)
)

dim_customer.insert(0, "CustomerKey", range(1, len(dim_customer) + 1))

dim_customer.to_sql(
    "DimCustomer_Enterprise",
    engine,
    schema="gold",
    if_exists="replace",
    index=False
)

print("✅ DimCustomer_Enterprise Created")
print("Customers :", len(dim_customer))

# ======================================
# Enterprise Product Dimension
# ======================================

dim_product = (
    df[
        [
            "Product_ID",
            "Product_Name",
            "Category",
            "Sub_Category"
        ]
    ]
    .sort_values("Product_ID")
    .drop_duplicates(subset=["Product_ID"], keep="first")
    .reset_index(drop=True)
)

dim_product.insert(0, "ProductKey", range(1, len(dim_product) + 1))

dim_product.to_sql(
    "DimProduct_Enterprise",
    engine,
    schema="gold",
    if_exists="replace",
    index=False
)

print("✅ DimProduct_Enterprise Created")
print("Products :", len(dim_product))

# ======================================
# Enterprise Location Dimension
# ======================================

dim_location = (
    df[
        [
            "Country",
            "Market",
            "Market2",
            "Region",
            "State",
            "City"
        ]
    ]
    .drop_duplicates(
        subset=[
            "Country",
            "Market",
            "Market2",
            "Region",
            "State",
            "City"
        ]
    )
    .reset_index(drop=True)
)

dim_location.insert(0, "LocationKey", range(1, len(dim_location) + 1))

dim_location.to_sql(
    "DimLocation_Enterprise",
    engine,
    schema="gold",
    if_exists="replace",
    index=False
)

print("✅ DimLocation_Enterprise Created")
print("Locations :", len(dim_location))

# ======================================
# Enterprise Date Dimension
# ======================================

dim_date = (
    df[
        ["Order_Date"]
    ]
    .drop_duplicates(subset=["Order_Date"])
    .reset_index(drop=True)
)

dim_date.rename(
    columns={
        "Order_Date": "Date"
    },
    inplace=True
)

dim_date.insert(0, "DateKey", range(1, len(dim_date) + 1))

dim_date["Day"] = dim_date["Date"].dt.day
dim_date["Month"] = dim_date["Date"].dt.month
dim_date["Month_Name"] = dim_date["Date"].dt.month_name()
dim_date["Quarter"] = dim_date["Date"].dt.quarter
dim_date["Year"] = dim_date["Date"].dt.year
dim_date["Week_Number"] = dim_date["Date"].dt.isocalendar().week.astype(int)
dim_date["Day_Name"] = dim_date["Date"].dt.day_name()

dim_date.to_sql(
    "DimDate_Enterprise",
    engine,
    schema="gold",
    if_exists="replace",
    index=False
)

print("✅ DimDate_Enterprise Created")
print("Dates :", len(dim_date))

print("\n" + "=" * 60)
print("Enterprise Star Schema Dimensions Completed Successfully!")
print("=" * 60)