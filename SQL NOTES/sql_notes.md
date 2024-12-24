# How To Login MySQL as a root:-

- To **login** as a `root user` in Open Terminal and enter the following command.

  ```bash
  # In Linux
  sudo mysql -u root -p

  # In Windows
  mysql -u root -p
  ```

---

## Basic Important Commands :-

- `status` **:-** 👉 &nbsp;This command is used to show status of mysql server.
- `show databases` **:-** 👉 &nbsp;**This command is used to show all databases in our mysql server.**

- `use dataBaseName` **:-** 👉 &nbsp; **This command is used to select database.**

- `show tables` **:-** 👉 &nbsp; **This command is used to show tables from selected database.**
- `describe tableName` **:-** 👉 &nbsp; **It is used to show structure of selected database table content.**

- `\q` **:-** 👉 &nbsp; **It is used to exit from mysql datbase.**
- `exit` **:-** 👉 &nbsp; **It is also used to exit from mysql database.**

## How To Create a Database:-

- **`CREATE DATABASE databaseName ;`** 👉 &nbsp;This command is used **to create a database.**
- **`CREATE DATABASE databaseName IF NOT EXISTS ;`** 👉 &nbsp;This command is also used to **create a database if database is not exist.**
- **For Example :-** 👇

  ```sql
  CREATE DATABASE testdb;
  ```

## How To Delete a Database :-

- `DROP DATABASE databaseName;` 👉 This command is used **to delete a specified database.**

- `DROP DATABASE IF EXISTS databaseName;` 👉 This command is used **to delete a database if database exists.**
- **For Example:-** 👇

  ```sql
  DROP DATABASE testdb;

  ---- conditionally delete
  DROP DATABASE IF EXISTS testdb;

  ```

---

## How To Create a Table in a Database :-

- **Each row in a table is called record. record is a collection of fields / columns.**
- **Table (schema) definition can be described with columns in a table and asociated data type and also constraints.**
- **Syntax** 👇

  - **CREATE TABLE tableName(
    column1 dataType constraint,
    column2 dataType constraint,
    column3 dataType constraint,
    ........
    );**

  - **Constraints are optional.**

  - **For Example :-** 👇

  ```sql
  CREATE TABLE Employee(
      empid int,
      name varchar(255),
      age int,
      salary float
  );

  ```

- **If we not give any value of any column or field then default value of this column is** `NULL`.**When we not apply any constraint of that column.**

## How To Delete a Table in a Database :-

- **Syntax :-** 👉 &nbsp;**DROP TABLE tableName;**
- For Example :- 👇
  ```sql
  DROP TABLE Employee;
  ```

---

## SQL Constraints :-

1. **NOT NULL**
2. **UNIQUE**
3. **PRIMARY KEY**
4. **FOREIGN KEY**
5. **CHECK**
6. **DEFAULT**

   ### 1. NOT NULL :-

   - **By default** Column can hold `NULL` value.
   - **NOT NULL Constraints enforces a column will not accept NULL values.**
   - When we create a table we can enforce NOT NULL constraint. After creating a table, If we want to apply NOT NULL constraint then to do this we will have to ALTER that table but condition will be that field we want to apply NOT NULL constraint that field do not have NULL value already.

   - **Inserting a new record or updating a record without adding a value to a NOT NULL field is not possible.**
   - **If any field has NULL value and we want to apply NOT NULL Constraint on this field then it is not possible to do this first we will have to remove NULL value and then apply NOT NULL constraint.**

   ### How To add NOT NULL Constraint When We Create A Table :-

   - **Syntax :-** 👇

     ```text
     CREATE TABLE tableName(
     column1 dataType constraint,
     column2 dataType constraint,
     column3 dataType constraint,
     ......
     );

     ```

   - **For Example :-** 👇

     ```sql
     CREATE TABLE Employee(
         empid int,
         name varchar(255) NOT NULL,
         age int,
         salary float
     );

     ```

   ### How To add NOT NULL Constraint After Creating a Table :-

   ##### ALTER Table for NOT NULL :-

   - **Syntax :-** 👇

   ```text
   ALTER TABLE tableName MODIFY COLUMN columnName dataType NOT NULL;
   ```

   - **For Example :-** 👇

   ```sql

   ALTER TABLE Employee MODIFY COLUMN age int NOT NULL;

   ```

   ### How To Remove NOT NULL Constraint After Creating a Table :-

