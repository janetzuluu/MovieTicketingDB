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

# creating table for user info ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
c.execute("""CREATE TABLE USER_INFO (
        USER_ID integer primary key,
        USER_FNAME text,
        USER_LNAME text,
        USER_PHONE integer,
        USER_EMAIL varchar,
        USER_AGE integer,
        USER_PAY integer, 
        USER_HIST money
        )""")
'''

# creating the submit function for the submit_button
def submit():
    conn = sqlite3.connect('theater_ticketing.db')
    c = conn.cursor()

    # insert data into the user_info table
    c.execute("INSERT INTO USER_INFO VALUES (:user_id, :first_name, :last_name, :phone_num, :email_addr, :age, :pay, :history)",
              {
                  'user_id': user_id.get(),
                  'first_name': first_name.get(),
                  'last_name': last_name.get(),
                  'phone_num': phone_num.get(),
                  'email_addr': email_addr.get(),
                  'age': age.get(),
                  'pay': pay.get(),
                  'history': history.get()
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

#create a sql query function for the query button
def query():
    conn = sqlite3.connect('theater_ticketing.db')
    c = conn.cursor()

    #oid here means everything and the primary key
    c.execute("SELECT *, oid FROM USER_INFO")

    User_Records = c.fetchall()
    # print(User_Records)
    print_records = ''

# looping through all user info 'show record' query
    for record in User_Records:
        print_records += str(record) +" "

    query_label = Label(root, text=print_records)
    query_label.grid(row=10, column=0, columnspan=2)

    conn.commit()
    conn.close()


# creating the text boxes ~~~~~~~~~~~~~~~~~~~~~
user_id = Entry(root, width=30)
user_id.grid(row=0, column=1, padx=20)

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

# creating labels for the text boxes ~~~~~~~~~~~~~~~
user_id_label = Label(root, text="User ID")
user_id_label.grid(row=0, column=0)

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

# create a submit button ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
submit_button = Button(root, text="Add User Info Record To Database", command=submit)
submit_button.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# create a query button to see the user table information
query_button = Button(root, text="Show User Info Records", command=query)
query_button.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=137)



# commit changes
conn.commit()
# close connection
conn.close()
root.mainloop()


