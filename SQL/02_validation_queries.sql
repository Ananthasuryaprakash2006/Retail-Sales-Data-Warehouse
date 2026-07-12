/********************************************************************************************
 Project  : Retail Sales Data Warehouse with Machine Learning-Based Demand Forecasting
 File     : 02_validation_queries.sql
 Author   : Surya Prakash
 Purpose  : Validate the Data Warehouse after ETL execution.
            These queries help verify that data has been loaded correctly and that
            there are no duplicate business keys in the dimension tables.
********************************************************************************************/

USE RetailDW;
GO

/********************************************************************************************
 Query 1 : Verify Bronze Layer Row Count

 Why?
 ----
 The Bronze layer stores the raw data imported from the CSV file without any changes.
 This query confirms that all records were loaded successfully.

 Expected Result:
 ----------------
 51290 rows
********************************************************************************************/

SELECT COUNT(*) AS TotalRows
FROM bronze.superstore_raw;
GO


/********************************************************************************************
 Query 2 : Verify Silver Layer Row Count

 Why?
 ----
 The Silver layer stores cleaned and transformed data.
 The row count should remain the same unless invalid or duplicate records were removed.

 Expected Result:
 ----------------
 51290 rows
********************************************************************************************/

SELECT COUNT(*) AS TotalRows
FROM silver.superstore_clean;
GO


/********************************************************************************************
 Query 3 : Check for Duplicate Dates

 Why?
 ----
 Each date should appear only once in DimDate_Enterprise.
 Duplicate dates will cause multiple matches during Fact Table creation.

 Expected Result:
 ----------------
 No rows returned.
********************************************************************************************/

SELECT
    Date,
    COUNT(*) AS DuplicateCount
FROM gold.DimDate_Enterprise
GROUP BY Date
HAVING COUNT(*) > 1;
GO


/********************************************************************************************
 Query 4 : Check for Duplicate Customers

 Why?
 ----
 Every Customer_ID should be unique.
 Duplicate customer IDs will create duplicate fact records during joins.

 Expected Result:
 ----------------
 No rows returned.
********************************************************************************************/

SELECT
    Customer_ID,
    COUNT(*) AS DuplicateCount
FROM gold.DimCustomer_Enterprise
GROUP BY Customer_ID
HAVING COUNT(*) > 1;
GO


/********************************************************************************************
 Query 5 : Check for Duplicate Products

 Why?
 ----
 Every Product_ID should be unique.
 Duplicate Product_ID values create duplicate mappings in the Fact Table.

 Expected Result:
 ----------------
 No rows returned.
********************************************************************************************/

SELECT
    Product_ID,
    COUNT(*) AS DuplicateCount
FROM gold.DimProduct_Enterprise
GROUP BY Product_ID
HAVING COUNT(*) > 1;
GO


/********************************************************************************************
 Query 6 : Check for Duplicate Locations

 Why?
 ----
 Each location should be unique based on:
 Country + Market + Market2 + Region + State + City

 Duplicate locations will cause one sales record to match multiple location records.

 Expected Result:
 ----------------
 No rows returned.
********************************************************************************************/

SELECT
    Country,
    Market,
    Market2,
    Region,
    State,
    City,
    COUNT(*) AS DuplicateCount
FROM gold.DimLocation_Enterprise
GROUP BY
    Country,
    Market,
    Market2,
    Region,
    State,
    City
HAVING COUNT(*) > 1;
GO


/********************************************************************************************
 Query 7 : Verify Enterprise Fact Table Row Count

 Why?
 ----
 The Fact Table should contain exactly the same number of rows as the Silver layer.
 This confirms that every sales record was mapped correctly without duplication or loss.

 Expected Result:
 ----------------
 51290 rows
********************************************************************************************/

SELECT COUNT(*) AS TotalRows
FROM gold.FactSales_Enterprise;
GO


/********************************************************************************************
 Validation Summary

 Bronze Layer              : 51290 rows
 Silver Layer              : 51290 rows
 FactSales Enterprise      : 51290 rows

 Duplicate Customer IDs    : 0
 Duplicate Product IDs     : 0
 Duplicate Location Keys   : 0
 Duplicate Dates           : 0

 If all expected results match, the Enterprise Data Warehouse has been
 successfully validated and is ready for SQL Analytics, Power BI, and
 Machine Learning.
********************************************************************************************/