---

### 2. UNIQUE :-

#### When We Creating A Table :-

- **It ensures that all tables in a column are different.**
- **Syntax :-** 👇

```text
CREATE TABLE tableName(
    column1 dataType constraint,
    column2 dataType constraint,
    column3 dataType constraint,
    ......
    );

----- 2nd Syntax

CREATE TABLE tableName(
    column1 dataType ,
    column2 dataType ,
    column3 dataType ,
    UNIQUE (colname)
    ......
    );

----- Name Your Constraint

CREATE TABLE tableName(
    colname type,
    colname type,
    colname type,
    CONSTRAINT constraintName UNIQUE(col1,col2,.....)
);
```

- **Example :-** 👇

```sql
CREATE TABLE Employee(
    --- UNIQUE Constraint
    empid int UNIQUE,

    --- NOT NULL Constraint
    name varchar(255) NOT NULL,
    age int,
    salary float
);
```

#### How To Apply Constraint After Creating A Table :-

- **After Creating a Table we will have to ensure that field has no repeated value , In Simple terms we can say that field has already `UNIQUE` value except `NULL`.**

- **If that field has already repeated value then we will have to remove repeated value.**

- **Syntax :-** 👇

  ```text
  ALTER TABLE tableName
  ADD UNIQUE (colName);

  ----- Constraint Name
  ALTER TABLE tableName
  ADD CONSTRAINT constraintName UNIQUE(cols);


  ```

#### How To Delete Constraint After Creating A Table :-

- **Syntax :-** 👇
  ```text
  ALTER TABLE tableName
  DROP INDEX constraintName;
  ```

---

### 3. PRIMARY KEY :-

- The `PRIMARY KEY` **Constraint uniquely identifies each record in a table.**
- Field which is `PRIMARY KEY` must contain `UNIQUE` **values** and can not contain `NULL` **values.**
- A Table can have only one `PRIMARY KEY`, **PRIMARY KEY** can consist of **single or multiple fields.**

- **Syntax :-** 👇

```text
CREATE TABLE tableName(
    column1 dataType constraint,
    column2 dataType constraint,
    column3 dataType constraint,
    ......
    );

----- 2nd Syntax

CREATE TABLE tableName(
    column1 dataType ,
    column2 dataType ,
    column3 dataType ,
    PRIMARY KEY (colname)
    ......
    );

----- Name Your Constraint

CREATE TABLE tableName(
    colname type,
    colname type,
    colname type,
    CONSTRAINT constraintName PRIMARY KEY(col1,col2,.....)
);

```

- **For Example :-** 👇

```sql
CREATE TABLE Employee(
    --- PRIMARY KEY Constraint
    empid int PRIMARY KEY,

    --- NOT NULL Constraint
    name varchar(255) NOT NULL,
    age int,
    salary float
);
```

##### How To ADD PRIMARY KEY After Creating A Table :-

```text
ALTER TABLE tableName ADD PRIMARY KEY (colName);

------ 2nd Syntax
ALTER TABLE tableName ADD CONSTRAINT constraintName PRIMARY KEY(colName,colName,colName,.....);


```

##### How To DELETE PRIMARY KEY After Creating A Table :-

```text
------ Without Constraint Name
ALTER TABLE tableName DROP PRIMARY KEY;

------ 2nd Syntax (If Constraint Name then use this)
ALTER TABLE tableName DROP CONSTRAINT constraintName;
```

---

### 4. CHECK :-

- `CHECK` **constraint is used to limit the value in a range that can placed in a column.**
- **After Applying `CHECK` constraint that column will accept** `NULL` **value but not accept a value that will not satisfy of given conditions that we will apply.**

