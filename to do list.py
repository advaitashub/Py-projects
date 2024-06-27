#TASK 1: CREATING A TO-DO LIST GUI

from tkinter import *

#pop up box structure
class todo:
    def __init__(self, root):
       self.root = root
       self.root.title('To-Do-List')
       self.root.geometry('650x410+300+150')

       #Label as a heading 
       self.label = Label(self.root,text='To-Do-List-App', 
                          font= 'ariel, 25 bold', width = 10, bd=5,bg="red", fg='black')
       self.label.pack(side='top',fill=BOTH)

        #label for add tast
       self.label2 = Label(self.root,text='ADD TASK', 
                          font= 'ariel, 18 bold', width = 10, bd=5,bg="blue", fg='white')
       self.label2.place(x=40, y=54)

         #label for task
       self.label3 = Label(self.root,text='TASK', 
                          font= 'ariel, 18 bold', width = 10, bd=5,bg="blue", fg='white')
       self.label3.place(x=320, y=54)

       self.main_text =Listbox(self.root, height=9,bd =5, width =23,bg="sky blue",font= "aerial, 20 bold")
       self.main_text.place(x=280, y=100)

       self.text = Text(self.root, bd=5, height=4,bg="light green", width=30, font = 'ariel, 10 bold')
       self.text.place(x=20, y=120)

#=====================ADD TAST=================#
       def add():
           content = self.text.get(1.0, END)
           self.main_text.insert(END, content)
           with open(r"C:\Users\singh\OneDrive\Documents\data.txt",'a') as file:
               file.write(content)
               file.seek(0)
               file.close()
           self.text.delete(1.0,END)
        
        #creating delete function
       def delete():
           delete_=self.main_text.curselection()
           look = self.main_text.get(delete_) 
           with open(r'C:\Users\singh\OneDrive\Documents\data.txt','r+') as f:
               new_f = f.readlines()
               f.seek(0)
               for line in new_f:
                   item = str(look)
                   if item not in line:
                       f.write(line)
               f.truncate() 
           self.main_text.delete(delete_)

       with open(r'C:\Users\singh\OneDrive\Documents\data.txt','r') as file:
           read = file.readlines()
           for i in read:
               ready= i.split()
               self.main_text.insert(END, ready)
           file.close()
    

    
       #buttons
       self.button= Button(self.root, text="Add", font='sarif, 20 bold italic',
                                    width=10, bd = 5, bg= 'orange', fg= 'black',command= add)
       self.button.place(x=30, y=180)

       self.button2= Button(self.root, text="Delete", font='sarif, 20 bold italic',
                                    width=10, bd = 5, bg= 'orange', fg= 'black',command= delete)
       self.button2.place(x=30, y=280)   


       
def main():
 root = Tk()
 ui = todo(root)
 root.mainloop()

if __name__== "__main__":
    main()
 