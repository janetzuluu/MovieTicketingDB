import sqlite3
import tkinter as tk
from tkinter import *

from tkinter import Entry

root2 = tk.Tk()
root2.title("Management")
root2.geometry('1000x1200')

# database------------------

# creating a database
conn = sqlite3.connect('theater_ticketing.db')

# cursor creation
c = conn.cursor()


'''
c.execute("""CREATE TABLE IF NOT EXISTS THEATER (
        THEATER_ID integer primary key,
        THEATER_NAME text,
        THEATER_SEATCAPACITY integer
        )""")
'''
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




def home_page():
    conn = sqlite3.connect('theater_ticketing.db')
    c = conn.cursor()

    # query here means everything and the primary key
    #  c.execute("SELECT * FROM USER_INFO")
    r_set1 = c.execute("SELECT COUNT(THEATER_ID) FROM THEATER")
    r_set1 = c.fetchone()

    r_set2 = c.execute("SELECT SUM(USER_PAY) FROM USER_INFO")
    r_set2 = c.fetchone()

    r_set3 = c.execute("SELECT COUNT(USER_PAY) FROM USER_INFO")
    r_set3 = c.fetchone()
    print(r_set2)
    current_frame=tk.Frame(main_frame)

    mCanvas = tk.Canvas(current_frame, width=320, height=320, bg="#c3c3c3")
    mCanvas.create_text(159, 50, text="Current Movies", fill="black", font=('Helvetica 25 bold'))
    mCanvas.create_text(130, 150, text= r_set1,fill="black",font=('Helvetica 20 bold'))

    mCanvas2 = tk.Canvas(current_frame, width=320, height=320, bg="#c3c3c3")

    mCanvas2.create_text(159, 50, text="Money Made: ", fill="black", font=('Helvetica 25 bold'))
    mCanvas2.create_text(130, 150, text="$ ", fill="black", font=('Helvetica 20 bold'))
    mCanvas2.create_text(130, 160, text=r_set2, fill="black", font=('Helvetica 20 bold'))



    mCanvas3 = tk.Canvas(current_frame, width=320, height=320, bg="#c3c3c3")
    mCanvas3.create_text(159, 50, text="Customers Served", fill="black", font=('Helvetica 25 bold'))

    mCanvas3.create_text(150, 150, text=r_set3, fill="black", font=('Helvetica 20 bold'))

    lb1 = tk.Label(current_frame, text='Welcome Admin', font=('Bold', 50))
    lb1.pack()
    lb2 = tk.Label(current_frame, text='', font=('Bold', 30))
  #  lb2.pack()


    T = tk.Text(current_frame, height=10, width=30,font=('Bold'))
   # T.pack(side=tk.LEFT,anchor='nw')
    T.insert(INSERT, "Current Movies")



    v = tk.Text(current_frame, height=10, width=30,font=('Bold'))
   # v.pack(side=tk.LEFT, anchor='nw')
    v.insert(INSERT, "Money Made")

    b = tk.Text(current_frame, height=10, width=30,font=('Bold'))
   # b.pack(side=tk.LEFT, anchor='nw')

    mCanvas.pack(side=tk.LEFT)
    mCanvas2.pack(side=tk.LEFT)
    mCanvas3.pack(side=tk.LEFT)
    #b.insert(INSERT,f"{r_set1}")

    conn.commit()
    conn.close()
    current_frame.pack(padx=20)
def theater_page():
    theater_frame=tk.Frame(main_frame)



    theater_frame.pack(pady=20)

def history_page():
    history_frame=tk.Frame(main_frame)


    conn = sqlite3.connect('theater_ticketing.db')
    c = conn.cursor()

    # query here means everything and the primary key
  #  c.execute("SELECT * FROM USER_INFO")
    r_set = c.execute("SELECT * FROM MOVIE")
    i = 0
    e = tk.Label(history_frame, width=10, text='user_id', borderwidth=2, relief='ridge', anchor='w', bg='white')
    e.grid(row=0, column=0)
    e = tk.Label(history_frame, width=10, text='Movie Title', borderwidth=2, relief='ridge', anchor='w', bg='white')
    e.grid(row=0, column=1)
    e = tk.Label(history_frame, width=10, text='Movie Date', borderwidth=2, relief='ridge', anchor='w', bg='white')
    e.grid(row=0, column=2)
    e = tk.Label(history_frame, width=10, text='Movie_price', borderwidth=2, relief='ridge', anchor='w', bg='white')
    e.grid(row=0, column=3)
    e = tk.Label(history_frame, width=10, text='Conf number', borderwidth=2, relief='ridge', anchor='w', bg='white')
    e.grid(row=0, column=4)
    i = 1
    for USERS in r_set:
        for j in range(len(USERS)):

            e = tk.Entry(history_frame, width=10, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, USERS[j])
        i = i + 1

    history_frame.pack(pady=20)
