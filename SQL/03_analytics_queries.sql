/********************************************************************************************
 Project : Retail Sales Data Warehouse
 File    : 03_analytics_queries.sql

 Purpose :
 Business Intelligence Queries
********************************************************************************************/

USE RetailDW;
GO

/*--------------------------------------------------
1. Total Sales
Purpose:
Shows total revenue generated.
--------------------------------------------------*/

SELECT SUM(Sales) AS TotalSales
FROM gold.FactSales_Enterprise;
GO

/*--------------------------------------------------
2. Total Profit
Purpose:
Shows total business profit.
--------------------------------------------------*/

SELECT SUM(Profit) AS TotalProfit
FROM gold.FactSales_Enterprise;
GO

/*--------------------------------------------------
3. Total Quantity Sold
Purpose:
Shows total products sold.
--------------------------------------------------*/

SELECT SUM(Quantity) AS TotalQuantity
FROM gold.FactSales_Enterprise;
GO

/*--------------------------------------------------
4. Monthly Sales Trend
Purpose:
Analyze monthly business performance.
--------------------------------------------------*/

SELECT
d.Year,
d.Month,
d.Month_Name,
SUM(f.Sales) AS TotalSales
FROM gold.FactSales_Enterprise f
JOIN gold.DimDate_Enterprise d
ON f.DateKey=d.DateKey
GROUP BY
d.Year,
d.Month,
d.Month_Name
ORDER BY
d.Year,
d.Month;
GO

/*--------------------------------------------------
5. Top 10 Products
Purpose:
Find best-selling products.
--------------------------------------------------*/

SELECT TOP 10
p.Product_Name,
SUM(f.Sales) AS TotalSales
FROM gold.FactSales_Enterprise f
JOIN gold.DimProduct_Enterprise p
ON f.ProductKey=p.ProductKey
GROUP BY
p.Product_Name
ORDER BY TotalSales DESC;
GO

/*--------------------------------------------------
6. Top 10 Customers
Purpose:
Identify high-value customers.
--------------------------------------------------*/

SELECT TOP 10
c.Customer_Name,
SUM(f.Sales) AS TotalSales
FROM gold.FactSales_Enterprise f
JOIN gold.DimCustomer_Enterprise c
ON f.CustomerKey=c.CustomerKey
GROUP BY
c.Customer_Name
ORDER BY TotalSales DESC;
GO

/*--------------------------------------------------
7. Category-wise Sales
--------------------------------------------------*/

SELECT
p.Category,
SUM(f.Sales) AS Sales
FROM gold.FactSales_Enterprise f
JOIN gold.DimProduct_Enterprise p
ON f.ProductKey=p.ProductKey
GROUP BY
p.Category
ORDER BY Sales DESC;
GO

/*--------------------------------------------------
8. Region-wise Sales
--------------------------------------------------*/

SELECT
l.Region,
SUM(f.Sales) AS Sales
FROM gold.FactSales_Enterprise f
JOIN gold.DimLocation_Enterprise l
ON f.LocationKey=l.LocationKey
GROUP BY
l.Region
ORDER BY Sales DESC;
GO

/*--------------------------------------------------
9. Country-wise Sales
--------------------------------------------------*/

SELECT
l.Country,
SUM(f.Sales) AS Sales
FROM gold.FactSales_Enterprise f
JOIN gold.DimLocation_Enterprise l
ON f.LocationKey=l.LocationKey
GROUP BY
l.Country
ORDER BY Sales DESC;
GO

/*--------------------------------------------------
10. Average Order Value
--------------------------------------------------*/

SELECT
AVG(Sales) AS AverageOrderValue
FROM gold.FactSales_Enterprise;
GO