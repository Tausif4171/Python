from tkinter import *

class MyButton:
    def __init__(self,root):
        
        self.f=Frame(root,height=400,width=500)
        
        self.f.propagate(0)
        
        self.f.pack()
        
        self.b1=Button(self.f, text='Red',width=15,height=2,command=lambda: self.buttonClick(1))
        self.b2=Button(self.f, text='Blue',width=15,height=2,command=lambda: self.buttonClick(2))
        self.b3=Button(self.f, text='Green',width=15,height=2,command=lambda: self.buttonClick(3))
        
        self.b1.pack()
        self.b2.pack()
        self.b3.pack()

def buttonClick(self,num):
    if num==1:
        self.f["bg"]='red'
    if num==2:
        self.f["bg"]='blue'
    if num==3:
        self.f["bg"]='green'

        
root=Tk()
mb=MyButton(root,buttonClick)
root.mainloop()
        
