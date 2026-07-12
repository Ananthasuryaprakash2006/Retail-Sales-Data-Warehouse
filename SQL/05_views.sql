/********************************************************************************************
 Purpose:
Reusable SQL Views
********************************************************************************************/

USE RetailDW;
GO

/* Sales Summary View */

CREATE VIEW gold.vw_SalesSummary
AS

SELECT

d.Year,
d.Month_Name,

p.Category,

l.Region,

SUM(f.Sales) AS Sales,

SUM(f.Profit) AS Profit,

SUM(f.Quantity) AS Quantity

FROM gold.FactSales_Enterprise f

JOIN gold.DimDate_Enterprise d
ON f.DateKey=d.DateKey

JOIN gold.DimProduct_Enterprise p
ON f.ProductKey=p.ProductKey

JOIN gold.DimLocation_Enterprise l
ON f.LocationKey=l.LocationKey

GROUP BY

d.Year,
d.Month_Name,
p.Category,
l.Region;
GO

/* Test View */

SELECT *
FROM gold.vw_SalesSummary;
GO