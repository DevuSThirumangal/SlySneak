from tkinter import *
root = Tk()
root.title("SlySneak")
root.attributes('-fullscreen',True)
#root.geometry("x200")
def user():
    #n =m.get()
    #print(n)
    return
def newwindow():
    root.destroy()
    master1 = Tk()
    master1.title("SlySneak")
    master1.geometry("200x200")
    #label1 = Label(master1,text ="",padx =40,pady =20,command = user,borderwidth = 10)
    mylabel = Label(master1,text ="Enter full name:")
    mylabel.place(relx=0.3, rely=0.5, anchor=CENTER)
    m = Entry(master1,width = 40,borderwidth = 5)
    m.place(relx=0.5, rely=0.5, anchor=CENTER)
    label= Label(master1, text="", font=('Helvetica 13'))
    label.pack()
    button3 = Button(master1,text ="   Enter   ",command = get_data,padx =40,pady =20,borderwidth = 10)
    button3.place(x=1000, y=350)
    m1 = str(m.get())
    label= Label(master1, text="", font=('Helvetica 13'))
    label.pack()
    master1.mainloop()
def Button_add():
  return;
def get_data():
    label.config(text= m.get(), font= ('Helvetica 13'))
button1 = Button(root,text ="   Admin   ",padx =40,pady =20,command = newwindow,borderwidth = 10)
button2 = Button(root,text ="Other user",padx =40,pady =20,command = newwindow,borderwidth = 10)
button1.place(x=500, y=350)
button2.place(x=900, y=350)
root.mainloop()
