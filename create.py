import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="knackforge",
    )
query = connection.cursor()

query.execute("create database employee;")	

query.execute("create table emp_salary(id int not null,emp_id int,salary)";)
query.execute("create table emp(dep varchar(100),id int not null,emp_id int,role varchar(200)";)
query = connection.cursor()
query.execute("alter table emp_salary add primary key(id);")
query.execute("alter table emp add primary key(id);")
query.execute("ALTER TABLE emp_salary ADD FOREIGN KEY (id) REFERENCES emp(id);")
