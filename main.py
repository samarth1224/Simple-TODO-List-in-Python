import DataBase
import sqlite3

# db = DataBase.DataBase("samarthh.db")
# # db.Create_Table("samarthssws")
# print(db.Read_task("samarthssws"))
# # db.Update_Task("nimade","samarthssws","2")

#
#
print("-------------TODO LIST---------------")
Name = input("Enter your Name ")

Task_input  = int(input('''Enter your choice:
        1) Add Task
        2) Delete Task
        3) Update Task
        4) Display Tasks
        5) Exit'''))

db = DataBase.DataBase("samarthh.db")
db.Create_Table(Name)
if Task_input == 1:
    Task = input("Enter a Task:")
    db.Create_Task(Task=Task,Tabel_Name=Name)
elif Task_input == 2:
    Task_Number = input("Enter the number of Task to Delete")
    db.Delete_Task(Table_Name=Name,Id=Task_Number)
elif Task_input == 3:
    Task_Number = input("Enter the Number of Task to Update")
    Updated_task = input("Enter Updated Task")
    db.Update_Task(Task=Updated_task,Table_Name=Name,Id=Task_Number)
elif Task_input == 4:
    print("No.      TASk ")
    for Number,Task in db.Read_task(Table_Name=Name):
        print(f"{Number}:| {Task}")
else:
    print("exiting....")
    db.cursor.close()
