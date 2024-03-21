
#Task3:        
import mysql.connector as con
mysqldb=con.connect(host="localhost",user="root",password="root",database="my")
cursor=mysqldb.cursor()
# cursor.execute("create table if not exists student(student_id INT AUTO_INCREMENT PRIMARY KEY,first_name varchar(50),last_name varchar(50),age int,grade float )")
# print("database")

def insert():
    first_name=input("enter first_name:")
    last_name=input("enter last_name:")
    age=input("enter age:")
    grade=input("enter a grade:")
    sql="insert into student(first_name,last_name,age,grade)values(%s,%s,%s,%s)"
    val=(first_name,last_name,age,grade)
    cursor.execute(sql,val)
    mysqldb.commit()


def update():
   grade=float(input("enter new grade:"))
   first_name=input("enter first_name:")
   sql="update student set grade=%s where first_name=%s"
   val=(grade,first_name)
   cursor.execute(sql,val)
   mysqldb.commit()
 

def delete():
   last_name=input("enter last_name:")
   sql="delete from student where last_name=%s"
   val=(last_name,)
   cursor.execute(sql,val)
   mysqldb.commit()
   

def read():
    sql="select* from student"
    cursor.execute(sql)
    d=cursor.fetchall()
    for i in d:
     print(i)


def menu():
   print("opction\n1.insert\n2.update\n3.delete\n4.read")
   ch=int(input("enter ch:"))
   if ch==1:
      insert()
   elif ch==2:
      update()  
   elif ch==3:
      delete()
   elif ch==4:
      read()  
   else:
      print("wrong opction")      
      menu()        
menu()      
