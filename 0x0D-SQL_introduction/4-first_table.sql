--  a script to create a table in the current database
-- It creates the table only if the table doesn't already exist

CREATE TABLE IF NOT EXISTS first_table (
       id INT,
       name VARCHAR(256)
 );
