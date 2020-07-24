import mysql.connector

try:
    connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="knackforge",
    database="employee")
    query = connection.cursor()
    query.execute("select max(salary),role from emp_salary,emp where role='as' and salary not in(select max(salary) from emp_salary);")
    for x in query:
	    print(x)
except Exception as e:
    print(e)
    