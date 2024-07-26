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
- `describe tableName` **:-** 👉 &nbsp; **It is used to show describe/show table content.**

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