/********************************************************************************************
 Purpose:
Improve data integrity and query performance.
********************************************************************************************/

USE RetailDW;
GO

/* Primary Keys */

ALTER TABLE gold.DimCustomer_Enterprise
ADD CONSTRAINT PK_DimCustomer PRIMARY KEY(CustomerKey);

ALTER TABLE gold.DimProduct_Enterprise
ADD CONSTRAINT PK_DimProduct PRIMARY KEY(ProductKey);

ALTER TABLE gold.DimLocation_Enterprise
ADD CONSTRAINT PK_DimLocation PRIMARY KEY(LocationKey);

ALTER TABLE gold.DimDate_Enterprise
ADD CONSTRAINT PK_DimDate PRIMARY KEY(DateKey);

/* Useful Indexes */

CREATE INDEX IX_FactSales_Customer
ON gold.FactSales_Enterprise(CustomerKey);

CREATE INDEX IX_FactSales_Product
ON gold.FactSales_Enterprise(ProductKey);

CREATE INDEX IX_FactSales_Date
ON gold.FactSales_Enterprise(DateKey);