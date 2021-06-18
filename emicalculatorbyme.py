import tkinter as tk
from tkinter import*
#from tkinter import messagebox

class LoanCalculator:
        

    def __init__(self):
        
        self.win=Tk()
        self.win.geometry("1000x626")
        self.win.title("EMI CALCULATOR")
        img=PhotoImage(file="finance.png")
        Label(self.win,image=img).pack(side=RIGHT)
        self.l2=Label(self.win,font=("times new roman",24,'bold'),text="Loan Amount",fg="black").place(x=90,y=50)
        self.e1=DoubleVar()
        Entry(self.win,textvariable=self.e1,width=50).place(x=50,y=120)
        self.l3=Label(self.win,font=("times new roman",24,'bold'),text="Interest Per Annum",fg="black").place(x=60,y=150)
        self.e2=DoubleVar()
        Entry(self.win,textvariable=self.e2,width=50).place(x=50,y=210)
        self.l4=Label(self.win,font=("times new roman",24,'bold'),text="Period In Months",fg="black").place(x=90,y=250)
        self.e3=DoubleVar()
        Entry(self.win,textvariable=self.e3,width=50).place(x=50,y=300)
        self.b2=Button(self.win,text="Click To Calculate",font=("times new roman",13,'bold'),cursor="hand2",bg="blue",fg="white",command=lambda:self.calculate()).place(x=110,y=350)
        self.win.mainloop()
        
    def calculate(self):
        p=self.e1.get()
        r=self.e2.get()
        n=self.e3.get()
        e=p*(r/1200)*((1+r/1200)**n)/(((1+r/1200)**n)-1)
        Label(self.win,text=e,font=("times new roman",24,'bold')).place(x=50,y=400)

lc=LoanCalculator()

