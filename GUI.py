from Tkinter import *
import tkFont
import sqlite3
import tkMessageBox
import os

class Application(Frame):


    def __init__(self,master):

        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        #label1(Main Heading)
        self.customFont = tkFont.Font(size=16)
        self.label1 = Label(self,text = "ENTER DETAILS", font=self.customFont, height=4)
        self.label1.grid(row = 0, column = 6, columnspan =3, sticky = N)

        #label2(Name)
        self.customFont = tkFont.Font(size=12)
        self.label2 = Label(self,text = "NAME", font=self.customFont, height=1)
        self.label2.grid(row=4, column = 0, columnspan =2, sticky = W)

        #TextField1(Name)
        self.Entry1 = Entry(self)
        self.Entry1.grid(row= 4,column=6, columnspan =2, sticky = E)

        fw = open(r'C:\3d-Model\bin\curr_proj.txt','r')
        pathDir = fw.readline()
        fw.close()
        os.chdir(pathDir)
        paths = pathDir.split('\\')
        index=len(paths)-1
        projName ='column'+'.txt'
                        
        fw=open(projName,'r')
        global line
        line = fw.readlines()
        

        
        i=0
        

        
        self.a=line
        #Placing the columns from the column.txt
        while(i<len(line)):
            #label for text from column entries
            self.a[i]= Label(self, text=line[i].upper(), font=self.customFont, height=2)
            self.a[i].grid(row=(26+4*i), column=0, columnspan=2, sticky=W)

            #TextField
            self.a[i] = Entry(self)
            self.a[i].grid(row= (26+4*i),column=6, columnspan =2, sticky = W)
            i+=1
            
            
        
        

        #create button
        self.button1= Button(self, font=self.customFont, height=2)
        self.button1.grid(row = 100, column=2, columnspan= 3, sticky = W)
        self.button1["text"] = "SUBMIT"
        self.button1["command"] = self.DatabaseValue

    def DatabaseValue(self):
            f=open('C:\\3d-Model\\bin\\segmentation_files\\seg_text.txt','r')
            name_file=f.read()
            f.close()
            print name_file
            f=open("C:\\3d-Model\\bin\\segmentation_files\\"+name_file,'a')

            f.write(self.Entry1.get()+"\n")

            for i in range(0,len(line)):
            
                f.writelines(self.a[i].get()+"\n")

            

            tkMessageBox.showinfo("Message", "Value saved successfully")
    
            root.destroy()

        
root=Tk()
root.title("INFORMATION")
root.geometry("600x600")
root.configure()
app = Application(root)
root.mainloop()
