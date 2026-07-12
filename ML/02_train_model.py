import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
import os

print("=" * 60)
print("Retail Sales Demand Forecasting")
print("Step 2 : Model Training")
print("=" * 60)

# ======================================
# Load Clean Dataset
# ======================================

DATA_PATH = r"C:\Users\surya\OneDrive\Desktop\Retail-Sales-Data-Warehouse\ML\cleaned_sales_data.csv"

df = pd.read_csv(DATA_PATH)

print("\nDataset Loaded Successfully!")
print("Rows :", len(df))
print("Columns :", len(df.columns))

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
# Convert Date
# ======================================

df["Date"] = pd.to_datetime(df["Date"])

df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Week"] = df["Date"].dt.isocalendar().week.astype(int)

# ======================================
# Convert Categorical Data
# ======================================

df["IsHoliday"] = df["IsHoliday"].astype(int)
df["Type"] = df["Type"].astype("category").cat.codes

# ======================================
# Features and Target
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

print("\nFeatures Selected :", X.shape[1])

# ======================================
# Train-Test Split
# ======================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training Rows :", len(X_train))
print("Testing Rows :", len(X_test))

# ======================================
# Train Random Forest
# ======================================

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

print("\nModel Trained Successfully!")

# ======================================
# Prediction
# ======================================

pred = model.predict(X_test)

# ======================================
# Evaluation
# ======================================

mae = mean_absolute_error(y_test, pred)
rmse = mean_squared_error(y_test, pred) ** 0.5
r2 = r2_score(y_test, pred)

print("\nModel Performance")
print("MAE  :", round(mae, 2))
print("RMSE :", round(rmse, 2))
print("R2   :", round(r2, 4))

# ======================================
# Save Model
# ======================================

MODEL_DIR = r"C:\Users\surya\OneDrive\Desktop\Retail-Sales-Data-Warehouse\ML\model"

os.makedirs(MODEL_DIR, exist_ok=True)

MODEL_PATH = os.path.join(MODEL_DIR, "retail_sales_model.pkl")

joblib.dump(model, MODEL_PATH)

print("\nModel Saved Successfully!")
print(MODEL_PATH)

print("\n" + "=" * 60)
print("Step 2 Completed Successfully")
print("=" * 60)