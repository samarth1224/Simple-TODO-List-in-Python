#By Samarth Nimade
#Database Class---Handles Database Operations Like Adding and Removing Tasks.

import sqlite3

class DataBase:
    def __init__(self,DataBase_Name):
        self.DataBase_Name = DataBase_Name
        self.connect  = sqlite3.connect(DataBase_Name)
        self.cursor = self.connect.cursor()


    def Create_Table(self,Table_Name):
        self.cursor.execute(f"SELECT name FROM sqlite_master WHERE type = 'table' AND name = '{Table_Name}';")
        # print(self.cursor.fetchone())

        if self.cursor.fetchone() == None:
            self.cursor.execute(f"CREATE TABLE {Table_Name}("
                                # f"Number INTEGER PRIMARY KEY AUTOINCREMENT,"
                                f"TASK TEXT)")
        self.connect.commit()


    def Create_Task(self,Task,Tabel_Name):

        try:
            self.cursor.execute(f"INSERT INTO {Tabel_Name} VALUES('{Task}')")
        except sqlite3.OperationalError as e:
            print(f"Error {e}")
        finally:
            self.connect.commit()


    def Delete_Task(self,Table_Name,Id):

        try:
            self.cursor.execute(f"DELETE FROM {Table_Name} WHERE ROWID = {Id}")

        except sqlite3.OperationalError as e:
            print(f"Error {e}")
        finally:
            self.connect.commit()


    def Read_task(self,Table_Name):

        try:
            self.cursor.execute(f"SELECT ROWID,TASK FROM {Table_Name} ")
            Task = self.cursor.fetchall()
            return Task
        except sqlite3.OperationalError as e:
            print(f'Error {e}')
        finally:
            self.connect.commit()


    def Update_Task(self,Task,Table_Name,Id):

        try:
            self.cursor.execute(f'''UPDATE {Table_Name} SET TASK = ? WHERE ROWID = ?''',(Task,Id))
        except sqlite3.OperationalError as e:
            print(f'Error {e}')
        finally:
            self.connect.commit()


    def close_cursor(self):
        self.cursor.close()




