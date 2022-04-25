import pickle
import os
from tkinter import messagebox
class UserPwd:
    #db = {}
    #self.tp=()
    def __init__(self):
        os.chdir("c:\\project\\")
        self.user=''
        self.pwd=''
        self.site=''
        self.dbfile = open('unpw.dat', 'rb')
        self.db={}
        if os.stat('unpw.dat').st_size != 0:        
            self.db = pickle.load(self.dbfile)
        self.dbfile.close()

    def setRec(self,u,p,s):
        self.flag=True
        self.user=u
        self.pwd=p
        self.site=s
        for keys in self.db:
            if keys==self.user:
                messagebox.showwarning("Warning","Entered Duplicate Value")
                flag=False
                break
        if self.flag:
            self.db.update({self.user:[self.pwd,self.site]})
            messagebox.showwarning("Info","Record Saved")

    def retrieveRec(self):
        return self.db

    def storeRec(self,d):
        #self.user=u
        #self.pwd=p
        #self.site=s
        #self.db.update({u:[p,s]}) 
        #self.dbfile = open('unpw.dat', 'ab')
        self.db=d
        #print(self.user,self.pwd,self.site)
        self.dbfile = open('unpw.dat', 'wb')
        pickle.dump(self.db, self.dbfile)                     
        self.dbfile.close()
        

'''
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
'''