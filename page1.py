from tkinter import *
from tkinter import ttk
import mysql.connector
from mysql.connector.errors import Error

from os import getcwd

win = Tk()
win.geometry("635x485")

#--------------back_end---------------------#


#show and hide password
def show_pas():
    password_box.config(show  = "")


#next page
def next_page():
    win.destroy()
    import passproject


# connect to database
def connect_mysql():
    global mydb
    global my_cursor

    try:
        mydb = mysql.connector.connect(host = host_box.get(),user = username_box.get(), password = password_box.get())
        my_cursor = mydb.cursor()
        my_cursor.execute("CREATE DATABASE IF NOT EXISTS save_password")
        my_cursor.execute("use save_password")
        my_cursor.execute('''create table if not exists private(platform varchar(20),
        username varchar(300),
        password varchar(50) )''')

        if mysql:
            connect_label.config(text = "your connect to mysql")

    except mysql.connector.Error as err:
        connect_label.config(text = "Something went wrong please try again")

#--------------------GUI---------------------#


#side_frame
img_label  = PhotoImage(file = getcwd() + "/img" "/label.png")
frame_side = Frame(win,bg = "white")
frame_side.place(x = 0 , y = 0, height=500 , width= 150)
Label(frame_side,image = img_label, bg="white").place(x = -5 , y = -12,height=530, width=155)


#center_frame
center_frame = Frame(win,bg = "white")
center_frame.place(x =150 ,y = 0, width= 500, height=500)


#title_label
ttk.Label(center_frame,text = "please enter your host and your username and your password", foreground="skyblue2",background="white", font= "dyuthi 10 bold").place(x = 15 , y = 15)

#connect_label
connect_label = ttk.Label(center_frame,text = "", foreground="skyblue1",background="white", font= "dyuthi 10")
connect_label.place(x = 20 , y = 370)

#label and entry for input your values
ttk.Label(center_frame,text = "Host:", foreground="skyblue2",background="white", font= "dyuthi 13 bold").place(x = 20 , y = 130)
host_box = Entry(center_frame, background = "white",foreground="darkgreen", highlightbackground= "darksalmon",highlightcolor="blue",font= "Tahoma 10 bold")
host_box.place(x = 150 , y = 120,height=35, width= 200)

ttk.Label(center_frame,text = "Username:", foreground="skyblue2",background="white", font= "dyuthi 13 bold").place(x = 20 , y = 180 )
username_box = Entry(center_frame, background = "white",foreground="darkgreen", highlightbackground= "darksalmon",highlightcolor="blue",font= "Tahoma 10 bold")
username_box.place(x = 150 , y = 170,height=35, width= 200)

ttk.Label(center_frame,text = "Password:", foreground="skyblue2",background="white", font= "dyuthi 13 bold").place(x = 20 , y = 230)
password_box = Entry(center_frame, background = "white",foreground="darkgreen", highlightbackground= "darksalmon",highlightcolor="blue",font= "Tahoma 10 bold",show="*")
password_box.place(x = 150 , y = 220,height=35, width= 200)


#image_button
next_img = PhotoImage(file = getcwd() + "/img"+ "/button_page1.png")
connect_img = PhotoImage(file = getcwd() + "/img"+ "/button2.png")


#button
connect_btn = Button(center_frame,image = connect_img, bg= "white" ,highlightbackground= "white", activebackground= "white" , borderwidth= 0,command=connect_mysql)
connect_btn.place(x = 20, y = 330)
next_btn = Button(center_frame,image = next_img, bg= "white" ,highlightbackground= "white", activebackground= "white" , borderwidth= 0 ,command= next_page)
next_btn.place(x = 360, y = 330)

# secure button
img_show = PhotoImage(file = getcwd() + "/img"+ "/images.png")
show_btn = Button(center_frame,image = img_show,bg = "white", borderwidth=0, activebackground="white", highlightbackground="white",command= show_pas).place(x = 350 , y = 221)

win.mainloop()
