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

# commit changes
conn.commit()

# close connection
conn.close()

root.mainloop()