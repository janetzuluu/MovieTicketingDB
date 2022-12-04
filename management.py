import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
root2 = tk.Tk()
root2.title("Management")
root2.geometry('1000x1200')
def home_page():
    current_frame=tk.Frame(main_frame)
    lb=tk.Label(current_frame,text='Current Page\n\nPage: 1',font=('Bold', 30))
    lb.pack()
    current_frame.pack(pady=20)
def history_page():
    history_frame=tk.Frame(main_frame)

    lb=tk.Label(history_frame,text='History Page\n\nPage: 2',font=('Bold', 30))
    lb.pack()
    history_frame.pack(pady=20)
def exit_page():
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

options_frame=tk.Frame(root2, bg="#c3c3c3")

current_btn=tk.Button(options_frame,text="Home",font=('Bold',20),fg='#128aff', bd=0,bg='#c3c3c3',command=lambda :indicate(current_indicate,home_page))
current_btn.place(x=10,y=60)
current_indicate=tk.Label(options_frame, text='', bg='#c3c3c3')
current_indicate.place(x=3,y=60,width=5, height=40)

History_btn=tk.Button(options_frame,text="Menu",font=('Bold',20),fg='#128aff', bd=0,bg='#c3c3c3' ,command=lambda :indicate(history_indicate,history_page))
History_btn.place(x=10,y=130)
history_indicate=tk.Label(options_frame, text='', bg='#c3c3c3')
history_indicate.place(x=3,y=130,width=5, height=40)

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