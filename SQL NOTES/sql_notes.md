# How To Login MySQL as a root:-
- To **login** as a `root user` in Open Terminal and enter the following command.
    ```bash
    # In Linux 
    sudo mysql -u root -p

    # In Windows
    mysql -u root -p
    ``` 
------
## Basic Important Commands :-

- `status` **:-** 👉 &nbsp;This command is used to show status of mysql server.
- `show databases` **:-** 👉 &nbsp;**This command is used to show all databases in our mysql server.**

- `use dataBaseName` **:-** 👉 &nbsp; **This command is used to select database.**

- `show tables` **:-** 👉 &nbsp; **This command is used to show tables from selected database.**
- `describe tableName` **:-** 👉 &nbsp; **It is used to show structure of selected database table content.**

- `\q` **:-** 👉 &nbsp; **It is used to exit from mysql datbase.**
- `exit` **:-** 👉 &nbsp; **It is also used to exit from mysql database.**



## How To Create a Database:-

- **CREATE DATABASE databaseName ;** 👉 &nbsp;This command is used **to create a database.**
- **CREATE DATABASE databaseName IF NOT EXISTS ;**  👉 &nbsp;This command is also used to **create a database if database is not exist.**
- **For Example :-** 👇

    ```sql
    CREATE DATABASE testdb;
    ```

## How To Delete a Database :-

- `DROP DATABASE databaseName;` 👉 This command is used **to delete a specified database.**

-  `DROP DATABASE IF EXISTS databaseName;` 👉 This command is used **to delete a database if database exists.**
- **For Example:-** 👇
    ```sql
    DROP DATABASE testdb;
    
    ---- conditionally delete
    DROP DATABASE IF EXISTS testdb;

    ```
------
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
    
    - **For Example :-**  👇
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
------
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

-----

### 2. UNIQUE :- 

#### When We Creating A Table :-

- **It ensures that all tables in a column are different.**
- **Syntax :-** 👇

``` text
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

------
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
