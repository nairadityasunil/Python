

from mysql.connector import Connect,Error
from threading import *

# Making connection

con = Connect(
    host ="localhost",
    port = 3307,
    user = "root",
    password = "Appu_2003",
    database = "pydb"
    )

# Cursor to execute queries
cursor = con.cursor()

sql = """CREATE TABLE tblstudent(
    roll int,
    name varchar(30)
    )"""
    
try:
    cursor.execute(sql)
    print("Table Created")
except Error as e:
    print(e) 
##
   
lock = Lock()

def ins_male():
    with lock:
        for i in range(3):
            print("Male Student Details")
            roll = input("Enter Roll : ")
            name = input("Enter Name : ")
            sql = "Insert into tblstudent (roll,name) values(%s,%s)"
            values = (roll, name)

            try:
                cursor.execute(sql, values)
                con.commit()
            except Error as e:
                print(e)
##            

def ins_female():
    with lock:
        for i in range(3):
            print("Female Student Details")
            roll = input("Enter Roll : ")
            name = input("Enter Name : ")
            sql = "Insert into tblstudent (roll,name) values(%s,%s)"
            values = (roll, name)

            try:
                cursor.execute(sql, values)
                con.commit()
            except Error as e:
                print(e)
##           

t1 = Thread(target = ins_male)
t2 = Thread(target = ins_female)

t1.start()
t2.start()

t1.join()
t2.join()
