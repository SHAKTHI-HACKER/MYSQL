import mysql.connector

try:
    connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="knackforge",
    database="employee")
    query = connection.cursor()
    query.execute("select role,emp_id from emp where role ='bs' and dep !='it';")
    for x in query:
	    print(x)
except Exception as e:
    print(e)
    