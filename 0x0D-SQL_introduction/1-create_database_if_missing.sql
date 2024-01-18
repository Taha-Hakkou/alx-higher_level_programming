-- 1-create_database_if_missing.sql
-- creates the database hbtn_0c_0 in your MySQL server if doesn't exist
IF NOT EXISTS(SELECT * FROM sys.databases WHERE name = 'DataBase')
  BEGIN
    CREATE DATABASE hbtn_0c_0
    
    USE DataBase
  END
