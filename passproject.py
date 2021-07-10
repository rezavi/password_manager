from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
from page1 import *
import random

win = Tk()
win.geometry("635x485")

#-----------------back_end-----------------------#
#clear entry _box
def clear_box():

    platform_box.delete(0,END)
    username_box.delete(0,END)
    password_box.delete(0,END)

#-----------Genrate Page----------#
def generate_page():
    global generate_entry
    win = Tk()
    win.geometry("500x300")
    win.config(bg = "white") 
    win.title("search platform ")

    def generate_password():

        num = int(number_entry.get())
        word = "".join([chr(65 + i) for i in range(26)])
        number = "".join([str(i) for i in range(1, 10)])
        symbol = [".", "_", "-"]
        word_num = []
        while len(word_num) != num:
            word_num.append("".join(random.choices(word, k=1)))
            word_num.append("".join(random.choices(number, k=1)))
            word_num.append("".join(random.choices(symbol, k=1)))
            
            if len(word_num) >= num:
                a = len(word_num) - num
                for j in range(0,a):
                    word_num.pop()


        generate_entry.insert(0 , "".join(word_num))




    generate_entry = Entry(win, bg = "white", fg = "black",highlightbackground="darksalmon",font = "Tahoma 10 bold")
    generate_entry.place(x = 180 , y = 170,height=35)

    number_entry = Entry(win, bg = "white", fg = "black")
    number_entry.place(x = 230,y = 120, height= 25, width=25)

    generate_button = Button(win , text = "genrate_password",bg = "white", fg = "black",command = generate_password,font = "Tahoma 10 bold",activebackground="darksalmon",activeforeground="white")
    generate_button.place(x = 20 , y = 170)

    generate_label = Label(win , text = "number of generate password: ",bg = "white", fg = "black",font = "Tahoma 9 bold",)
    generate_label.place(x = 20 , y = 120)

    top_frame = Frame(win,bg = "darksalmon")
    top_frame.place(x = 0 , y = 0,height= 80,width=500)

    Label(win,text = "Strong   your   password" ,bg="darksalmon",font = "Tahoma 13 bold",fg ="white").place(x = 140 , y = 25)

# insert get value into mysql from entry
def add_form():
    sql_command = "INSERT into private(platform,username,password) values(%s, %s , %s)"
    values = (platform_box.get(),username_box.get(),password_box.get())
    my_cursor.execute(sql_command,values)
    mydb.commit()
    clear_box()



#show and hide password
def show_pas():
    password_box.config(show  = "")


#-----------search page search your user and password by platform-----------#
def search_page():
    win = Tk()
    win.geometry("600x400")
    win.config(bg = "white")
    win.title("search platform ")

    def search_by_platform():
        search  = search_entry.get()
        sql = "SELECT * FROM private WHERE platform = %s"
        name = (search,)
        my_cursor.execute(sql , name)
        a = []
        result = my_cursor.fetchall()
        for i in result:
            a.append(( " " + str(i[0]) + " " + str(i[1]) + "  " + str(i[2]) + " "))
            search_label.config(text  = "\n\n\n".join(a))

    frame_side = Frame(win,bg = "skyblue3")
    frame_side.place(x = 0 , y = 0,height= 180,width=600)

    Label(win,text = "Search user and password by platform" ,bg="skyblue3",font = "Tahoma 13 bold",fg ="white").place(x = 120 , y = 25)
    search_entry = Entry(frame_side, bg = "white", fg = "black",highlightbackground="black",font = "Tahoma 9 bold")
    search_entry.place(x = 170, y = 100,height=35)
    search_button = Button(frame_side , text = "search_platform",bg = "white", fg = "black",activeforeground="white",activebackground ="skyblue4",font = "Tahoma 10 bold",command = search_by_platform)
    search_button.place(x = 20 , y = 100)
    search_label = Label(win , text = "",bg = "white", fg = "skyblue",font = "dyuthi 9 bold")
    search_label.place(x = 20 , y = 200)


#------------GUI_PAGE_2----------#


#side_frame
img_label  = PhotoImage(file = getcwd() + "/img"+ "/label2(1).png")
frame_side = Frame(win,bg = "white")
frame_side.place(x = 0 , y = 0, height=500 , width= 150)
Label(frame_side,image = img_label, bg="white").place(x = -5 , y = -12,height=530, width=155)


#center_frame
center_frame = Frame(win,bg = "white")
center_frame.place(x =150 ,y = 0, width= 500, height=500)


#label and entry for input your values
ttk.Label(center_frame,text = "Platform:", foreground="darksalmon",background="white", font= "dyuthi 12 bold").place(x = 20 , y = 80)
platform_box = Entry(center_frame, background = "white",foreground="red", highlightbackground= "darksalmon",highlightcolor="blue",font= "Tahoma 10 bold")
platform_box.place(x = 150 , y = 70,height=35, width= 200)

ttk.Label(center_frame,text = "username:", foreground="darksalmon",background="white", font= "dyuthi 12 bold").place(x = 20 , y = 140)
username_box = Entry(center_frame, background = "white",foreground="darksalmon", highlightbackground= "darksalmon",highlightcolor="blue",font= "Tahoma 10 bold")
username_box.place(x = 150 , y = 130,height=35, width= 200)

ttk.Label(center_frame,text = "Password:", foreground="darksalmon",background="white", font= "dyuthi 12 bold").place(x = 20 , y = 200)
password_box =Entry(center_frame, background = "white",show = "*",foreground="orange", highlightbackground= "darksalmon",highlightcolor="blue",font= "Tahoma 10 bold")
password_box.place(x = 150 , y = 190,height=35, width= 200)

#create image_button
submit_img = PhotoImage(file = getcwd() + "/img" + "/submit.png")
clear_img = PhotoImage(file = getcwd() + "/img" + "/clear.png")
genrator_img = PhotoImage(file = getcwd() + "/img"+ "/genrator.png")
search_img = PhotoImage(file = getcwd() + "/img" + "/search.png")

#button
submit_btn = Button(center_frame,image = submit_img, bg= "white" ,highlightbackground= "white", activebackground= "white" , borderwidth= 0,command = add_form)
submit_btn.place(x = 20, y = 330)
clear_btn = Button(center_frame,image = clear_img, bg= "white" ,highlightbackground= "white", activebackground= "white" , borderwidth= 0,command = clear_box)
#clear_btn.place(x = 350, y = 330) 

#gerator_btn
genrator_btn = Button(center_frame,image = genrator_img, bg= "white" ,highlightbackground= "white", activebackground= "white" , borderwidth= 0,command = generate_page)
genrator_btn.place(x = 185, y = 330)

#search platform_button
search_btn = Button(center_frame,image = search_img, bg= "white" ,highlightbackground= "white", activebackground= "white" , borderwidth= 0,command = search_page)
search_btn.place(x = 350, y = 330)

# secure button
img_show = PhotoImage(file = getcwd() + "/img" + "/images.png")
show_btn = Button(center_frame,image = img_show,bg = "white", borderwidth=0, activebackground="white", highlightbackground="white",command= show_pas).place(x = 350 , y = 191)

win.mainloop()
