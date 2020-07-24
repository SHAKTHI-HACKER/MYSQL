import mysql.connector


def insert_values(id,emp_id,salary):

  try:
    
    connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="knackforge",
    database="employee"
    )
    query = connection.cursor()
    
        
    query_be = """insert into emp_salary(id,emp_id,salary) 
    values(%s,%s,%s)"""
    value_are = (id,emp_id,salary)
    query.execute(query_be,value_are)
    connection.commit()
    for x in query:
       print(x)
       

  except exception as e:
    print(e)
    
  finally:
    if(connection.is_connected()):
      query.close()
      connection.close()
      print("Db closed")
      
def insert_values_salary(dep,id,emp_id,role):

  try:
    
    connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="knackforge",
    database="employee"
    )
    query = connection.cursor()
    
        
    query_be = """insert into emp(dep,id,emp_id,role) 
    values(%s,%s,%s,%s)"""
    value_are = (dep,id,emp_id,role)
    query.execute(query_be,value_are)
    connection.commit()
    for x in query:
       print(x)
       

  except Exception as e:
    print(e)
    
  finally:
    if(connection.is_connected()):
      query.close()
      connection.close()
      print("Db closed")
      
      

num = int(input("enter the number of emp")) 

for x in range(1,num+1):     
    id = input("enter the id :")
    dep = input("enter the dept")
    emp_id = input("emp id : ")
    role = input("enter role : ")
    insert_values_salary(dep,id,emp_id,role)
for x in range(1,num+1):     
    id = input("enter the id :")
    emp_id = input("emp id : ")
    salary = input("salary : ")
    insert_values(id,emp_id,salary)