import mysql.connector

try:
    connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="knackforge",
    database="employee")
    query = connection.cursor()
    query.execute("select role ,sum(salary) from emp,emp_salary group by role;")
    for x in query:
	    print(x)
except Exception as e:
    print(e)
    