import pandas as pd
import joblib
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

print("=" * 60)
print("Retail Sales Demand Forecasting")
print("Step 3 : Model Evaluation")
print("=" * 60)

# ======================================
# Load Dataset
# ======================================

DATA_PATH = r"C:\Users\surya\OneDrive\Desktop\Retail-Sales-Data-Warehouse\ML\cleaned_sales_data.csv"

df = pd.read_csv(DATA_PATH)

print("\nDataset Loaded Successfully!")

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
# Convert Categorical Columns
# ======================================

df["IsHoliday"] = df["IsHoliday"].astype(int)
df["Type"] = df["Type"].astype("category").cat.codes

# ======================================
# Features & Target
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

y = df["Weekly_Sales"]

# ======================================
# Load Saved Model
# ======================================

MODEL_PATH = r"C:\Users\surya\OneDrive\Desktop\Retail-Sales-Data-Warehouse\ML\model\retail_sales_model.pkl"

model = joblib.load(MODEL_PATH)

print("Model Loaded Successfully!")

# ======================================
# Predict
# ======================================

predictions = model.predict(X)

# ======================================
# Evaluate
# ======================================

mae = mean_absolute_error(y, predictions)
rmse = mean_squared_error(y, predictions) ** 0.5
r2 = r2_score(y, predictions)

print("\n========== MODEL PERFORMANCE ==========")
print(f"MAE  : {mae:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R²   : {r2:.4f}")

# ======================================
# Prediction Sample
# ======================================

results = pd.DataFrame({
    "Actual Sales": y.head(10),
    "Predicted Sales": predictions[:10]
})

print("\n========== SAMPLE PREDICTIONS ==========")
print(results)

print("\n" + "=" * 60)
print("Step 3 Completed Successfully")
print("=" * 60)