def exit_page():
    root2.destroy()
    exit_frame=tk.Frame(main_frame)

    lb=tk.Label(exit_frame,text='Exit Page\n\nPage: 3',font=('Bold', 30))
    lb.pack()
    exit_frame.pack(pady=20)
def hide_indicators():
    current_indicate.config(bg='#c3c3c3')
    history_indicate.config(bg='#c3c3c3')
    exit_indicate.config(bg='#c3c3c3')
def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()
def indicate(lb,page):
    hide_indicators()
    lb.config(bg='#158aff')
    delete_pages()
    page()


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

    query_label = Label(add_frame, text=print_records)
    query_label.grid(row=11, column=0, columnspan=2)

    conn.commit()
    conn.close()


def hi():
    global add_frame
    global movie_id

    global movie_title
    global movie_screen
    global movie_date
    global movie_start
    global movie_end
    global movie_rating
    global movie_price
    global theater_id
    add_frame=tk.Frame(main_frame)
    movie_id = Entry(add_frame, width=30)
    movie_id.grid(row=0, column=1, padx=20, pady=(10, 0))

    movie_title = Entry(add_frame, width=30)
    movie_title.grid(row=1, column=1, padx=20)

    movie_screen = Entry(add_frame, width=30)
    movie_screen.grid(row=2, column=1)

    movie_date = Entry(add_frame, width=30)
    movie_date.grid(row=3, column=1)

    movie_start = Entry(add_frame, width=30)
    movie_start.grid(row=4, column=1)

    movie_end = Entry(add_frame, width=30)
    movie_end.grid(row=5, column=1)

    movie_rating = Entry(add_frame, width=30)
    movie_rating.grid(row=6, column=1)

    movie_price = Entry(add_frame, width=30)
    movie_price.grid(row=7, column=1)

    theater_id = Entry(add_frame, width=30)
    theater_id.grid(row=8, column=1, padx=20, pady=(10, 0))
    global delete_box
    delete_box = Entry(add_frame, width=30)
    delete_box.grid(row=12, column=1, pady=5)

    # creating labels for the text boxes ~~~~~~~~~~~~~~~
    movie_id_label = Label(add_frame, text="Movie ID")
    movie_id_label.grid(row=0, column=0, pady=(10, 0))

    movie_title_label = Label(add_frame, text="Movie Title")
    movie_title_label.grid(row=1, column=0)

    movie_screen_label = Label(add_frame, text="Movie Screen")
    movie_screen_label.grid(row=2, column=0)

    movie_date_label = Label(add_frame, text="Movie Date")
    movie_date_label.grid(row=3, column=0)

    movie_start_label = Label(add_frame, text="Movie Start")
    movie_start_label.grid(row=4, column=0)

    movie_end_label = Label(add_frame, text="Movie End")
    movie_end_label.grid(row=5, column=0)

    movie_rating_label = Label(add_frame, text="Movie Rating")
    movie_rating_label.grid(row=6, column=0)

    movie_price_label = Label(add_frame, text="Movie Price")
    movie_price_label.grid(row=7, column=0)

    theater_id_label = Label(add_frame, text="Theater ID")
    theater_id_label.grid(row=8, column=0)

    delete_label = Label(add_frame, text="Select Movie ID")
    delete_label.grid(row=12, column=0, pady=5)

    # create a submit button ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    submit_button = Button(add_frame, text="Add Movie Info Record To Database", command=submit)
    submit_button.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=120)

    # create a query button to see the Theater table information
    query_button = Button(add_frame, text="Show Movie Info Records", command=query)
    query_button.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=147)

    # create a delete button to delete a Theater's record from the table
    delete_button = Button(add_frame, text="Delete a Movie's Info Records", command=delete)
    delete_button.grid(row=13, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

    # create an edit button to update/edit a Theater's info record
    edit_button = Button(add_frame, text="Edit a Movie's Info Records", command=edit)
    edit_button.grid(row=14, column=0, columnspan=2, pady=10, padx=10, ipadx=142)

    # commit changes
    conn.commit()
    # close connection
    conn.close()
    add_frame.pack(pady=20)


def update():
    conn = sqlite3.connect('theater_ticketing.db')
    c = conn.cursor()

    record_select_id = delete_box.get()
    c.execute("""UPDATE THEATER SET
        THEATER_ID = :ID,
        THEATER_NAME = :NAME,
        THEATER_SEATCAPACITY = :SEAT

        WHERE THEATER_ID = :SELECTED_ID""",
              {
                  'ID': theater_id_edit.get(),
                  'NAME': theater_name_edit.get(),
                  'SEAT': theater_seatCapacity_edit.get(),
                  'SELECTED_ID': record_select_id
              })

    conn.commit()
    conn.close()

    editor.destroy()

# edit/updates a THEATER's info record
def edit1():
    global editor
    editor = Tk()
    editor.title('Edit theater Record Info')
    editor.geometry("550x400")
    conn = sqlite3.connect('theater_ticketing.db')
    c = conn.cursor()

    record_id = delete_box.get()

    # query here means everything and the primary key
    c.execute("SELECT * FROM THEATER WHERE THEATER_ID =" + record_id)

    theater_records = c.fetchall()

    # create the text box name edits to global variables
    global theater_id_edit
    global theater_name_edit
    global theater_seatCapacity_edit


    # creating the text boxes ~~~~~~~~~~~~~~~~~~~~~
    theater_id_edit = Entry(editor, width=30)
    theater_id_edit.grid(row=0, column=1, padx=20, pady=(10, 0))

    theater_name_edit = Entry(editor, width=30)
    theater_name_edit.grid(row=1, column=1, padx=20)

    theater_seatCapacity_edit = Entry(editor, width=30)
    theater_seatCapacity_edit.grid(row=2, column=1)

    # creating labels for the text boxes ~~~~~~~~~~~~~~~
    theater_id_label = Label(editor, text="Theater ID")
    theater_id_label.grid(row=0, column=0, pady=(10, 0))

    theater_name_label = Label(editor, text="Theater Name")
    theater_name_label.grid(row=1, column=0)

    theater_seatCapacity_label = Label(editor, text="Seat Capacity")
    theater_seatCapacity_label.grid(row=2, column=0)

    # go through our record data and update them by looping
    for record in theater_records:
        theater_id_edit.insert(0, record[0])
        theater_name_edit.insert(0, record[1])
        theater_seatCapacity_edit.insert(0, record[2])

    # creates a save button to save the edits/updates done on the theater's record information
    save_button = Button(editor, text="Save Theater's Info Records", command=update)
    save_button.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

    # conn.commit()
    # conn.close()


# create a function that deletes a THEATER info record from the THEATER table
def delete1():
    conn = sqlite3.connect('theater_ticketing.db')
    c = conn.cursor()

    # delete a THEATER record
    c.execute("DELETE from THEATER WHERE THEATER_ID = " + delete_box.get())

    delete_box.delete(0, END)

    conn.commit()
    conn.close()


# creating the submit function for the submit_button
def submit1():
    conn = sqlite3.connect('theater_ticketing.db')
    c = conn.cursor()

    # insert data into the theater_info table
    c.execute(
        "INSERT INTO THEATER VALUES (:theater_id, :theater_name, :theater_seatCapacity)",
        {
            'theater_id': theater_id.get(),
            'theater_name': theater_name.get(),
            'theater_seatCapacity': theater_seatCapacity.get()
        })

    conn.commit()
    conn.close()

    # clear the text boxes before/after each submit
    theater_id.delete(0, END)
    theater_name.delete(0, END)
    theater_seatCapacity.delete(0, END)


# create a sql query function for the query button
def query1():
    conn = sqlite3.connect('theater_ticketing.db')
    c = conn.cursor()

    # query here means everything and the primary key
    c.execute("SELECT * FROM THEATER")

    theater_records = c.fetchall()
    # print(theater_Records)
    print_records = ''

    # looping through all theater info 'show record' query
    for record in theater_records:
        print_records += str(record[0]) + "  " + str(record[1]) + "  " + str(record[2]) + " \n"

    query_label = Label(h1_frame, text=print_records)
    query_label.grid(row=11, column=0, columnspan=2)

    conn.commit()
    conn.close()

# creating the text boxes ~~~~~~~~~~~~~~~~~~~~~
def h2():
    global h1_frame
    h1_frame=tk.Frame(main_frame)
    theater_id = Entry(h1_frame, width=30)
    theater_id.grid(row=0, column=1, padx=20, pady=(10, 0))

    theater_name = Entry(h1_frame, width=30)
    theater_name.grid(row=1, column=1, padx=20)

    theater_seatCapacity = Entry(h1_frame, width=30)
    theater_seatCapacity.grid(row=3, column=1)

    delete_box = Entry(h1_frame, width=30)
    delete_box.grid(row=12, column=1, pady=5)

    # creating labels for the text boxes ~~~~~~~~~~~~~~~
    theater_id_label = Label(h1_frame, text="Theater ID")
    theater_id_label.grid(row=0, column=0, pady=(10, 0))

    theater_name_label = Label(h1_frame, text="Theater Name")
    theater_name_label.grid(row=1, column=0)

    theater_seatCapacity_label = Label(h1_frame, text="Seat Capacity")
    theater_seatCapacity_label.grid(row=3, column=0)

    delete_label = Label(h1_frame, text="Select Theater ID")
    delete_label.grid(row=12, column=0, pady=5)

    # create a submit button ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    submit_button = Button(h1_frame, text="Add Theater Info Record To Database", command=submit1)
    submit_button.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=120)

    # create a query button to see the Theater table information
    query_button = Button(h1_frame, text="Show Theater Info Records", command=query1)
    query_button.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=147)

    # create a delete button to delete a Theater's record from the table
    delete_button = Button(h1_frame, text="Delete a Theater's Info Records", command=delete1)
    delete_button.grid(row=13, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

    # create an edit button to update/edit a Theater's info record
    edit_button = Button(h1_frame, text="Edit a Theater's Info Records", command=edit1)
    edit_button.grid(row=14, column=0, columnspan=2, pady=10, padx=10, ipadx=142)
    h2_frame.pack(pady=20)

# commit changes
conn.commit()
# close connection
conn.close()



options_frame=tk.Frame(root2, bg="#c3c3c3")

current_btn=tk.Button(options_frame,text="Home",font=('Bold',20),fg='#128aff', bd=0,bg='#c3c3c3',command=lambda :indicate(current_indicate,home_page))
current_btn.place(x=10,y=60)
current_indicate=tk.Label(options_frame, text='', bg='#c3c3c3')
current_indicate.place(x=3,y=60,width=5, height=40)

History_btn=tk.Button(options_frame,text="Menu",font=('Bold',20),fg='#128aff', bd=0,bg='#c3c3c3' ,command=lambda :indicate(history_indicate,history_page))
History_btn.place(x=10,y=130)
history_indicate=tk.Label(options_frame, text='', bg='#c3c3c3')
history_indicate.place(x=3,y=130,width=5, height=40)

add_btn=tk.Button(options_frame,text="Add",font=('Bold',20),fg='#128aff', bd=0,bg='#c3c3c3' ,command=lambda :indicate(history_indicate,hi))
add_btn.place(x=10,y=190)
add_indicate=tk.Label(options_frame, text='', bg='#c3c3c3')
add_indicate.place(x=3,y=190,width=5, height=40)

theater_btn=tk.Button(options_frame,text="Theaters",font=('Bold',20),fg='#128aff', bd=0,bg='#c3c3c3' ,command=lambda :indicate(history_indicate,h2))
theater_btn.place(x=10,y=250)
theater_indicate=tk.Label(options_frame, text='', bg='#c3c3c3')
theater_indicate.place(x=3,y=190,width=5, height=40)

exit_btn=tk.Button(options_frame,text="logout",font=('Bold',20),fg='#128aff', bd=0,bg='#c3c3c3',command=lambda :indicate(exit_indicate,exit_page))
exit_btn.place(x=10,y=600)
exit_indicate=tk.Label(options_frame, text='', bg='#c3c3c3')
exit_indicate.place(x=3,y=600,width=5, height=40)


options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=160, height=1200)

main_frame=tk.Frame(root2,highlightbackground="black",highlightthickness=2)
main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=1000,width=1200)
root2.mainloop()