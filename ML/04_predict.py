import pandas as pd
import joblib
import os

print("=" * 60)
print("Retail Sales Demand Forecasting")
print("Step 4 : Weekly Sales Prediction")
print("=" * 60)

# ======================================
# Paths
# ======================================

BASE_PATH = r"C:\Users\surya\OneDrive\Desktop\Retail-Sales-Data-Warehouse\data\Raw\Walmart Sales Forecast"

TEST_PATH = os.path.join(BASE_PATH, "test.csv")

MODEL_PATH = r"C:\Users\surya\OneDrive\Desktop\Retail-Sales-Data-Warehouse\ML\model\retail_sales_model.pkl"

OUTPUT_PATH = r"C:\Users\surya\OneDrive\Desktop\Retail-Sales-Data-Warehouse\ML\predicted_sales.csv"

# ======================================
# Load Test Dataset
# ======================================

test = pd.read_csv(TEST_PATH)

print("\nTest Dataset Loaded Successfully!")
print("Rows :", len(test))
print("Columns :", len(test.columns))

# ======================================
# Load Features Dataset
# ======================================

features = pd.read_csv(
    os.path.join(BASE_PATH, "features.csv")
)

stores = pd.read_csv(
    os.path.join(BASE_PATH, "stores.csv")
)

# ======================================
# Merge Datasets
# ======================================

df = pd.merge(
    test,
    features,
    on=["Store", "Date", "IsHoliday"],
    how="left"
)

df = pd.merge(
    df,
    stores,
    on="Store",
    how="left"
)

print("\nDatasets Merged Successfully!")

# ======================================
# Handle Missing Values
# ======================================

markdown_cols = [
    "MarkDown1",
    "MarkDown2",
    "MarkDown3",
    "MarkDown4",
    "MarkDown5"
]

df[markdown_cols] = df[markdown_cols].fillna(0)

# ======================================
# Date Features
# ======================================

df["Date"] = pd.to_datetime(df["Date"])

df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Week"] = df["Date"].dt.isocalendar().week.astype(int)

# ======================================
# Encode Columns
# ======================================

df["IsHoliday"] = df["IsHoliday"].astype(int)
df["Type"] = df["Type"].astype("category").cat.codes

# ======================================
# Features
# ======================================

X = df[
    [
        "Store",
        "Dept",
        "IsHoliday",
        "Temperature",
        "Fuel_Price",
        "CPI",
        "Unemployment",
        "Size",
        "Type",
        "Year",
        "Month",
        "Week"
    ]
]

# ======================================
# Load Model
# ======================================

model = joblib.load(MODEL_PATH)

print("\nModel Loaded Successfully!")

# ======================================
# Predict
# ======================================

predictions = model.predict(X)

df["Predicted_Weekly_Sales"] = predictions

print("\nPrediction Completed!")

# ======================================
# Save Predictions
# ======================================

df.to_csv(
    OUTPUT_PATH,
    index=False
)

print("\nPrediction File Saved Successfully!")

print("\nLocation")
print(OUTPUT_PATH)

print("\nFirst 10 Predictions")

print(
    df[
        [
            "Store",
            "Dept",
            "Date",
            "Predicted_Weekly_Sales"
        ]
    ].head(10)
)

print("\n" + "=" * 60)
print("Machine Learning Pipeline Completed Successfully!")
print("=" * 60)