#### How To Apply CHECK CONSTRAINT When We Create A Table :-

- **Syntax :-** 👇

```text
CREATE TABLE tableName(
    column1 dataType constraint,
    column2 dataType constraint,
    column3 dataType constraint,
    ......
    CONSTRAINT constraintName CHECK (condition)
    );

---- 2nd method

CREATE TABLE tableName(
    column1 dataType constraint,
    column2 dataType constraint,
    column3 dataType constraint,
    ......
    CHECK (condition)
    );

```

For Example:-

```sql
CREATE TABLE Employee(
    --- PRIMARY KEY Constraint
    empid int PRIMARY KEY,

    --- NOT NULL Constraint
    name varchar(255) NOT NULL,
    age int,
    salary float,

    --- CHECK constraint
    CONSTRAINT c1 CHECK (age>=18)

);
```

#### How To Apply CHECK CONSTRAINT After Creating A Table :-

- If we apply `CHECK` `CONSTRAINT` **after creating a table on any field/column in a given table then that column values should be satisfied before that conditions we want to apply on that field/column.**

- **Syntax :-** 👇

```text
ALTER TABLE tableName ADD CONSTRAINT constraintName CHECK (conditions);

----- 2nd method
ALTER TABLE tableName ADD CHECK (conditions);
```

- **For Example :-** 👇

```sql
ALTER TABLE Employee ADD CONSTRAINT c1 CHECK (age>=18);

```

#### How To Delete CHECK CONSTRAINT In A Table :-

- **Syntax :-** 👇

```text
ALTER TABLE tableName DROP CHECK constraintName;

```

- **For Example :-** 👇

```sql
ALTER TABLE Employee DROP CHECK c1;

```

---

### 5. DEFAULT :-

- **The** `DEFAULT` **constraint is used to set a default value for a column.**
- **When we do not set default value it takes NULL values.**
- **When We create a new table by defult `DEFAULT` Constraint will be applied until unless if we don't specify any default.**

#### How To Apply CHECK CONSTRAINT When We Creating A Table :-

**Syntax :-** 👇

```txt
CREATE TABLE tableName(
    colName type,
    colName type,
    colName type DEFAULT value,
    .....
    );

```

**For Example :-** 👇

```sql
CREATE TABLE Employee(
   --- PRIMARY KEY Constraint
    empid int PRIMARY KEY,

    --- NOT NULL Constraint
    name varchar(255) NOT NULL,
    age int,

    --- DEFAULT Constraint
    salary float DEFAULT 10000,
    );
```

#### How To Apply CHECK CONSTRAINT After Creating A Table :-

**Syntax :-** 👇

```txt
ALTER TABLE tableName ALTER colName SET DEFAULT defaultValue;

```

**For Example :-** 👇

```sql
ALTER TABLE Employee ALTER salary SET DEFAULT 10000;
```

#### How To Delete DEFAULT CONSTRAINT In A Table :-

**Syntax :-** 👇

```txt
ALTER TABLE tableName ALTER columnName DROP DEFAULT;
```

**For Example :-** 👇

```sql
ALTER TABLE Employee ALTER salary DROP DEFAULT;
```

---

## Alter TABLE Command :-

- This command can be used to add, delete or modify columns in an existing table.
- It can be used to add and drop various constraints an on exitsting table.
- **Syntax :-** 👇

  ```sql
  ALTER TABLE tableName ADD columnName dataType;

  ---- To modify column dataType
  ALTER TABLE tableName MODIFY COLUMN columnName dataType;

  ----- To Rename a column
  ALTER TABLE tableName RENAME COLUMN oldColumnName TO newColumnName;
  ```

### How To Delete a column :-

- **Syntax :-** 👇

  ```sql
  ALTER TABLE tableName DROP COLUMN columnName;
  ```

---

## INSERT Command :-

### How To INSERT A New Record In A Table:-

- This command is used to insert a new record into the specified Table.

- **Specify both column name and values to be inserted.**

