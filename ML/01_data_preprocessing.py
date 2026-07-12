import pandas as pd
import os

print("=" * 60)
print("Retail Sales Demand Forecasting")
print("Step 1 : Data Preprocessing")
print("=" * 60)

# ======================================
# Dataset Paths
# ======================================

BASE_PATH = r"C:\Users\surya\OneDrive\Desktop\Retail-Sales-Data-Warehouse\data\Raw\Walmart Sales Forecast"

train_path = os.path.join(BASE_PATH, "train.csv")
features_path = os.path.join(BASE_PATH, "features.csv")
stores_path = os.path.join(BASE_PATH, "stores.csv")

# ======================================
# Read CSV Files
# ======================================

train = pd.read_csv(train_path)
features = pd.read_csv(features_path)
stores = pd.read_csv(stores_path)

print("\nDatasets Loaded Successfully!")

print("\nTrain Shape :", train.shape)
print("Features Shape :", features.shape)
print("Stores Shape :", stores.shape)

# ======================================
# Merge Train + Features
# ======================================

df = pd.merge(
    train,
    features,
    on=["Store", "Date", "IsHoliday"],
    how="left"
)

print("\nTrain + Features Merged")
print("Shape :", df.shape)

# ======================================
# Merge Stores
# ======================================

df = pd.merge(
    df,
    stores,
    on="Store",
    how="left"
)

print("\nStores Merged")
print("Final Shape :", df.shape)

# ======================================
# Convert Date
# ======================================

df["Date"] = pd.to_datetime(df["Date"])

print("\nDate Converted Successfully!")

# ======================================
# Missing Values
# ======================================

print("\nMissing Values")

print(df.isnull().sum())

# ======================================
# Dataset Information
# ======================================

print("\nDataset Information")

print(df.info())

# ======================================
# First Five Rows
# ======================================

print("\nFirst Five Rows")

print(df.head())

# ======================================
# Save Clean Dataset
# ======================================

OUTPUT_PATH = r"C:\Users\surya\OneDrive\Desktop\Retail-Sales-Data-Warehouse\ML\cleaned_sales_data.csv"

df.to_csv(
    OUTPUT_PATH,
    index=False
)

print("\nClean Dataset Saved Successfully!")

print("\nLocation")

print(OUTPUT_PATH)

print("\n" + "=" * 60)
print("Step 1 Completed Successfully")
print("=" * 60)