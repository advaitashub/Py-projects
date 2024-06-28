from tkinter import *
import random
from tkinter import messagebox

class Pass:
    # FIRST PAGE

    def __init__(self,root):
        self.root=root
        self.root.title("PASS-GENERATOR")
        self.root.geometry('650x450+300+100')
        Label(self.root, text="PASSWORD GENERATOR", fg="gold", bg="black",font= "arial, 35 bold").pack(side='top',fill=BOTH)
        self.bottom=Frame(root,height=500, bg="gold", bd="8", relief=GROOVE)
        self.bottom.pack(fill=X)
        self.first_page()
    

    def first_page(self):
        fi=Frame(self.root,height= 340, width=390, bg="black",bd=15, relief=GROOVE)
        fi.place(x=120,y=80)
        fj=Frame(fi,height= 300, width=350,bd=8, bg="grey" ,relief=GROOVE)
        fj.place(x=6,y=6)

        Label(fj, text="DO YOU WANT TO GENERATE \n A PASSWORD FOR YOUR \n ACCOUNT? ", fg="black",bg="gold",font= "arial, 15 bold").place(x=8, y=20 )
        Radiobutton(fj, text="yes", fg="blue", value="0",font="sherif, 20 bold", bg="yellow", command=self.Yes).place(x=40,y=120)
        Radiobutton(fj, text="no", fg= "blue", value ="1",font="sherif, 20 bold",bg="yellow", command=self.No).place(x=40,y=180)


#===================== RADIOBUTTON FUNCTIONS=====================#

    # ON CLICKING NO
    def No(self):
        self.msg=messagebox.askyesno("MESSAGE", "ARE YOU SURE?")
        
    
    # ON CLICKING YES
    def Yes(self):
        
        # FRAMES | LABELS | BUTTONS
        fi=Frame(self.root ,height= 340, width=390, bg="red",bd=15, relief=GROOVE)
        fi.place(x=120,y=80)
        fj=Frame(fi,height= 300, width=350,bd=8 ,relief=GROOVE)
        fj.place(x=6,y=6)
        Label(fj, text="WHAT SHOULD BE THE LENGTH OF \nYOUR PASSWORD? PLEAS ENTER", fg="black",font= "arial, 13").place(x=20, y=10)
        self.name_1=Entry(fj,bd=3, font= "aerial, 18 bold")
        self.name_1.place(x=80, y=60, height=40, width=170)
        Label(fj, text="YOUR PASSWORD IS: ", fg="black",font= "arial, 13").place(x=20, y=120)
        self.main_text =Listbox(self.root, height=1,bd =5, width =15,bg="sky blue",font= "aerial, 20 bold")
        self.main_text.place(x=205, y=260)

        btn=Button(fj,text="SUBMIT",width=10, font="arial 15 bold", bd=4, relief= GROOVE, bg= "orange" , command=self.pg)
        btn.place(x=180, y= 220)
        btn2=Button(fj,text="NEW",width=10, font="arial 15 bold", bd=4, relief= GROOVE, bg= "orange", command=self.Yes)
        btn2.place(x=10, y= 220)

    #SUBMIT BUTTON FUNCTION
    def add(self):
        content = self.name_1.get()
        with open(r"C:\Users\singh\OneDrive\Documents\passkey.txt",'a') as file:
            file.write(content)
            file.seek(0)
            file.close()
            return int(content)


     # ENTERING DATA AND GENERATING PASS KEY
    def pg(self):

        self.label3=Label(self.root, text="YOUR PASWORD IS: ", fg="black",font= "arial, 15")
        m="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        n= self.add()
        r= random.sample(m,n)
        self.main_text.insert(0, r)


    


def main():
    root=Tk()
    ui=Pass(root)
    root.mainloop()

if __name__=="__main__":
  main()





