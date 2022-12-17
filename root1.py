from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import cv2 
import os
root = Tk()
root.title("SlySneak")
root.attributes('-fullscreen',True)
root.geometry("200x200")
facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
def user():
    person = m.get()
    print(person)
    #os.makedirs('images/'+person)
    #path = './images/'+person+'/img.jpg'
    #while True:
    #    faces = facedetect.detectMultiScale(f1,1.3,5)
    #    for x,y,w,h in faces:
    #        nameloc = './images/'+person+'/img.jpg'
    #        cv2.imwrite(nameloc, f1[y:y+h,x:x+h])
    #    break

def newwindow():
    root.destroy()
    video = cv2.VideoCapture(0  )
    master1 = Tk()
    master1.title("SlySneak")
    width= master1.winfo_screenwidth()               
    height= master1.winfo_screenheight()              
    master1.geometry("%dx%d" % (width, height))
    label1 =Label(master1)
    label1.place(relx=0.8, rely=0.3, anchor=CENTER)
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
    button3 = Button(master1,text ="   Enter   ",command = user,padx =40,pady =20,borderwidth = 10)
    button3.place(x=650, y=200)
    while True:
        frame = video.read()[1]
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        frame = ImageTk.PhotoImage(Image.fromarray(frame))
        L1['image'] = frame
        master1.update()
    master1.mainloop()
button1 = Button(root,text ="   Admin   ",padx =30,pady =20,command = newwindow,borderwidth = 10)
button2 = Button(root,text ="Other user",padx =40,pady =20,command = newwindow,borderwidth = 10)
button1.place(x=500, y=350)
button2.place(x=900, y=350)
root.mainloop()
