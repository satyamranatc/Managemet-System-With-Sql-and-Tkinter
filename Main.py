from tkinter import *
import mysql.connector

db = mysql.connector.connect(
    username="root",
    password="satyamrana",
    host="localhost",
    database="Test"
)

cursor = db.cursor()


class Student:
    def __init__(self, I, N, A, C, R):
        self.Id = I
        self.Name = N
        self.Age = A
        self.Class = C
        self.Rank = R
        cursor.execute("CREATE TABLE IF NOT EXISTS Student (Id INT, Name TEXT, Age INT, Class TEXT, `Rank` INT)")
        cursor.execute("INSERT INTO Student VALUES (%s, %s, %s, %s, %s)",
                       (self.Id, self.Name, self.Age, self.Class, self.Rank))
        db.commit()


AllStudents = []

root = Tk()
root.title("My App")
root.geometry("400x400")

l1 = Label(text="Student Management System")
l1.pack()

l2 = Label(text="Enter Your Id: ")
l2.pack()

i1 = Entry()
i1.pack()

l3 = Label(text="Enter Your Name: ")
l3.pack()

i2 = Entry()
i2.pack()

l4 = Label(text="Enter Your Age: ")
l4.pack()

i3 = Entry()
i3.pack()

l5 = Label(text="Enter Your Class: ")
l5.pack()

i4 = Entry()
i4.pack()

l6 = Label(text="Enter Your Rank: ")
l6.pack()

i5 = Entry()
i5.pack()


def fetchData():
    Id = i1.get()
    Name = i2.get()
    Age = i3.get()
    Class = i4.get()
    Rank = i5.get()
    AllStudents.append(Student(Id, Name, Age, Class, Rank))


def getData():
    for i in AllStudents:
        print(i.Id)
        print(i.Name)
        print(i.Age)
        print(i.Class)
        print(i.Rank)
        print("-------------")


b1 = Button(text="Submit", command=fetchData)
b1.pack()

b2 = Button(text="Print", command=getData)
b2.pack()

root.mainloop()
