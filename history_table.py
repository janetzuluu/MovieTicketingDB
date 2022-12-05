from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('Theater E-Ticket Info')
root.geometry("500x600")
# database------------------

# creating a database
conn = sqlite3.connect('theater_ticketing.db')

# cursor creation
c = conn.cursor()

# creating table for Theater info ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


""" 

query = (''' CREATE TABLE IF NOT EXISTS TICKET
            (TICKET_NUM INTEGER primary key,
            CONF_NUM INTEGER,
            SEAT_NUM INTEGER,
            USER_ID integer,
            THEATER_ID INTEGER NOT NULL,
            MOVIE_ID INTEGER,       
            FOREIGN KEY (USER_ID) REFERENCES USER_INFO(USER_ID), 
            FOREIGN KEY (THEATER_ID) REFERENCES THEATER(THEATER_ID),
            FOREIGN KEY (MOVIE_ID) REFERENCES MOVIE(MOVIE_ID)
            );''')

conn.execute(query)



conn.execute("PRAGMA foreign_keys = ON")

conn.execute("INSERT INTO TICKET (TICKET_NUM, CONF_NUM, SEAT_NUM, USER_ID, THEATER_ID, MOVIE_ID) \
VALUES (123, 321, 23, 1, 2, 1)");

query = (''' CREATE TABLE IF NOT EXISTS HISTORY
            (HISTORY_NUM INTEGER PRIMARY KEY,
            USER_ID integer,
            MOVIE_ID INTEGER,
            TICKET_NUM INTEGER NOT NULL,
            FOREIGN KEY (USER_ID) REFERENCES USER_INFO(USER_ID),
            FOREIGN KEY (MOVIE_ID) REFERENCES MOVIE(MOVIE_ID),
            FOREIGN KEY (TICKET_NUM) REFERENCES TICKET(TICKET_NUM )
            );''')


conn.execute(query)

conn.execute("PRAGMA foreign_keys = ON")

conn.execute("INSERT INTO HISTORY (HISTORY_NUM, USER_ID, MOVIE_ID, TICKET_NUM) \
VALUES (1111, 1, 1, 123)");

"""
'''
query = ("""CREATE TABLE IF NOT EXISTS USER_INFO (
        USER_ID integer primary key,
        USER_FNAME text,
        USER_LNAME text,
        USER_PHONE integer,
        USER_EMAIL varchar,
        USER_AGE integer,
        USER_PAY integer, 
        USER_HIST money,
        USER_PASS varchar
        )""")
conn.execute(query)
'''


# conn.execute("SELECT movie_title FROM movie WHERE movie_id = '156'");







# commit changes
conn.commit()

# close connection
conn.close()

root.mainloop()