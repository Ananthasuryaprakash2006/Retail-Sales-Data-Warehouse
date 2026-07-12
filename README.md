Retail Sales Data Warehouse with Machine Learning-Based Demand Forecasting
## 📖 About the Project

The **Retail Sales Data Warehouse with Machine Learning-Based Demand Forecasting** is an end-to-end data engineering and analytics project that transforms raw retail sales data into meaningful business insights and future sales predictions.

The project follows the **Medallion Architecture (Bronze, Silver, and Gold)** to build a scalable data warehouse using **Microsoft SQL Server**. Raw retail datasets are extracted from CSV files, cleaned and transformed through Python-based ETL pipelines, and modeled into an **Enterprise Star Schema** for efficient reporting and analytics.

Interactive dashboards are developed in **Microsoft Power BI** to visualize key business metrics, including sales performance, customer behavior, product analysis, and regional trends. Additionally, a **Random Forest Regression** machine learning model is implemented to forecast future weekly sales, enabling data-driven business decisions.

This project demonstrates practical implementation of **Data Engineering, ETL Pipelines, Data Warehousing, Business Intelligence, SQL Development, and Machine Learning**, making it a comprehensive portfolio project for aspiring Data Engineers and Data Analysts.

---
## 🏗️ Project Architecture

The **Retail Sales Data Warehouse with Machine Learning-Based Demand Forecasting** follows a modern end-to-end data engineering architecture that integrates data ingestion, ETL processing, data warehousing, business intelligence, and machine learning to support data-driven business decisions.

The architecture begins with retail sales datasets collected from the **Global Superstore** and **Walmart Sales Forecast** datasets in CSV format. A Python-based ETL pipeline extracts, cleans, transforms, and loads the data into a SQL Server data warehouse following the **Medallion Architecture**

<p align="center">
  <img src=<img width="1536" height="1024" alt="Retail sales data warehouse architecture" src="https://github.com/user-attachments/assets/2ffdf7cd-7bb5-43de-9fe5-87de75d04d7c" />
>
</p>
The data warehouse is organized into three layers:

- **Bronze Layer** stores raw data exactly as received from the source systems.
- **Silver Layer** performs data cleansing, validation, standardization, and transformation to improve data quality.
- **Gold Layer** contains business-ready data modeled as an **Enterprise Star Schema** with fact and dimension tables optimized for analytics and reporting.

The processed data is then utilized by two major components:

- **Power BI Dashboards** provide interactive visualizations for executive reporting, customer and product analytics, regional sales analysis, and business performance monitoring.
- **Machine Learning Pipeline** applies a Random Forest Regression model to preprocess data, train and evaluate the model, and generate future weekly sales forecasts.

This architecture enables efficient data processing, scalable analytics, accurate forecasting, and meaningful business insights, supporting strategic decision-making across retail operations.
---
## 📖 Project Overview

The **Retail Sales Data Warehouse with Machine Learning-Based Demand Forecasting** is an end-to-end Data Engineering project that integrates **SQL Server, Python, Power BI, and Machine Learning** to transform raw retail sales data into valuable business insights and accurate sales forecasts.

The project implements the **Medallion Architecture (Bronze, Silver, and Gold)**, develops Python-based ETL pipelines, designs an **Enterprise Star Schema**, and creates interactive **Power BI dashboards** for business analytics. A **Random Forest Regression** model is used to predict future weekly sales, enabling data-driven decision-making.

This project demonstrates practical skills in **Data Engineering, ETL Development, Data Warehousing, SQL, Business Intelligence, Power BI, and Machine Learning**.
---
## 🛠️ Important Links & Tools

The following tools, datasets, and technologies were used to build this project.

| 📊 Global Superstore Dataset | https://www.kaggle.com/datasets/vivek468/superstore-dataset-final |
| 🛒 Walmart Sales Forecast Dataset | https://www.kaggle.com/datasets/aslanahmedov/walmart-sales-forecast |
| 🗄️ Microsoft SQL Server | https://www.microsoft.com/en-us/sql-server/sql-server-downloads |
| 💻 SQL Server Management Studio (SSMS) | https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms |
| 🐍 Python | https://www.python.org/ |
| 📦 Pandas | https://pandas.pydata.org/ |
| 🔢 NumPy | https://numpy.org/ |
| 🤖 Scikit-learn | https://scikit-learn.org/stable/ |
| 📈 Microsoft Power BI Desktop | https://powerbi.microsoft.com/desktop/ |
| 📒 Jupyter Notebook | https://jupyter.org/ |
| 🔀 Git | https://git-scm.com/ |
| 🌐 GitHub | https://github.com/ |
| 🎨 Draw.io | https://app.diagrams.net/ |
---
## 🚀 Project Requirements

