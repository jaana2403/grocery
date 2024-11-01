

# Grocery-Store-Management-System

This program has been made as a school project using Python and MySQL.

# General Instructions
1. The database is to be created manually, tables will be created automatically after first run.

2. [tkinter](https://docs.python.org/3/library/tkinter.html) and [pillow](https://pypi.org/project/Pillow/) modules must be installed on your device to run the program. 

3. The admin account can only be created manually from the MySQL command line. You will need to at least create one admin account to get started with the system.

4. Host, Username, Password is set to the default value, change it according to your device to connect the program with the database.

*NOTE:- There is 19 database connector statement which all need to change according to your device.*

5. *Category, Sub-Category, Products* are to be manually added to the code as well as normally added to the database to execute further instructions in the system. (To manually add items jump to line no: *1333*.)

*NOTE:- Data added to the database is to be the same as the data entered in the source code. Also, space gap is not allowed in sub-categories and products, adding gap may result in an error. Use subtract symbol or underscore instead.*

# Database Information

Database name: *grocery_store*

```bash
CREATE DATABASE grocery_store;
```
*Note:- The database is to be created manually.*

# Tables Information

Tables: *admin_register, employees, invoices, products*

1. admin_register 
```bash
CREATE TABLE admin_register (
id int,
username varchar(20),
password varchar(50)
);
```
2. employees
```bash
CREATE TABLE employees (
employee_id int,
username varchar(20),
password varchar(50),
employee_name varchar(300),
contact_num varchar(10),
address varchar(300),
aadhar_num varchar(12)
);
```
3. invoices
```bash
CREATE TABLE invoices (
bill_number int,
date varchar(10),
customer_name varchar(300),
customer_contact varchar(10)
);
```
4. products
```bash
CREATE TABLE products (
product_id int,
category varchar(300),
sub_category varchar(300),
product_name varchar(300),
stock_quantity int,
MRP int
);
```
*Note:- Tables will be created automatically after first run.*


# Software Requrements
1. [Python 3.9](https://www.python.org)
2. [MySQL](https://www.mysql.com/)

## License

[MIT](https://choosealicense.com/licenses/mit/)
