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
#c = conn.cursor()

# creating table for Theater info ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
query = (''' CREATE TABLE IF NOT EXISTS MOVIE
            (MOVIE_ID INTEGER PRIMARY KEY,
            MOVIE_TITLE TEXT,
            MOVIE_SCREEN INTEGER,
            MOVIE_DATE TEXT,
            MOVIE_START INTEGER,
            MOVIE_END INTEGER,
            MOVIE_RATING INTEGER,
            MOVIE_PRICE MONEY,
            THEAT_ID INTEGER NOT NULL,
            FOREIGN KEY (THEAT_ID) REFERENCES THEATER(THEATER_ID)
            );''')
conn.execute(query)


conn.execute("PRAGMA foreign_keys = ON")

conn.execute("INSERT INTO THEATER (THEATER_ID,THEATER_NAME,THEATER_SEATCAPACITY) \
VALUES (2, 'Test Cinema', 34)");

conn.execute("INSERT INTO MOVIE (MOVIE_ID, MOVIE_TITLE, MOVIE_SCREEN, MOVIE_DATE, MOVIE_START, MOVIE_END, MOVIE_RATING, MOVIE_PRICE, THEAT_ID) \
VALUES (1, 'TEST MOVIE', 2, 'OCT 12 22', 1200, 1400, 7, 12.99, 2)");



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

"""

'''
c.execute("""CREATE TABLE MOVIE (
        MOVIE_ID integer primary key,
        MOVIE_TITLE text,
        MOVIE_DATE text,
        MOVIE_START integer,
        MOVIE_END integer,
        MOVIE_RATING integer,
        MOVIE_PRICE money,
        FOREIGN KEY (THEATER_ID) REFERENCES THEATER(THEATER_ID),
        FOREIGN KEY (THEATER_SCREEN) REFERENCES THEATER(THEATER_SCREEN)
        )""")

c.execute("""CREATE TABLE TICKET (
        TICKET_NUM integer primary key,
        CONF_NUM integer,
        MOVIE_SEATNUM integer,
        FOREIGN KEY (USER_FNAME) REFERENCES USER_INFO(USER_FNAME),
        FOREIGN KEY (USER_LNAME) REFERENCES USER_INFO(USER_LNAME),
        FOREIGN KEY (USER_AGE) REFERENCES USER_INFO(USER_AGE),
        FOREIGN KEY (MOVIE_TITLE) REFERENCES MOVIE(MOVIE_TITLE),
        FOREIGN KEY (MOVIE_START) REFERENCES MOVIE(MOVIE_START),
        FOREIGN KEY (MOVIE_END) REFERENCES MOVIE(MOVIE_END),
        FOREIGN KEY (MOVIE_PRICE) REFERENCES MOVIE(MOVIE_PRICE),
        FOREIGN KEY (THEATER_ID) REFERENCES THEATER(THEATER_ID),
        FOREIGN KEY (MOVIE_SCREEN) REFERENCES MOVIE(MOVIE_SCREEN),
        FOREIGN KEY (USER_ID) REFERENCES USER_INFO(USER_ID),
        FOREIGN KEY (MOVIE_ID) REFERENCES MOVIE(MOVIE_ID)
        )""")

c.execute("""CREATE TABLE HISTORY (
        HISTORY_NUM integer primary key,
        FOREIGN KEY (USER_ID) REFERENCES USER_INFO(USER_ID),
        FOREIGN KEY (MOVIE_TITLE) REFERENCES MOVIE(MOVIE_TITLE),
        FOREIGN KEY (MOVIE_DATE) REFERENCES MOVIE(MOVIE_DATE),
        FOREIGN KEY (MOVIE_PRICE) REFERENCES MOVIE(MOVIE_PRICE),
        FOREIGN KEY (CONF_NUM) REFERENCES TICKET(CONF_NUM)
        )""")
'''

# commit changes
conn.commit()
# close connection
conn.close()

root.mainloop()