### 🎯 Objective

The objective of this project is to design and develop a modern **Retail Sales Data Warehouse** that integrates retail sales data from multiple datasets into a centralized analytical platform. The project enables business intelligence reporting, sales analysis, and machine learning-based demand forecasting to support data-driven decision-making.

---

## 🚀 Project Requirements

### 📋 Functional Requirements

#### 🗂️ Data Sources
- Import retail sales data from CSV datasets.
- Use the **Global Superstore** and **Walmart Sales Forecast** datasets.

#### 🔄 ETL Pipeline
- Extract, transform, and load (ETL) retail sales data.
- Clean, validate, and standardize datasets.
- Load processed data into SQL Server.

#### 🏗️ Data Warehouse
- Implement the **Medallion Architecture** (Bronze, Silver, Gold).
- Build an **Enterprise Star Schema** with Fact and Dimension tables.

#### 📊 Business Intelligence
- Develop interactive **Power BI** dashboards for:
  - Executive Dashboard
  - Customer & Product Analytics
  - Regional Sales Analysis
  - Demand Forecasting

#### 🤖 Machine Learning
- Train a **Random Forest Regression** model.
- Forecast future weekly sales.
- Evaluate model performance using **MAE, RMSE, and R² Score**.

#### 📈 Business Analytics
Generate insights for:
- Sales & Profit Analysis
- Customer & Product Performance
- Regional & Category Analysis
- Sales Trends & Demand Forecasting

---

### 🎯 Expected Outcomes

- Modern Retail Sales Data Warehouse
- Automated Python ETL Pipeline
- Enterprise Star Schema
- Interactive Power BI Dashboards
- Machine Learning-Based Demand Forecasting
- Actionable Business Insights
---
## 📂 Repository Structure

```text
Retail-Sales-Data-Warehouse/
│
├── Dashboard/
│   ├── Retail_Sales_Dashboard.pbix
│   └── Dashboard_Designs/
│       ├── Page1_Executive_Dashboard.png
│       ├── Page2_Customer_Product_Analytics.png
│       ├── Page3_Regional_Analysis.png
│       └── Page4_ML_Forecasting.png
│
├── data/
│   └── Raw/
│       ├── Global Superstore Dataset/
│       │   └── superstore.csv
│       │
│       └── Walmart Sales Forecast/
│           ├── train.csv
│           ├── test.csv
│           ├── features.csv
│           └── stores.csv
│
├── ETL/
│   ├── load_bronze.py
│   ├── silver_etl.py
│   ├── gold_star_schema.py
│   └── fact_sales_enterprise.py
│
├── Images/
│   ├── Data_Warehouse_Architecture.png
│   ├── ETL_Pipeline.png
│   ├── Star_Schema.png
│   ├── PowerBI_Architecture.png
│   └── ML_Workflow.png
│
├── ML/
│   ├── 01_data_preprocessing.py
│   ├── 02_train_model.py
│   ├── 03_evaluate_model.py
│   ├── 04_predict.py
│   ├── cleaned_sales_data.csv
│   ├── predicted_sales.csv
│   └── model/
│       └── retail_sales_model.pkl
│
├── SQL/
│   ├── 01_database_setup.sql
│   ├── 02_validation_queries.sql
│   ├── 03_analytics_queries.sql
│   ├── 04_constraints.sql
│   └── 05_views.sql
│
├── README.md
├── LICENSE
└── requirements.txt
```
---
🛡️ License

This project is licensed under the MIT License. You are free to use, modify, and distribute this project with proper attribution.
---
## 👨‍💻 About Me

Hi, I'm **Anantha Surya Prakash Pullagura**, a B.Tech student in **Artificial Intelligence & Data Science** at **Koneru Lakshmaiah Education Foundation** with a strong interest in **Data Engineering, Data Warehousing, Business Intelligence, and Machine Learning**.

I enjoy designing scalable data pipelines, building modern data warehouses, developing ETL processes, and creating interactive dashboards that transform raw data into meaningful business insights.

### 🚀 Areas of Interest

- Data Engineering
- Data Warehousing
- ETL Pipeline Development
- SQL Development
- Data Modeling
- Business Intelligence (Power BI)
- Machine Learning
- Data Analytics

I'm continuously learning and building hands-on projects to strengthen my skills in data engineering and analytics. Feel free to explore this repository and connect with me for collaboration, learning, or feedback.

📧 **Email:** suryaprakashpullagura@gmail.com

🔗 **GitHub:** https://github.com/Ananthasuryaprakash2006

🔗 **LinkedIn:** https://www.linkedin.com/in/surya-prakash-pullagura-bb0a7b38b/
