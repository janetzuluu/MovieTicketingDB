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
'''
c.execute("""CREATE TABLE IF NOT EXISTS THEATER (
        THEATER_ID integer primary key,
        THEATER_NAME text,
        THEATER_SEATCAPACITY integer
        )""")
'''

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
def edit():
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
def delete():
    conn = sqlite3.connect('theater_ticketing.db')
    c = conn.cursor()

    # delete a THEATER record
    c.execute("DELETE from THEATER WHERE THEATER_ID = " + delete_box.get())

    delete_box.delete(0, END)

    conn.commit()
    conn.close()


# creating the submit function for the submit_button
def submit():
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
def query():
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

    query_label = Label(root, text=print_records)
    query_label.grid(row=11, column=0, columnspan=2)

    conn.commit()
    conn.close()

# creating the text boxes ~~~~~~~~~~~~~~~~~~~~~
theater_id = Entry(root, width=30)
theater_id.grid(row=0, column=1, padx=20, pady=(10, 0))

theater_name = Entry(root, width=30)
theater_name.grid(row=1, column=1, padx=20)

theater_seatCapacity = Entry(root, width=30)
theater_seatCapacity.grid(row=3, column=1)

delete_box = Entry(root, width=30)
delete_box.grid(row=12, column=1, pady=5)

# creating labels for the text boxes ~~~~~~~~~~~~~~~
theater_id_label = Label(root, text="Theater ID")
theater_id_label.grid(row=0, column=0, pady=(10, 0))

theater_name_label = Label(root, text="Theater Name")
theater_name_label.grid(row=1, column=0)

theater_seatCapacity_label = Label(root, text="Seat Capacity")
theater_seatCapacity_label.grid(row=3, column=0)

delete_label = Label(root, text="Select Theater ID")
delete_label.grid(row=12, column=0, pady=5)

# create a submit button ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
submit_button = Button(root, text="Add Theater Info Record To Database", command=submit)
submit_button.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=120)

# create a query button to see the Theater table information
query_button = Button(root, text="Show Theater Info Records", command=query)
query_button.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=147)

# create a delete button to delete a Theater's record from the table
delete_button = Button(root, text="Delete a Theater's Info Records", command=delete)
delete_button.grid(row=13, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

# create an edit button to update/edit a Theater's info record
edit_button = Button(root, text="Edit a Theater's Info Records", command=edit)
edit_button.grid(row=14, column=0, columnspan=2, pady=10, padx=10, ipadx=142)

# commit changes
conn.commit()
# close connection
conn.close()
root.mainloop()