from cryptography.fernet import Fernet
import time
import os
import sys
from tkinter import *
from tkinter import simpledialog
from PIL import Image,ImageTk
import UserPwd
from tkinter import messagebox
import ClosingInProgress
from threading import *

class LayoutDesign(Thread):
    def __init__(self):
        self.win = Tk()
        self.uname=StringVar()
        self.pd=StringVar()
        self.site=StringVar()
        self.val=IntVar()#new line
        self.iter=-1
        self.liter=0
        self.knum=[]
        self.l=0
        self.blr=False
        self.afr=False
        self.edRec=False
        self.delRec=False
        with open('mykey.key', 'rb') as mykey:
            self.key = mykey.read()
            self.fernet = Fernet(self.key)
        #self.key = Fernet.generate_key()
        #self.fernet = Fernet(self.key)
        #self.win.geometry("300x505+1050+250")
        ws = self.win.winfo_screenwidth() # width of the screen
        hs = self.win.winfo_screenheight()# height of the screen
        self.win.geometry('%dx%d+%d+%d' % (300, 516, (ws/2)-200, (hs/2)-250))
        self.win.resizable(False,False)
        self.win.config(bg="#ffecad")
        self.win.wm_iconbitmap("c:\\project\icon\\stock_lock.ico")
        self.win.title("Password Manager")
        self.win.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.up=UserPwd.UserPwd()
        self.db=self.up.retrieveRec()
        self.up.db.clear

    def on_closing(self):
        ans=messagebox.askokcancel("Quit", "Do you want to quit?")
        if ans:
            self.up.storeRec(self.db)
            self.cip = ClosingInProgress.ClosingInProgress()
            self.cip.start()
            #self.cip.join()
            self.cip.root.destroy()
            self.win.destroy()

    def OnOff(self):
        if self.val.get()==0:
            self.pwdEF.config(show='*')
        if self.val.get()==1:
            self.pwdEF.config(show='')

    def setComponents(self):
        self.title=Label(self.win,text="PASSWORD MANAGER",bg="yellow",fg="red",font=("Times New Roman",18))
        self.title.pack(padx=5,pady=5)

        self.lf = LabelFrame(self.win,bg="#98ede7",text="Confidential",padx=10,pady=10)
        self.lf.pack(padx=3,pady=3)
        
        self.first = Frame(self.lf,bg="#98ede7")
        self.first.pack()
        self.unm = Label(self.first,text="User Name",bg="yellow",fg="blue",font=("Times New Roman",14,"bold"))
        self.unm.pack(fill=X)
        self.unmEF = Entry(self.first,text='',width=20,font=("Times New Roman",14,"bold"),fg="#adf542",bg='black',insertbackground='#adf542',textvariable=self.uname)
        self.unmEF.pack(padx=5,pady=5,side=LEFT)
        self.unmEF.focus_set()
        
        self.second = Frame(self.lf,bg="#98ede7")
        self.second.pack()
        self.pwd = Label(self.second,text="Password",bg="yellow",fg="blue",font=("Times New Roman",14,"bold"))
        self.pwd.pack(fill=X)
        self.pwdEF = Entry(self.second,text='',width=20,font=("Times New Roman",14,"bold"),fg="#adf542",bg='black',insertbackground='#adf542',textvariable=self.pd)
        self.pwdEF.pack(padx=5,pady=5,side=LEFT)
        
        self.radioFrame = Frame(self.lf,bg="#98ede7")
        self.radioFrame.pack()
        #self.pwdEF.grid(row=0,column=0)
        self.show = Radiobutton(self.radioFrame,text="show password",bg="yellow",fg="blue",font=("Times New Roman",10,"bold"),variable=self.val,value=1,command=self.OnOff)        #self.show.pack(padx=5,pady=5)
        self.show.grid(row=0,column=0,pady=5)
        self.hide = Radiobutton(self.radioFrame,text="hide password",bg="yellow",fg="blue",font=("Times New Roman",10,"bold"),variable=self.val,value=0,command=self.OnOff)
        #self.hide.pack(padx=5,pady=5)
        self.hide.grid(row=0,column=1,pady=5)
        self.show.select()

        self.third = Frame(self.lf,bg="#98ede7")
        self.third.pack()
        self.sitename = Label(self.third,text="Site Name",bg="yellow",fg="blue",font=("Times New Roman",14,"bold"))
        self.sitename.pack(fill=X)
        self.sitenameEF = Entry(self.third,text='',width=20,font=("Times New Roman",14,"bold"),fg="#adf542",bg='black',insertbackground='#adf542',textvariable=self.site)
        self.sitenameEF.pack(padx=5,pady=5,side=LEFT)

        #Bottom Left Panel Design
        self.lpanel=LabelFrame(self.win,text="DataContorls",bg="#2ee69f",padx=5,pady=5)
        self.lpanel.place(x=24,y=313)#new
        self.add=Button(self.lpanel,text="ADD",bg="#d0e62e",fg="#e31269",bd=5,font=("Dutch801 Rm BT",8,'bold'),command=self.addRec,width=5)
        #self.add.pack(padx=3,pady=3)
        self.add.grid(row=0,column=0,padx=3,pady=3)
        self.update=Button(self.lpanel,text="UPDATE",bg="#d0e62e",fg="#e31269",bd=5,font=("Dutch801 Rm BT",8,'bold'),state= DISABLED,command=self.saveRec,width=6)
        #self.update.pack(padx=3,pady=3)
        self.update.grid(row=0,column=1,padx=3,pady=3)
        self.edit=Button(self.lpanel,text="EDIT",bg="#d0e62e",fg="#e31269",bd=5,font=("Dutch801 Rm BT",8,'bold'),width=5,command=self.editRecord)
        #self.edit.pack(padx=3,pady=3)
        self.edit.grid(row=1,column=0,padx=3,pady=3)
        self.exit=Button(self.lpanel,text="EXIT",bg="#d0e62e",fg="#e31269",bd=5,font=("Dutch801 Rm BT",8,'bold'),width=5,command=self.on_closing)
        #self.exit.pack(padx=3,pady=3)
        self.exit.grid(row=1,column=1,padx=3,pady=3)

        #Bottom Right Panel Design
        self.rpanel=LabelFrame(self.win,text="NavigationContorls",bg="#2ee69f",padx=5,pady=5)
        self.rpanel.place(x=156,y=313)#new
        self.next=Button(self.rpanel,text="NEXT",bg="#d0e62e",fg="#e31269",bd=5,font=("Dutch801 Rm BT",8,'bold'),command=self.nextRec,width=5)
        #self.next.pack(padx=3,pady=3)
        self.next.grid(row=0,column=0,padx=3,pady=3)
        self.last=Button(self.rpanel,text="LAST",bg="#d0e62e",fg="#e31269",bd=5,font=("Dutch801 Rm BT",8,'bold'),command=self.lastRec,width=5)
        #self.last.pack(padx=3,pady=3)
        self.last.grid(row=0,column=1,padx=3,pady=3)
        self.pre=Button(self.rpanel,text="PRE",bg="#d0e62e",fg="#e31269",bd=5,font=("Dutch801 Rm BT",8,'bold'),command=self.preRec,width=5)
        #self.pre.pack(padx=3,pady=3)
        self.pre.grid(row=1,column=0,padx=3,pady=3)
        self.first=Button(self.rpanel,text="FIRST",bg="#d0e62e",fg="#e31269",bd=5,font=("Dutch801 Rm BT",8,'bold'),command=self.firstRec,width=5)
        #self.first.pack(padx=3,pady=3)
        self.first.grid(row=1,column=1,padx=3,pady=3)

        self.bottomPanel = LabelFrame(self.win,text="",bg="#342abf",fg="#abf243",padx=5,pady=5)
        self.bottomPanel.place(x=12,y=420)
        #button width=22
        self.delete=Button(self.bottomPanel,text="DELETE RECORDS",bg="#f7ae02",fg="#e80765",font=("Times New Roman",8),command=self.deleteRecord)
        self.delete.grid(row=0,column=0,padx=3)#x=32,y=395)
        self.cancel=Button(self.bottomPanel,text="CANCEL",bg="#0acff2",fg="#ed074c",font=("Times New Roman",8),command=self.cancelTask)
        self.cancel.grid(row=0,column=1,padx=3)#x=32,y=433)
        self.cancel.config(state=DISABLED)
        self.find=Button(self.bottomPanel,text="FIND RECORDS",bg="#00e81b",fg="#050505",font=("Times New Roman",8),command=self.findRecord)
        self.find.grid(row=0,column=2,padx=3)#(x=32,y=470)
        self.by = Label(self.win,text="Developed By VAKKAS\nvakkas77@gmail.com\nMob:9894040431",bg="yellow",fg="blue",font=("Times New Roman",8,"bold"))
        self.by.place(x=85,y=465)

        #Load File During Startup
        self.l=len(list(self.db.keys()))

        if self.l!=0:
            #messagebox.showerror("error",self.db.keys())
            for k in self.db.keys():
                self.knum.append(k)
            self.nextRec()

    def addRec(self):
        tempiter=self.iter
        self.update.config(state=NORMAL)
        self.unmEF.delete(0,END)
        self.pwdEF.delete(0,END)
        self.sitenameEF.delete(0,END)
        self.add.config(state=DISABLED)
        self.edit.config(state=DISABLED)
        self.next.config(state=DISABLED)
        self.pre.config(state=DISABLED)
        self.first.config(state=DISABLED)
        self.last.config(state=DISABLED)
        self.cancel.config(state=NORMAL)
        self.delete.config(state=DISABLED)
        self.find.config(state=DISABLED)
        self.unmEF.focus_set()

    def cancelTask(self):
        self.edit.config(state=NORMAL)
        self.next.config(state=NORMAL)
        self.pre.config(state=NORMAL)
        self.first.config(state=NORMAL)
        self.last.config(state=NORMAL)
        self.add.config(state=NORMAL)
        self.cancel.config(state=DISABLED)
        self.update.config(state=DISABLED)
        self.delete.config(state=NORMAL)
        self.find.config(state=NORMAL)
        self.unmEF.config(state=NORMAL)
        self.exit.config(state=NORMAL)
        self.iter-=1
        self.nextRec()
        self.edRec=False
        self.unmEF.focus_set()

    def findRecord(self):
        lusername=simpledialog.askstring("Question","Enter User Name:",parent=self.win)
        tempiter=self.iter
        self.iter=0
        if lusername==None:
            return
        if lusername.strip()=="":
            messagebox.showinfo("Information","You Have Left The Field Blank")
            self.edRec=True
        else:
            for i in self.db.keys():
                if lusername.strip()==str(i).strip():
                    self.uname.set(self.knum[self.iter])
                    v=self.db[self.knum[self.iter]]
                    #self.pd.set(v[self.liter])
                    self.decmsg=self.fernet.decrypt(v[self.liter]).decode() # Added Recenlty
                    self.pd.set(self.decmsg)
                    self.liter+=1
                    self.site.set(v[self.liter])
                    self.liter=0
                    self.edRec=True
                    break 
                else:
                    self.iter+=1
        if not self.edRec:
            messagebox.showinfo("Information","No Such Record Found")
            self.iter=tempiter
            #self.nextRec()
        self.edRec=False

    def editRecord(self):
        if self.l!=0:
            lusername=simpledialog.askstring("Question","Enter User Name:",parent=self.win)
            tempiter=self.iter
            if lusername==None:
                return
            self.iter=0 	
            if lusername.strip()=="":
                messagebox.showinfo("Information","You Have Left The Field Blank")
                return
                #self.edRec=True
            else:
                for i in self.db.keys():
                    if lusername.strip()==str(i).strip():
                        self.uname.set(self.knum[self.iter])
                        v=self.db[self.knum[self.iter]]
                        #self.pd.set(v[self.liter])
                        self.decmsg=self.fernet.decrypt(v[self.liter]).decode() # Added Recenlty
                        self.pd.set(self.decmsg)
                        self.liter+=1
                        self.site.set(v[self.liter])
                        self.liter=0
                        self.add.config(state=DISABLED)
                        self.update.config(state=NORMAL)
                        self.unmEF.config(state=DISABLED)
                        self.edit.config(state=DISABLED)
                        self.exit.config(state=DISABLED)
                        self.next.config(state=DISABLED)
                        self.pre.config(state=DISABLED)
                        self.first.config(state=DISABLED)
                        self.last.config(state=DISABLED)
                        self.delete.config(state=DISABLED)
                        self.find.config(state=DISABLED)
                        self.cancel.config(state=NORMAL)
                        self.edRec=True
                        break 
                    else:
                        self.iter+=1
        else:
            messagebox.showinfo("Information","No Records In The File")
            self.edRec=True
            #self.iter=tempiter
        if not self.edRec:
            messagebox.showinfo("Information","No Such Record Found")
            self.iter=tempiter
            self.edRec=False
        

    def deleteRecord(self):
        if self.l!=0:
            #else:     
            ans=messagebox.askokcancel("Quit", "Do you want to DELETE?")
            if ans:
                del self.db[self.knum[self.iter]]
                self.knum.remove(self.knum[self.iter])
                self.l-=1
                self.iter=-1
                #self.unmEF.focus_set()
                self.nextRec()
            else:
                messagebox.showinfo("Infomration","Record Not Deleted")
                self.unmEF.focus_set()
                self.delRec=False
        else:
            if(self.unmEF.get().strip()=='' or str(self.pwdEF.get()).strip()=='' or str(self.sitenameEF.get()).strip()==''):
                messagebox.showinfo("Information","No Records To Delete, Your File is Empty")
                self.unmEF.focus_set()
        
    def saveRec(self):
        if self.edRec:
            #print(self.knum[self.iter])
            n=self.knum[self.iter]
            v=self.db.get(n)
            p=v[self.liter]
            self.liter+=1
            s=v[self.liter]
            self.liter=0
            self.add.config(state=NORMAL)
            self.update.config(state=DISABLED)
            self.unmEF.config(state=NORMAL)
            self.edRec=False
            self.db[self.uname.get()]=[self.fernet.encrypt(self.pd.get().encode()),self.site.get()]  
            messagebox.showinfo("Message","Record Successfully Modified")
            self.next.config(state=NORMAL)
            self.cancel.config(state=DISABLED)
            self.pre.config(state=NORMAL)
            self.first.config(state=NORMAL)
            self.last.config(state=NORMAL)
            self.edit.config(state=NORMAL)
            self.exit.config(state=NORMAL)
            self.delete.config(state=NORMAL)
            self.find.config(state=NORMAL)
            self.iter=-1
            self.nextRec()
        else:
            self.flag=True
            if(self.unmEF.get().strip()=='' or str(self.pwdEF.get()).strip()=='' or str(self.sitenameEF.get()).strip()==''):
                messagebox.showwarning("Warning","Dont Leave Blank")
                self.flag=False
            else:
                for keys in self.db:
                    if keys==self.uname.get():
                        messagebox.showwarning("Warning","Entered Duplicate Value")
                        self.flag=False
                        break
            if self.flag:
                #self.fernet.encrypt(message.encode())
                self.db.update({self.uname.get():[self.fernet.encrypt(self.pd.get().encode()),self.site.get()]})
                messagebox.showwarning("Info","Record Saved")
                #self.up.setRec(self.uname.get(),self.pd.get(),self.site.get())
                self.add.config(state=NORMAL)
                self.update.config(state=DISABLED)
                self.edit.config(state=NORMAL)
                self.next.config(state=NORMAL)
                self.pre.config(state=NORMAL)
                self.first.config(state=NORMAL)
                self.last.config(state=NORMAL)
                self.cancel.config(state=DISABLED)
                self.delete.config(state=NORMAL)
                self.find.config(state=NORMAL)
                self.l+=1
                #self.iter+=1#new line
                self.knum.append(self.uname.get())
                self.iter=-1
                self.nextRec()

    def nextRec(self):
        #messagebox.showerror("error",self.knum)
        self.unmEF.focus_set()
        if self.l!=0:
            if self.l==self.iter+1:
                messagebox.showinfo("Warning","Reached Last Records")
                self.blr=True
                #self.iter-=1
            else:
                self.iter+=1
                self.uname.set(self.knum[self.iter])
                v=self.db[self.knum[self.iter]]
                #print(v[self.liter])
                self.decmsg=self.fernet.decrypt(v[self.liter]).decode() 
                self.pd.set(self.decmsg)
                self.liter+=1
                self.site.set(v[self.liter])
                self.liter=0
                self.blr=True
        else:
            messagebox.showwarning("Warning","No Records In File")
            self.uname.set("")
            self.pd.set("")
            self.site.set("")
            #self.iter-=1    

    def lastRec(self):
        if self.iter==self.l-1:
            messagebox.showinfo("Information","This is The Last Record")
        else:
            self.iter=self.l-1
            self.uname.set(self.knum[self.iter])
            v=self.db[self.knum[self.iter]]
            #self.pd.set(v[self.liter])
            self.decmsg=self.fernet.decrypt(v[self.liter]).decode() # Added Recently
            self.pd.set(self.decmsg)
            self.liter+=1
            self.site.set(v[self.liter])
            #self.iter-=1
            self.liter=0

    def preRec(self):
        if self.l!=0 and self.iter!=0:
            if self.l==1:
                messagebox.showinfo("Warning","Totally One Record in this File")
            else:
                if self.blr:
                    self.iter-=1
                    self.blr=False
                    self.uname.set(self.knum[self.iter])
                    v=self.db[self.knum[self.iter]]
                    #self.pd.set(v[self.liter])
                    self.decmsg=self.fernet.decrypt(v[self.liter]).decode() # Added Recenlty
                    self.pd.set(self.decmsg)
                    self.liter+=1
                    self.site.set(v[self.liter])
                    #self.iter-=1
                    self.liter=0
                else:
                    self.iter-=1
                    self.blr=False
                    self.uname.set(self.knum[self.iter])
                    v=self.db[self.knum[self.iter]]
                    #self.pd.set(v[self.liter])
                    self.decmsg=self.fernet.decrypt(v[self.liter]).decode() # Added Recenlty
                    self.pd.set(self.decmsg)
                    self.liter+=1
                    self.site.set(v[self.liter])
                    #self.iter-=1
                    self.liter=0
        else:
            messagebox.showwarning("Warning","First Record Reached")
            #self.iter-=1

    def firstRec(self):
            if self.iter==0:
                messagebox.showinfo("Information","This is The First Record")
            else:
                self.iter=0
                self.uname.set(self.knum[self.iter])
                v=self.db[self.knum[self.iter]]
                #self.pd.set(v[self.liter])
                self.decmsg=self.fernet.decrypt(v[self.liter]).decode() # Added Recenlty
                self.pd.set(self.decmsg)
                self.liter+=1
                self.site.set(v[self.liter])
                #self.iter-=1
                self.liter=0

