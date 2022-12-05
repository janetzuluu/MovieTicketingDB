from tkinter import *
# from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title('Theater E-Ticket Info')
root.geometry("500x600")

# database------------------

# creating a database
conn = sqlite3.connect('theater_ticketing.db')

# cursor creation
c = conn.cursor()

# creating table for user info ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
c.execute("""CREATE TABLE IF NOT EXISTS USER_INFO (
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
'''


def update():
    conn = sqlite3.connect('theater_ticketing.db')
    c = conn.cursor()

    record_select_id = delete_box.get()
    c.execute("""UPDATE USER_INFO SET
        USER_ID = :ID,
        USER_FNAME = :FIRST,
        USER_LNAME = :LAST,
        USER_PHONE = :PHONE,
        USER_EMAIL = :EMAIL,
        USER_AGE = :AGE,
        USER_PAY = :PAY, 
        USER_HIST = :HIST,
        USER_PASS = :PASS

        WHERE USER_ID = :SELECTED_ID""",
              {
                  'ID': user_id_edit.get(),
                  'FIRST': first_name_edit.get(),
                  'LAST': last_name_edit.get(),
                  'PHONE': phone_num_edit.get(),
                  'EMAIL': email_addr_edit.get(),
                  'AGE': age_edit.get(),
                  'PAY': pay_edit.get(),
                  'HIST': history_edit.get(),
                  'PASS': password_edit.get(),
                  'SELECTED_ID': record_select_id
              })

    conn.commit()
    conn.close()

    editor.destroy()


# edit/updates a user's info record
def edit():
    global editor
    editor = Tk()
    editor.title('Edit User Record Info')
    editor.geometry("550x400")
    conn = sqlite3.connect('theater_ticketing.db')
    c = conn.cursor()

    record_id = delete_box.get()

    # query here means everything and the primary key
    c.execute("SELECT * FROM USER_INFO WHERE USER_ID =" + record_id)

    user_records = c.fetchall()

    # create the text box namee edits to global variables
    global user_id_edit
    global first_name_edit
    global last_name_edit
    global phone_num_edit
    global email_addr_edit
    global age_edit
    global pay_edit
    global history_edit
    global password_edit

    # creating the text boxes ~~~~~~~~~~~~~~~~~~~~~
    user_id_edit = Entry(editor, width=30)
    user_id_edit.grid(row=0, column=1, padx=20, pady=(10, 0))

    first_name_edit = Entry(editor, width=30)
    first_name_edit.grid(row=1, column=1, padx=20)

    last_name_edit = Entry(editor, width=30)
    last_name_edit.grid(row=2, column=1)

    phone_num_edit = Entry(editor, width=30)
    phone_num_edit.grid(row=3, column=1)

    email_addr_edit = Entry(editor, width=30)
    email_addr_edit.grid(row=4, column=1)

    age_edit = Entry(editor, width=30)
    age_edit.grid(row=5, column=1)

    pay_edit = Entry(editor, width=30)
    pay_edit.grid(row=6, column=1)

    history_edit = Entry(editor, width=30)
    history_edit.grid(row=7, column=1)

    password_edit = Entry(editor, width=30)
    password_edit.grid(row=8, column=1)

    # creating labels for the text boxes ~~~~~~~~~~~~~~~
    user_id_label = Label(editor, text="User ID")
    user_id_label.grid(row=0, column=0, pady=(10, 0))

    first_name_label = Label(editor, text="First Name")
    first_name_label.grid(row=1, column=0)

    last_name_label = Label(editor, text="Last Name")
    last_name_label.grid(row=2, column=0)

    phone_num_label = Label(editor, text="Phone Number")
    phone_num_label.grid(row=3, column=0)

    email_addr_label = Label(editor, text="Email Address")
    email_addr_label.grid(row=4, column=0)

    age_label = Label(editor, text="Age")
    age_label.grid(row=5, column=0)

    pay_label = Label(editor, text="Payment Card")
    pay_label.grid(row=6, column=0)
    # maybe dont allow admin to edit the payment???
    # TODO add the payments to history automatically
    history_label = Label(editor, text="Payment History")
    history_label.grid(row=7, column=0)

    password_label= Label(editor, text="Password")
    password_label.grid(row=8, column=0)

    # go through our record data and update them by looping
    for record in user_records:
        user_id_edit.insert(0, record[0])
        first_name_edit.insert(0, record[1])
        last_name_edit.insert(0, record[2])
        phone_num_edit.insert(0, record[3])
        email_addr_edit.insert(0, record[4])
        age_edit.insert(0, record[5])
        pay_edit.insert(0, record[6])
        history_edit.insert(0, record[7])
        password_edit.insert(0, record[8])

    # creates a save button to save the edits/updates done on the user's record information
    save_button = Button(editor, text="Save User's Info Records", command=update)
    save_button.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

    # conn.commit()
    # conn.close()


# create a function that deletes a user's info record from the user_info table
def delete():
    conn = sqlite3.connect('theater_ticketing.db')
    c = conn.cursor()

    # delete a user record
    c.execute("DELETE from USER_INFO WHERE USER_ID = " + delete_box.get())

    delete_box.delete(0, END)

    conn.commit()
    conn.close()


# creating the submit function for the submit_button
def submit():
    conn = sqlite3.connect('theater_ticketing.db')
    c = conn.cursor()

    # insert data into the user_info table
    c.execute(
        "INSERT INTO USER_INFO VALUES (:user_id, :first_name, :last_name, :phone_num, :email_addr, :age, :pay, :history, :password)",
        {
            'user_id': user_id.get(),
            'first_name': first_name.get(),
            'last_name': last_name.get(),
            'phone_num': phone_num.get(),
            'email_addr': email_addr.get(),
            'age': age.get(),
            'pay': pay.get(),
            'history': history.get(),
            'password': password.get()
        })

    conn.commit()
    conn.close()

    # clear the text boxes before/after each submit
    user_id.delete(0, END)
    first_name.delete(0, END)
    last_name.delete(0, END)
    phone_num.delete(0, END)
    email_addr.delete(0, END)
    age.delete(0, END)
    pay.delete(0, END)
    history.delete(0, END)
    password.delete(0, END)


# create a sql query function for the query button
def query():
    conn = sqlite3.connect('theater_ticketing.db')
    c = conn.cursor()

    # query here means everything and the primary key
    c.execute("SELECT * FROM USER_INFO")

    user_records = c.fetchall()
    # print(User_Records)
    print_records = ''

    # looping through all user info 'show record' query
    for record in user_records:
        print_records += str(record[0]) + "  " + str(record[1]) + "  " + str(record[2]) + "  " + str(record[3]) + "  " \
                         + str(record[4]) + "  " + str(record[5]) + "  " + str(record[6]) + "  " + str(record[7]) + "  " \
                         + str(record[8]) +" \n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=11, column=0, columnspan=2)

    conn.commit()
    conn.close()


# creating the text boxes ~~~~~~~~~~~~~~~~~~~~~
user_id = Entry(root, width=30)
user_id.grid(row=0, column=1, padx=20, pady=(10, 0))

first_name = Entry(root, width=30)
first_name.grid(row=1, column=1, padx=20)

last_name = Entry(root, width=30)
last_name.grid(row=2, column=1)

phone_num = Entry(root, width=30)
phone_num.grid(row=3, column=1)

email_addr = Entry(root, width=30)
email_addr.grid(row=4, column=1)

age = Entry(root, width=30)
age.grid(row=5, column=1)

pay = Entry(root, width=30)
pay.grid(row=6, column=1)

history = Entry(root, width=30)
history.grid(row=7, column=1)

password = Entry(root, width=30)
password.grid(row=8, column=1)

delete_box = Entry(root, width=30)
delete_box.grid(row=12, column=1, pady=5)

# creating labels for the text boxes ~~~~~~~~~~~~~~~
user_id_label = Label(root, text="User ID")
user_id_label.grid(row=0, column=0, pady=(10, 0))

first_name_label = Label(root, text="First Name")
first_name_label.grid(row=1, column=0)

last_name_label = Label(root, text="Last Name")
last_name_label.grid(row=2, column=0)

phone_num_label = Label(root, text="Phone Number")
phone_num_label.grid(row=3, column=0)

email_addr_label = Label(root, text="Email Address")
email_addr_label.grid(row=4, column=0)

age_label = Label(root, text="Age")
age_label.grid(row=5, column=0)

pay_label = Label(root, text="Payment Card")
pay_label.grid(row=6, column=0)
# maybe dont allow admin to edit the payment???
# TODO add the payments to history automatically
history_label = Label(root, text="Payment History")
history_label.grid(row=7, column=0)

password_label = Label(root, text="Password")
password_label.grid(row=8, column=0)

delete_label = Label(root, text="Select User ID")
delete_label.grid(row=12, column=0, pady=5)

# create a submit button ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
submit_button = Button(root, text="Add User Info Record To Database", command=submit)
submit_button.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=120)

# create a query button to see the user table information
query_button = Button(root, text="Show User Info Records", command=query)
query_button.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=147)

# create a delete button to delete a user's record from the table
delete_button = Button(root, text="Delete a User's Info Records", command=delete)
delete_button.grid(row=13, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

# create an edit button to update/edit a user's info record
edit_button = Button(root, text="Edit a User's Info Records", command=edit)
edit_button.grid(row=14, column=0, columnspan=2, pady=10, padx=10, ipadx=142)

# commit changes
conn.commit()
# close connection
conn.close()
root.mainloop()