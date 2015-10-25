import controller as cntrl 
import tkinter as tk
class viewClass:
    def __init__(self):
        self.c = cntrl.controller1()
        self.root = tk.Tk()
        self.var = tk.IntVar()

        
        
        self.root.title("THE CLAPPER")

        self.label2 = tk.Label(self.root, text = "Choose your mood:")
        self.label2.grid(row = 0, column = 0,sticky = "n")

        self.button1 = tk.Button(self.root,text = "listen", command = lambda:self.lstnfrmcntrl())
        self.button1.grid(row=3,column=3)
        self.button2 = tk.Button(self.root, text = "Play Recording", command = lambda: self.playrecording())
        self.button2.grid(row=3, column = 2)
     
        self.radio1 = tk.Radiobutton(self.root, text = "Party",value = 1,variable = self.var,activeforeground = "purple",
                                     selectcolor = "purple").grid(row = 2, column = 0)
        
        self.radio2 = tk.Radiobutton(self.root, text = "Romantic", value = 2, variable = self.var, activeforeground = "red",
                                     cursor = "heart",selectcolor = "red").grid(row=2,column=1)

        self.radio3 = tk.Radiobutton(self.root, text = "Relaxing", value = 3, variable = self.var, activeforeground = "white",
                                     selectcolor = "white").grid(row=2, column=2)

        self.radio4 = tk.Radiobutton(self.root, text = "Record" , value = 4, variable = self.var, activeforeground = "green",
                                     selectcolor = "green").grid(row= 2, column = 3)
        
    def mainLoop(self):
        self.root.mainloop()

    def lstnfrmcntrl(self):
        if (self.var.get()== 1) and (self.listentoit() == True):
            print(self.var.get())
            self.root.destroy()
            self.c.playA()
        elif (self.var.get()==2) and (self.listentoit() == True):
            print(self.var.get())
            self.root.destroy()
            self.c.playB()
        elif (self.var.get()==3) and (self.listentoit() == True):
            print(self.var.get())
            self.root.destroy()
            self.c.playC()
        elif (self.var.get() == 4) and (self.listentoit() == True):
            print(self.var.get())
            self.root.destroy()
            self.c.recordit()
                  
    def listentoit(self):
        if self.c.listening():
            return True
        
    def playrecording(self):
        self.root.destroy()
        self.c.playrecord()

