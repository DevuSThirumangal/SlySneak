from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import cv2
import face_recognition
import mysql.connector
#import new
import smtplib,ssl
def user():
    conn=mysql.connector.connect(host="localhost",user='root',password='chinnu11',database="slysneak")
    cursor=conn.cursor() 
    path = './images/temp/img.jpg'
    image = Image.fromarray(frame1)
    image.save(path)
    cursor.execute("select image_path from slysneak")
    record = cursor.fetchall()
    for x in record:
        img1 = face_recognition.load_image_file(x[0])
        face_location1 = face_recognition.face_encodings(img1)[0]
        img2 = face_recognition.load_image_file(path)
        face_location2 = face_recognition.face_encodings(img2)[0]
        results = face_recognition.compare_faces([face_location1],face_location2)
        if results[0]:
            des()
def des():
    root.destroy()
    #exec(open("new.py").read())
root = Tk()
root.title("SlySneak")
root.attributes('-fullscreen',True)
video = cv2.VideoCapture(0)
global f1
f1 = LabelFrame(root,bg="white")
f1.place(x=450,y=30)
f1.config(width=1000)
global L1
L1 = Label(f1,bg="white")
L1.pack()
button4 = Button(root,text ="Check",command = user,padx =40,pady =20,borderwidth = 10)
button4.place(x=650, y=550)
while True:
        frame = video.read()[1]
        global frame1
        frame1 = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        frame = ImageTk.PhotoImage(Image.fromarray(frame1))
        L1['image'] = frame
        root.update()
root.mainloop()
