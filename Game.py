from tkinter import *
from tkinter import PhotoImage
import random
import tkinter as tk

class Game():


    def __init__(self,root=None):
        
        self.root=root
        self.root.title("ROCK-PAPER-SCISSOR-GAME")
        self.root.geometry('510x510+400+50')
        self.root.resizable(False, False)
        global image_path
        image_path= r"C:\Users\singh\Downloads\game.gif"
        global bg_image
        bg_image = PhotoImage(file=image_path)
        self.set_bg_image=Label(root,image= bg_image)
        self.set_bg_image.place(relheight=1, relwidth=1)
        Button(text="LETS PLAY", font= "georgia, 20 bold", bg= "yellow", fg= "black", command=self.main_w, cursor="hand2").place(x="170", y="250")

        self.sum = 0
        self.summ = 0
        self.match_result = None

    

    def rule(self):

     top=tk.Toplevel(self.root)
     top.title("HOW TO PLAY??")
     top.geometry("400x400")
     tk.Label(top, text="HOW TO PLAY??").pack()
     label = Label(top, text="Remember:\n Rock beats scissors, scissors cut paper,\nand paper covers rock. You can use this game to\nsettle minor  decisions or just for fun! 🤘✋✌️\n\n To view score click on score button \nRESET the game to replay")
     label.pack(pady=10)
     btn =tk.Button(top, text="BACK TO GAME!!", command=top.destroy)
     btn.pack(pady=10)
     self.root.mainloop()

    def main_w(self):
        
        self.root.f1=Frame(self.root,height=510, width=510, bg="purple",relief=GROOVE)
        self.root.f1.pack(anchor="center")
        self.root.f1.l1=Button(self.root.f1,text="SCORES", bg="gold", fg= "black", font=" roman 20 bold",cursor= "star",command=self.score).place(x="230")
        self.root.f1.l2=Button(self.root.f1,text="HOW TO PLAY?", bg="RED", fg= "black",height=1, font="segoescript, 10 bold", cursor= "question_arrow", command=self.rule).place(x="0")
        self.root.f1.l3=Button(self.root.f1,text="RESET", bg="red", fg= "black", font="inkfree, 10 bold", cursor= "exchange", command=self.reset_game).place(x="460")

        self.root.f1.text=Listbox(self.root.f1,height=8, width=25, bd=2, bg="sky blue",font=("Times", 10))
        self.root.f1.text.place(x="205",y="150")
        self.root.f1.textc=Listbox(self.root.f1,height=8, width=10, bd=2, bg="sky blue",font=("Times", 10))
        self.root.f1.textc.place(x="10",y="150")
        self.root.f1.textp=Listbox(self.root.f1,height=8, width=10, bd=2, bg="sky blue",font=("Times", 10))
        self.root.f1.textp.place(x="430",y="150")
        self.root.f1.sorce1=Listbox(self.root.f1,height=4, width=10, bd=2, bg="gold",font=("Times", 10))
        self.root.f1.sorce1.place(x="210",y="40")
        self.root.f1.sorce2=Listbox(self.root.f1,height=4, width=10, bd=2, bg="gold",font=("Times", 10))
        self.root.f1.sorce2.place(x="277",y="40")
        self.root.f1.l1=Label(self.root.f1,text="CHOOSE YOUR \n ELEMENT:", bg="gold", fg= "black", font=" roman 20 bold",cursor= "hand2").place(x="10", y="390")


        self.root.f1.b1=Button(self.root.f1,text="ROCK", bg="gold", fg= "black", font="arial, 15 bold", cursor="dot", command=self.isrock )
        self.root.f1.b1.place(x="200",y="400")
        self.root.f1.b2=Button(self.root.f1,text="PAPER", bg="gold", fg= "black", font="arial, 15 bold", cursor="box_spiral", command= self.ispaper)
        self.root.f1.b2.place(x="280",y="400")
        self.root.f1.b3=Button(self.root.f1,text="SCISSOR", bg="gold", fg= "black", font="arial, 15 bold", cursor="X_cursor", command= self.isscissor)
        self.root.f1.b3.place(x="370",y="400")
        
        
  
    computer_value = {
    "0": "Rock",
    "1": "Paper",
    "2": "Scissor"}

    def button_disable(self):
        self.root.f1.b1["state"] = "disable"
        self.root.f1.b2["state"] = "disable"
        self.root.f1.b3["state"] = "disable"


    def reset_game(self):
        self.root.f1.b1["state"] = "active"
        self.root.f1.b2["state"] = "active"
        self.root.f1.b3["state"] = "active"

        self.root.f1.text.delete(0,END)
        self.root.f1.textc.delete(0,END)
        self.root.f1.textp.delete(0,END)
        self.root.f1.sorce2.delete(0,END)
        self.root.f1.sorce1.delete(0,END)
    

# If player selected scissor
    def isrock(self):
        c_v = self.computer_value[str(random.randint(0, 2))]
        if c_v == "Rock":
            self.match_result = "Match Draw"
        elif c_v == "Scissor":
            self.match_result = "Player Win"
        else:
            self.match_result = "Computer Win"

        self.content=self.match_result
        self.root.f1.text.insert(END, self.content)
        self.content=c_v
        self.root.f1.textc.insert(END, self.content)
        self.content="rock"
        self.root.f1.textp.insert(END, self.content)
        self.button_disable()
        


 # If player selected paper
 
 
    def ispaper(self):
       c_v = self.computer_value[str(random.randint(0, 2))]
       if c_v == "Paper":
           self.match_result = "Match Draw"
       elif c_v == "Scissor":
           self.match_result = "Computer Win"
       else:
           self.match_result = "Player Win"
       self.content=self.match_result
       self.root.f1.text.insert(END, self.content)
       self.content=c_v
       self.root.f1.textc.insert(END, self.content)
       self.content="paper"
       self.root.f1.textp.insert(END, self.content)
       self.button_disable()
       
 
# If player selected scissor

    def isscissor(self):
        c_v = self.computer_value[str(random.randint(0, 2))]
        if c_v == "Rock":
            self.match_result = "Computer Win"
        elif c_v == "Scissor":
            self.match_result = "Match Draw"
        else:
            self.match_result = "Player Win"
        self.content=self.match_result
        self.root.f1.text.insert(END, self.content)
        self.content=c_v
        self.root.f1.textc.insert(END, self.content)
        self.content="scissor"
        self.root.f1.textp.insert(END, self.content)
        self.button_disable()
        

    def score(self):
        
            if self.match_result== "Computer Win":
              self.sum=0
              self.sum+=1
              self.summ=0
              self.root.f1.sorce1.insert(END,self.sum)
              self.root.f1.sorce2.insert(END,self.summ)

            elif self.match_result== "Player Win":
              self.summ=0
              self.summ+=1
              self.sum=0
              self.root.f1.sorce2.insert(END,self.summ)
              self.root.f1.sorce1.insert(END,self.sum)
        
            else:
                self.root.f1.sorce1.insert(END,0)
                self.root.f1.sorce2.insert(END,0)

    

        
        
              
            


def main():
    root=Tk()
    ui=Game(root)
    root.mainloop()

if __name__=="__main__":
    main()
