from tkinter import *
# from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title('Theater E-Ticket Info')
root.geometry("400x400")

# database------------------

# creating a database
conn = sqlite3.connect('theater_ticketing.db')

# cursor creation
c = conn.cursor()
'''
# creating tables
c.execute("""CREATE TABLE USER_INFO (
        USER_FNAME text,
        USER_LNAME text,
        USER_PHONE integer,
        USER_EMAIL varchar,
        USER_AGE integer,
        USER_PAY money,
        USER_HIST money
        )""")
'''

# commit changes
conn.commit()
# close connection
conn.close()

root.mainloop()


