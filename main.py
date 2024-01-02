import mysql.connector
from tabulate import tabulate

# Establish Connection
con = mysql.connector.connect(host="localhost", user="root", password="", database="student")


def insert_record():
    name = input("Enter Name : ")
    age = int(input("Enter Age : "))
    address = input("Enter Address : ")
    contact_no = int(input("Enter Contact Number : "))
    mail_id = input("Enter Mail_ID : ")
    res = con.cursor()
    sql = "insert into student_data(Name,Age,Address,Contact_No,Mail) values (%s,%s,%s,%s,%s)"
    res.execute(sql, (name, age, address, contact_no, mail_id))
    con.commit()
    print("\n")
    print("Record Added Successfully")


def select_record():
    res = con.cursor()
    print("\t\t\t1)Retrieve All The Records\t\t\t")
    print("\t\t\t2)Select a Specific Record\t\t\t")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        sql = "select * from student_data"
        res.execute(sql)
        result = res.fetchall()
        print("\n")
        print(tabulate(result, headers=["Roll_No", "Name", "Age", "Address", "Contact_No", "Mail_ID"]))
    if ch == 2:
        roll_no = int(input("Enter roll_no for which the record is to be retrieved : "))
        sql = "select * from student_data where Roll_No=%s"
        res.execute(sql, roll_no)
        result = res.fetchone()
        print("\n")
        print(tabulate(result, headers=["Roll_No", "Name", "Age", "Address", "Contact_No", "Mail_ID"]))


def update_record():
    print("\t\t\t1)Name\t\t\t")
    print("\t\t\t2)Age\t\t\t")
    print("\t\t\t3)Address\t\t\t")
    print("\t\t\t4)Contact_Number\t\t\t")
    print("\t\t\t5)Mail_ID\t\t\t")
    ch = int(input("Which field do you want to update? "))
    if ch == 1:
        roll_no = int(input("Enter Roll_No : "))
        name = input("Enter name : ")
        sql = "update student_data set Name=%s where Roll_No=%s"
        res = con.cursor()
        res.execute(sql, (name, roll_no))
        con.commit()
        print("Record Updated Successfully.......")
    elif ch == 2:
        roll_no = int(input("Enter Roll_No : "))
        age = int(input("Enter Age : "))
        sql = "update student_data set Age=%s where Roll_No=%s"
        res = con.cursor()
        res.execute(sql, (age, roll_no))
        con.commit()
        print("Record Updated Successfully.......")
    elif ch == 3:
        roll_no = int(input("Enter Roll_No : "))
        address = input("Enter Address : ")
        sql = "update student_data set Address=%s where Roll_No=%s"
        res = con.cursor()
        res.execute(sql, (address, roll_no))
        con.commit()
        print("Record Updated Successfully.......")
    elif ch == 4:
        roll_no = int(input("Enter Roll_No : "))
        age = int(input("Enter Contact Number : "))
        sql = "update student_data set Contact_No=%s where Roll_No=%s"
        res = con.cursor()
        res.execute(sql, (age, roll_no))
        con.commit()
        print("Record Updated Successfully.......")
    elif ch == 5:
        roll_no = int(input("Enter Roll_No : "))
        mail = input("Enter Mail_ID : ")
        sql = "update student_data set Mail=%s where Roll_No=%s"
        res = con.cursor()
        res.execute(sql, (mail, roll_no))
        con.commit()
        print("Record Updated Successfully.......")
    else:
        print("Invalid Choice!")


def delete_record():
    roll_no = int(input("Enter Roll_Number : "))
    sql = "delete from student_data where roll_no=%s"
    res = con.cursor()
    res.execute(sql, roll_no)
    con.commit()
    print("Record Deleted Successfully.......")


while True:
    print("\n")
    print("-----------STUDENT MANAGEMENT SYSTEM------------")
    print("\t\t\t\t1)Insert Record\t\t\t\t")
    print("\t\t\t\t2)Select Record\t\t\t\t")
    print("\t\t\t\t3)Update Record\t\t\t\t")
    print("\t\t\t\t4)Delete Record\t\t\t\t")
    print("\t\t\t\t5)Exit\t\t\t\t")
    choice = int(input("Enter your choice"))
    if choice == 1:
        insert_record()
    elif choice == 2:
        select_record()
    elif choice == 3:
        update_record()
    elif choice == 4:
        delete_record()
    elif choice == 5:
        quit()
    else:
        print("Invalid choice ! Try Again")
