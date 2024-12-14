from tkinter import*
from tkinter import ttk
from tkinter import ttk, font,messagebox


   
#BANK APPLICATION : 

def submit(win):
 win.destroy()





#LOGIN-PAGE : 
win=Tk()
win.config(bg="grey")
win.title("INDIAN BANK")
win.geometry("1400x1200")
# Frame:
frame1=Frame(win,width=800,height=500,bg="pink",highlightthickness=5,highlightbackground="hotpink",highlightcolor="blue")
frame1.place(relx=0.2,rely=0.1)
#Label :
label=Label(win,text="LOGIN_PAGE",fg="black",font=("times",20,"bold"),bg="lavender")
label.place(relx=0.45,rely=0.15)
label1=Label(win,text="Enter Your Account Number : ",fg="black",font=("times",15,"bold"),bg="pink")
label1.place(relx=0.35,rely=0.3)
label2=Label(win,text="Enter Your Password Number : ",fg="black",font=("times",15,"bold"),bg="pink")
label2.place(relx=0.35,rely=0.4)
label3=Label(win,text="Create Account",bg="pink",fg="blue",font=("times",15,"bold"))
label3.place(relx=0.25,rely=0.75)
label4=Label(win,text="Forget Password",bg="pink",fg="blue",font=("times",15,"bold"))
label4.place(relx=0.65,rely=0.75)
#Input or Entry :
input1=Entry(win,font=("times",15,"bold"))
input1.place(relx=0.58,rely=0.3)
input2=Entry(win,font=("times",15,"bold"))
input2.place(relx=0.58,rely=0.4)
#Button:
button1=Button(win,text="Submit",font=("times",15,"bold"),bg="green",fg="white",overrelief="ridge",activebackground="lightgreen",activeforeground="green",command=lambda:submit())
button1.place(relx=0.45,rely=0.55)
button2=Button(win,text="Clear",font=("times",15,"bold"),bg="red",fg="white",overrelief="groove",activebackground="orange",activeforeground="red",command=lambda:delete())
button2.place(relx=0.55,rely=0.55)
# def Fubnction in python:
def submit():
    newfile=open("tkintersretxt.txt","a")
    a=input1.get()
    b=input2.get()
    newfile.write("\n"+a+"\t"+b)
#clear:
def delete():
    a=input1.delete(0,END)
    b=input2.delete(0,END)

win.mainloop()


