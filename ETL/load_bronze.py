import pandas as pd
from sqlalchemy import create_engine
import urllib

# ------------------------------------
# SQL Server Configuration
# ------------------------------------
SERVER = r"SURYA\SQLEXPRESS"
DATABASE = "RetailDW"

CSV_PATH = r"C:\Users\surya\OneDrive\Desktop\Retail-Sales-Data-Warehouse\data\Raw\Global Superstore Dataset\superstore.csv"

# ------------------------------------
# Read CSV
# ------------------------------------
df = pd.read_csv(CSV_PATH)

print("CSV Loaded Successfully")
print(f"Rows : {len(df)}")
print(f"Columns : {len(df.columns)}")

# ------------------------------------
# Connect to SQL Server
# ------------------------------------
params = urllib.parse.quote_plus(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE};"
    "Trusted_Connection=yes;"
)

engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

print("Connected to SQL Server Successfully!")

# ------------------------------------
# Load Data into Bronze Layer
# ------------------------------------
print("Loading data into bronze.superstore_raw...")

df.to_sql(
    name="superstore_raw",
    schema="bronze",
    con=engine,
    if_exists="replace",
    index=False,
    chunksize=1000
)

print("Data Loaded Successfully into bronze.superstore_raw")