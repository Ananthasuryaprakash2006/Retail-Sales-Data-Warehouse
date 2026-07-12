/********************************************************************************************
 Project  : Retail Sales Data Warehouse with Machine Learning-Based Demand Forecasting
 File     : 01_database_setup.sql

 Purpose  :
 Creates the Retail Data Warehouse database and the Medallion Architecture schemas.

 Schemas
 --------
 bronze -> Raw Data
 silver -> Cleaned Data
 gold   -> Star Schema & Analytics
********************************************************************************************/

CREATE DATABASE RetailDW;
GO

USE RetailDW;
GO

CREATE SCHEMA bronze;
GO

CREATE SCHEMA silver;
GO

CREATE SCHEMA gold;
GO

/********************************************************************************************
 Verify Schemas
********************************************************************************************/

SELECT name
FROM sys.schemas
ORDER BY name;
GO