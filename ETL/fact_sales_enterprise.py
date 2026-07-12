import pandas as pd
from sqlalchemy import create_engine
import urllib
import sys

# Enable UTF-8
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
# Read Silver Table
# ======================================

silver = pd.read_sql(
    "SELECT * FROM silver.superstore_clean",
    engine
)

print("✅ Silver Layer Loaded")

# ======================================
# Read Enterprise Dimensions
# ======================================

dim_customer = pd.read_sql(
    "SELECT * FROM gold.DimCustomer_Enterprise",
    engine
)

dim_product = pd.read_sql(
    "SELECT * FROM gold.DimProduct_Enterprise",
    engine
)

dim_location = pd.read_sql(
    "SELECT * FROM gold.DimLocation_Enterprise",
    engine
)

dim_date = pd.read_sql(
    "SELECT * FROM gold.DimDate_Enterprise",
    engine
)

print("✅ Enterprise Dimension Tables Loaded")

print("\nRows")
print("Silver :", len(silver))
print("Customer :", len(dim_customer))
print("Product :", len(dim_product))
print("Location :", len(dim_location))
print("Date :", len(dim_date))

# ======================================
# Customer Mapping
# ======================================

fact = silver.merge(
    dim_customer[
        [
            "CustomerKey",
            "Customer_ID"
        ]
    ],
    on="Customer_ID",
    how="left"
)

print("\n✅ CustomerKey Mapped")

# ======================================
# Product Mapping
# ======================================

fact = fact.merge(
    dim_product[
        [
            "ProductKey",
            "Product_ID"
        ]
    ],
    on="Product_ID",
    how="left"
)

print("✅ ProductKey Mapped")

# ======================================
# Location Mapping
# ======================================

fact = fact.merge(
    dim_location[
        [
            "LocationKey",
            "Country",
            "Market",
            "Market2",
            "Region",
            "State",
            "City"
        ]
    ],
    on=[
        "Country",
        "Market",
        "Market2",
        "Region",
        "State",
        "City"
    ],
    how="left"
)

print("✅ LocationKey Mapped")

# ======================================
# Date Mapping
# ======================================

fact = fact.merge(
    dim_date[
        [
            "DateKey",
            "Date"
        ]
    ],
    left_on="Order_Date",
    right_on="Date",
    how="left"
)

print("✅ DateKey Mapped")

# ======================================
# Keep only Fact Table Columns
# ======================================

fact = fact[
    [
        "CustomerKey",
        "ProductKey",
        "LocationKey",
        "DateKey",
        "Order_ID",
        "Sales",
        "Quantity",
        "Discount",
        "Profit",
        "Shipping_Cost"
    ]
]

print("\nFact Table Preview")
print(fact.head())

print("\nFinal Rows :", len(fact))

# ======================================
# Load into SQL Server
# ======================================

fact.to_sql(
    name="FactSales_Enterprise",
    schema="gold",
    con=engine,
    if_exists="replace",
    index=False,
    chunksize=1000
)

print("\n✅ FactSales_Enterprise Loaded Successfully!")