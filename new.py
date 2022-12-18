#It is used to add new details inro the table
from tkinter import *
from tkinter import ttk
import mysql.connector
from PIL import Image,ImageTk
import cv2 
import os
root = Tk()
root.title("SlySneak")
root.attributes('-fullscreen',True)
root.geometry("200x200")
conn=mysql.connector.connect(host="localhost",user='root',password='chinnu11',database="slysneak")
cursor1=conn.cursor()
def user():         
    person = str(m.get())
    email = str(n.get())
    os.makedirs('images/'+person)
    path = './images/'+person+'/img.jpg'
    image = Image.fromarray(frame1)
    image.save(path)
    insert_stml=("INSERT INTO SLYSNEAK(FULLNAME,EMAIL,IMAGE_PATH) VALUES(%s,%s,%s)")
    data= (person,email,path) 
    cursor1.execute(insert_stml,data)
    conn.commit()
    master1.destroy()
    master2 = Tk()
    master2.title("SlySneak")
    lb = Label(master2,text="Information recorded")
    lb.pack()
    master2.geometry("300x300")
    master2.mainloop()


def newwindow():
    root.destroy()
    video = cv2.VideoCapture(0)
    global master1
    master1 = Tk()
    master1.title("SlySneak")
    width= master1.winfo_screenwidth()               
    height= master1.winfo_screenheight()              
    master1.geometry("%dx%d" % (width, height))
    label1 =Label(master1,text="Enter email id: ")
    label1.place(relx=0.1,rely=0.5)
    global n
    n = Entry(master1,width = 40,borderwidth = 5)
    n.place(relx=0.3, rely=0.5, anchor=CENTER)
    global btn
    global f1
    f1 = LabelFrame(master1,bg="white")
    f1.place(x=850,y=30)
    global L1
    L1 = Label(f1,bg="white")
    L1.pack()
    button4 = Button(master1,text ="Take a pic",command = user,padx =40,pady =20,borderwidth = 10)
    button4.place(x=900, y=550)
    global mylabel
    mylabel = Label(master1,text ="Enter full name:")
    mylabel.place(relx=0.1, rely=0.3, anchor=CENTER)
    global m
    m = Entry(master1,width = 40,borderwidth = 5)
    m.place(relx=0.3, rely=0.3, anchor=CENTER)
    while True:
        frame = video.read()[1]
        global frame1
        frame1 = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        frame3 = ImageTk.PhotoImage(Image.fromarray(frame1))
        L1['image'] = frame3
        master1.update()
    master1.mainloop()
button1 = Button(root,text ="Add User",padx =30,pady =20,command = newwindow,borderwidth = 10)
button2 = Button(root,text ="Log Details",padx =40,pady =20,command = newwindow,borderwidth = 10)
button1.place(x=500, y=350)
button2.place(x=900, y=350)
root.mainloop()
