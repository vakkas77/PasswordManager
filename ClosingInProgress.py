from tkinter import *
from tkinter.ttk import Progressbar
import time

class ClosingInProgress():
    def __init__(self):
        #Thread.__init__(self)
        self.curval=0
        self.root = Tk()
        self.root.title('Work In Progress')
        #self.root.geometry('600x100+500+300')
        ws = self.root.winfo_screenwidth() # width of the screen
        hs = self.root.winfo_screenheight()# height of the screen
        self.root.geometry('%dx%d+%d+%d' % (600, 100, (ws/2)-350, (hs/2)-75))
        self.pb = Progressbar(self.root, orient=HORIZONTAL,length=600, mode='determinate')
        self.pb.pack(expand=True)
        self.label = Label(self.root,width=600,text="Wait!!! Your File Is Being Saved\n0%",bg="black",fg="yellow",font=("digital-7",12,"bold"))
        self.label.pack(expand=True)
        self.pb['value']=self.curval
        self.pb['maximum']=100
        #self.pb.after(0,self.start())
        #self.root.destroy()
        #progressbar=ttk.Progressbar(master,orient="horizontal",length=300,mode="determinate")
        #progressbar.pack(side=tk.TOP)
        #currentValue=0
        #progressbar["value"]=currentValue
        #progressbar["maximum"]=maxValue
        #for i in range(10):
        #currentValue=currentValue+10
        #progressbar.after(500, progress(currentValue))
        #progressbar.update() # Force an update of the GUI
    def start(self):
        for i in range(21):
            #self.root.update_idletasks()
            self.curval+=5       
            self.pb['value'] = self.curval
            self.pb.update()
            self.label.config(text="Wait!!! Your File Is Being Saved\n"+str(self.curval)+"%")
            time.sleep(.2)
        #Desired_font = tkinter.font.Font( family = "Comic Sans MS", size = 20, weight = "bold") 
        #label.configure(font = Desired_font)