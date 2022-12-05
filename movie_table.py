from tkinter import *

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

"""



def update():
    conn = sqlite3.connect('theater_ticketing.db')
    c = conn.cursor()

    record_select_id = delete_box.get()
    c.execute("""UPDATE MOVIE SET
        MOVIE_ID = :ID,
        MOVIE_TITLE = :TITLE,
        MOVIE_SCREEN = :SCREEN,
        MOVIE_DATE = :DATE,
        MOVIE_START = :START,
        MOVIE_END = :END,
        MOVIE_RATING = :RATING,
        MOVIE_PRICE = :PRICE,
        THEAT_ID= :THEAT_ID

        WHERE MOVIE_ID = :SELECTED_ID""",
              {
                  'ID': movie_id_edit.get(),
                  'TITLE': movie_title_edit.get(),
                  'SCREEN': movie_screen_edit.get(),
                  'DATE': movie_date_edit.get(),
                  'START': movie_start_edit.get(),
                  'END': movie_end_edit.get(),
                  'RATING': movie_rating_edit.get(),
                  'PRICE': movie_price_edit.get(),
                  'THEAT_ID': theater_id_edit.get(),
                  'SELECTED_ID': record_select_id
              })

    conn.commit()
    conn.close()

    editor.destroy()


# edit/updates a THEATER's info record
def edit():
    global editor

    editor = Tk()
    editor.title('Edit Movie Record Info')
    editor.geometry("550x400")
    conn = sqlite3.connect('theater_ticketing.db')
    c = conn.cursor()

    record_id = delete_box.get()

    # query here means everything and the primary key
    c.execute("SELECT * FROM MOVIE WHERE MOVIE_ID =" + record_id)

    movie_records = c.fetchall()

    # create the text box name edits to global variables
    global movie_id_edit
    global movie_title_edit
    global movie_screen_edit
    global movie_date_edit
    global movie_start_edit
    global movie_end_edit
    global movie_rating_edit
    global movie_price_edit
    global theater_id_edit

    # creating the text boxes ~~~~~~~~~~~~~~~~~~~~~
    movie_id_edit = Entry(editor, width=30)
    movie_id_edit.grid(row=0, column=1, padx=20, pady=(10, 0))

    movie_title_edit = Entry(editor, width=30)
    movie_title_edit.grid(row=1, column=1, padx=20)

    movie_screen_edit = Entry(editor, width=30)
    movie_screen_edit.grid(row=2, column=1)

    movie_date_edit = Entry(editor, width=30)
    movie_date_edit.grid(row=3, column=1)

    movie_start_edit = Entry(editor, width=30)
    movie_start_edit.grid(row=4, column=1)

    movie_end_edit = Entry(editor, width=30)
    movie_end_edit.grid(row=5, column=1)

    movie_rating_edit = Entry(editor, width=30)
    movie_rating_edit.grid(row=6, column=1)

    movie_price_edit = Entry(editor, width=30)
    movie_price_edit.grid(row=7, column=1)

    theater_id_edit = Entry(editor, width=30)
    theater_id_edit.grid(row=8, column=1)

    # creating labels for the text boxes ~~~~~~~~~~~~~~~
    movie_id_label = Label(editor, text="Movie ID")
    movie_id_label.grid(row=0, column=0, pady=(10, 0))

    movie_title_label = Label(editor, text="Movie Title")
    movie_title_label.grid(row=1, column=0)

    movie_screen_label = Label(editor, text="Movie Screen")
    movie_screen_label.grid(row=2, column=0)

    movie_date_label = Label(editor, text="Movie Date")
    movie_date_label.grid(row=3, column=0)

    movie_start_label = Label(editor, text="Movie Start")
    movie_start_label.grid(row=4, column=0)

    movie_end_label = Label(editor, text="Movie End")
    movie_end_label.grid(row=5, column=0)

    movie_rating_label = Label(editor, text="Movie Rating")
    movie_rating_label.grid(row=6, column=0)

    movie_price_label = Label(editor, text="Movie Price")
    movie_price_label.grid(row=7, column=0)

    theater_id_label = Label(editor, text="Theater ID")
    theater_id_label.grid(row=8, column=0)

    # go through our record data and update them by looping
    for record in movie_records:
        movie_id_edit.insert(0, record[0])
        movie_title_edit.insert(0, record[1])
        movie_screen_edit.insert(0, record[2])
        movie_date_edit.insert(0, record[3])
        movie_start_edit.insert(0, record[4])
        movie_end_edit.insert(0, record[5])
        movie_rating_edit.insert(0, record[6])
        movie_price_edit.insert(0, record[7])
        theater_id_edit.insert(0, record[8])

    # creates a save button to save the edits/updates done on the theater's record information
    save_button = Button(editor, text="Save Movie's Info Records", command=update)
    save_button.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

    # conn.commit()
    # conn.close()


# create a function that deletes a THEATER info record from the THEATER table
def delete():
    conn = sqlite3.connect('theater_ticketing.db')
    c = conn.cursor()

    # delete a THEATER record
    c.execute("DELETE from MOVIE WHERE MOVIE_ID = " + delete_box.get())

    delete_box.delete(0, END)

    conn.commit()
    conn.close()


# creating the submit function for the submit_button
def submit():
    conn = sqlite3.connect('theater_ticketing.db')
    c = conn.cursor()

    # insert data into the theater_info table
    c.execute(
        "INSERT INTO MOVIE VALUES (:movie_id, :movie_title, :movie_screen, :movie_date, :movie_start, :movie_end, :movie_rating, :movie_price, :theat_id)",
        {
            'movie_id': movie_id.get(),
            'movie_title': movie_title.get(),
            'movie_screen': movie_screen.get(),
            'movie_date': movie_date.get(),
            'movie_start': movie_start.get(),
            'movie_end': movie_start.get(),
            'movie_rating': movie_rating.get(),
            'movie_price': movie_price.get(),
            'theat_id': theater_id.get()
        })

    conn.commit()
    conn.close()

    # clear the text boxes before/after each submit
    movie_id.delete(0, END)
    movie_title.delete(0, END)
    movie_screen.delete(0, END)
    movie_date.delete(0, END)
    movie_start.delete(0, END)
    movie_end.delete(0, END)
    movie_rating.delete(0, END)
    movie_price.delete(0, END)
    theater_id.delete(0, END)


# create a sql query function for the query button
def query():
    conn = sqlite3.connect('theater_ticketing.db')
    c = conn.cursor()

    # query here means everything and the primary key
    c.execute("SELECT * FROM MOVIE")

    movie_records = c.fetchall()
    # print(theater_Records)
    print_records = ''

    # looping through all theater info 'show record' query
    for record in movie_records:
        print_records += str(record[0]) + "  " + str(record[1]) + "  " + str(record[2]) + "  " + str(record[3]) + "  " \
                         + str(record[4]) + "  " + str(record[5]) + "  " + str(record[6]) + "  " + str(record[7]) \
                         + "  " + str(record[8]) + "  "+ " \n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=11, column=0, columnspan=2)

    conn.commit()
    conn.close()


# creating the text boxes ~~~~~~~~~~~~~~~~~~~~~
movie_id = Entry(root, width=30)
movie_id.grid(row=0, column=1, padx=20, pady=(10, 0))

movie_title = Entry(root, width=30)
movie_title.grid(row=1, column=1, padx=20)

movie_screen = Entry(root, width=30)
movie_screen.grid(row=2, column=1)

movie_date = Entry(root, width=30)
movie_date.grid(row=3, column=1)

movie_start = Entry(root, width=30)
movie_start.grid(row=4, column=1)

movie_end = Entry(root, width=30)
movie_end.grid(row=5, column=1)

movie_rating = Entry(root, width=30)
movie_rating.grid(row=6, column=1)

movie_price = Entry(root, width=30)
movie_price.grid(row=7, column=1)

theater_id = Entry(root, width=30)
theater_id.grid(row=8, column=1, padx=20, pady=(10, 0))

delete_box = Entry(root, width=30)
delete_box.grid(row=12, column=1, pady=5)

# creating labels for the text boxes ~~~~~~~~~~~~~~~
movie_id_label = Label(root, text="Movie ID")
movie_id_label.grid(row=0, column=0, pady=(10, 0))

movie_title_label = Label(root, text="Movie Title")
movie_title_label.grid(row=1, column=0)

movie_screen_label = Label(root, text="Movie Screen")
movie_screen_label.grid(row=2, column=0)

movie_date_label = Label(root, text="Movie Date")
movie_date_label.grid(row=3, column=0)

movie_start_label = Label(root, text="Movie Start")
movie_start_label.grid(row=4, column=0)

movie_end_label = Label(root, text="Movie End")
movie_end_label.grid(row=5, column=0)

movie_rating_label = Label(root, text="Movie Rating")
movie_rating_label.grid(row=6, column=0)

movie_price_label = Label(root, text="Movie Price")
movie_price_label.grid(row=7, column=0)

theater_id_label = Label(root, text="Theater ID")
theater_id_label.grid(row=8, column=0)

delete_label = Label(root, text="Select Movie ID")
delete_label.grid(row=12, column=0, pady=5)

# create a submit button ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
submit_button = Button(root, text="Add Movie Info Record To Database", command=submit)
submit_button.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=120)

# create a query button to see the Theater table information
query_button = Button(root, text="Show Movie Info Records", command=query)
query_button.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=147)

# create a delete button to delete a Theater's record from the table
delete_button = Button(root, text="Delete a Movie's Info Records", command=delete)
delete_button.grid(row=13, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

# create an edit button to update/edit a Theater's info record
edit_button = Button(root, text="Edit a Movie's Info Records", command=edit)
edit_button.grid(row=14, column=0, columnspan=2, pady=10, padx=10, ipadx=142)

# commit changes
conn.commit()
# close connection
conn.close()
root.mainloop()