if __name__ == "__main__":
    chk = Tk()
    ws = chk.winfo_screenwidth() # width of the screen
    hs = chk.winfo_screenheight()# height of the screen
    chk.geometry('%dx%d+%d+%d' % (350, 170, (ws/2)-250, (hs/2)-130))
    #chk.geometry("350x170+700+500")
    chk.title("Validation Window")
    chk.wm_iconbitmap("c:\\project\icon\\stock_lock.ico")
    chk.config(bg="#EDE850")
    Label(chk,text="User Authentication",width=350,bg="black",fg="yellow",font=("Dutch801 Rm BT",14,"bold")).pack()
    lframe= LabelFrame(chk,text='Checking Credentials',bg="#50EBED",fg='red',font=("Dutch801 Rm BT",14,"bold"),padx=4,pady=4)
    lframe.pack(pady=8)
    userlbl = Label(lframe,text="User Name",width=10,bg="black",fg="yellow",font=("Dutch801 Rm BT",12,"bold"))
    userlbl.grid(row=0,column=0)
    userTF = Entry(lframe,width=20,font=("Dutch801 Rm BT",14,"bold"),bg='#3DED96',fg='#3804F2')
    userTF.grid(row=0,column=1)
    pwdlbl = Label(lframe,text="PassWord",width=10,bg="black",fg="yellow",font=("Dutch801 Rm BT",12,"bold"))
    pwdlbl.grid(row=1,column=0)
    pwdTF = Entry(lframe,width=20,show="*",font=("Dutch801 Rm BT",14,"bold"),bg='#3DED96',fg='#3804F2')
    pwdTF.grid(row=1,column=1)

    def validateUP():
        flg=False
        os.chdir("C:\\project\\")
        f=open("validate.dat")
        with open("validate.dat",'r') as f:
            str=f.read()
            str=str.split('\n')
        for element in str:
            element=element.split(";")
            #print(element[0],element[1])
            if element[0]==userTF.get().strip() and element[1]==pwdTF.get().strip():
                chk.destroy()
                lk = LayoutDesign()
                lk.setComponents()
                lk.win.mainloop()
                flg=True
                break
        if not flg:
            messagebox.showerror("ERROR","Incorrect User Name or Password")
    
    def clearFields():
        userTF.delete(0,END)
        pwdTF.delete(0,END)
        userTF.focus_set()

    def exitApp():
        chk.destroy()

    f=Frame(chk,bg="#EDE850")
    f.pack(pady=0)
    vldt=Button(f,text="VALIDATE",font=("Dutch801 Rm BT",12,"bold"),bg='#F3139E',fg='#13F3DA',command=validateUP)
    vldt.grid(row=0,column=0,padx=5,pady=2)
    clr=Button(f,text="CLEAR",font=("Dutch801 Rm BT",12,"bold"),bg='#F3139E',fg='#13F3DA',command=clearFields)
    clr.grid(row=0,column=1,padx=5,pady=0)
    ext=Button(f,text="EXIT",font=("Dutch801 Rm BT",12,"bold"),bg='#F3139E',fg='#13F3DA',command=exitApp)
    ext.grid(row=0,column=2,padx=5,pady=0)
    userTF.focus_set()
    chk.mainloop()
    #lk = LayoutDesign()
    #lk.setComponents()
    #lk.win.mainloop()
#ws = root.winfo_screenwidth() # width of the screen
#hs = root.winfo_screenheight() # height of the screen
#root.geometry('%dx%d+%d+%d' % (w, h, x, y))