- **Syntax :-** 👇
  ```sql
  INSERT INTO tableName (col1,col2,col3,.....) VALUES (value1,value2,value3,.....);
  ```
- **If We are adding values for all the columns of the table, we do not need to specify the column names in the SQL query. However, make sure the order of the values is in the same order as the columns in the table.**
- **Syntax :-** 👇

  ```sql
  INSERT INTO tableName VALUES (value1,value2,value3,.....);
  ```

- **It is not necessary to insert data for all the columns.When lesser columns are specified remaining columns will have either default values or NULL.**

- **For Exmple :-** 👇

  ```sql
  ----- To insert data in a table with column Name and values.
  insert into Employee (empid,name,age,department,salary) values(10,'Manav',24,'Tech',45000);

  ---- To insert record in a table without column name but order wiil be same that will be in table.
  insert into Employee Values(9,'Master',52,50000,'HR');
  ```

---

## How To Update A Record :-

- **The** `UPDATE` **statement is used to modify the existing records in a table.**

- **Syntax :-** 👇

  ```sql
  UPDATE tableName SET column1=value1, column2=value2,column3=value3,...... where condition;
  ```

- **For Example :-** 👇

  ```sql
  update Employee set department='HR' where name='Mukesh';
  ```

> **Note :-** Be careful when updating a records in a table we should add `WHERE` clause in the UPDATE statement. `WHERE` clause specify which record or records should be updated. If we omit/skip `WHERE` clause all records will be updated.

---

## SELECT Command :-

- `SELECT` command is used to select data from a database.
- **Syntax** 👇
  ```sql
  SELECT col1,col2,col3,..... FROM tableName;
  ```
- **Here `col1`,`col2`,`col3` are the field(column) name of the table in which we want to select data.**

#### How To SELECT All Data From a Database :-

- **If we want to Select all rows and columns then we will use the following command :-**
- **Syntax** 👇
  ```sql
  SELECT * FROM tableName;
  ```

#### How To SELECT Specified Columns And All Rows :-

- **If we want to select specific and all rows then we will use the following command :-**
- This gives result specified column in which we specify column.

- **Syntax** 👇
  ```sql
  SELECT col1,col2,col3,..... FROM tableName;
  ```

#### Select All Columns and Specified Rows :-

- **If we want to select specified rows then we will have to use `WHERE` clause.**
- **Syntax** 👇
  ```sql
  SELECT * FROM tableName WHERE condition;
  ```

### How To Select Different Values In a Table :-

---

## 🌟 SQL Aggregate Functions :-

- **An Aggregate function is a function that performs calculations on a set of values, and returns a single value.**
- Most commonly SQL Aggregate functions are :-
  1. &nbsp; **`COUNT()`**
  2. &nbsp; **`MIN()`**
  3. &nbsp; **`MAX()`**
  4. &nbsp; **`AVG()`**
  5. &nbsp; **`SUM()`**

1. `COUNT()` :- 👉 This function returns the number of rows that matches the specified criteria.

   - **Syntax :-** 👇
     ```SQL
     SELECT COUNT(column_name) FROM table_name WHERE condition;
     ```
   - **Example :-** 👇
     ```SQL
     SELECT COUNT(*) AS All_Products FROM Products;
     ```
   - **If we want to get all values we will have to use asterisk(\*) symbol.Otherwise we will have to specify column name and condition also.**

   ##### How To Ignore Duplicates :-

   - We can Ignore Duplicates using `DISTINCT` keyword in the count function.
     ```SQL
     SELECT COUNT(DISTINCT Price) FROM Products;
     ```

2. `MIN()` :- 👉 This function returns the smallest value of the selected column.
    - **Syntax :-** 👇
        ```SQL
        SELECT MIN(column_name) FROM table_name WHERE condition;
        ```
3. `MAX()` :- 👉 This function returns the largest value of the selected column.

4. `AVG()` :- 👉 This function returns the average values of the numeric column.
    > Note :- &nbsp; `NULL` Values are ignored.

5. `SUM()` :- 👉 This function returns the total sum of a numeric column.