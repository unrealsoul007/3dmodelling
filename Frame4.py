#Boa:Frame:Frame4

import wx
import sqlite3
import os

def create(parent):
    return Frame4(parent)

[wxID_FRAME4, wxID_FRAME4LISTBOX1, wxID_FRAME4PANEL1, wxID_FRAME4STATICTEXT1, 
 wxID_FRAME4STATICTEXT2, wxID_FRAME4TEXTCTRL1, wxID_FRAME4TOGGLEBUTTON1, 
 wxID_FRAME4TOGGLEBUTTON2, wxID_FRAME4TOGGLEBUTTON3, 
] = [wx.NewId() for _init_ctrls in range(9)]

class Frame4(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME4, name='', parent=prnt,
              pos=wx.Point(318, 88), size=wx.Size(790, 587),
              style=wx.DEFAULT_FRAME_STYLE, title='Frame4')
        self.SetClientSize(wx.Size(774, 549))
        self.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.panel1 = wx.Panel(id=wxID_FRAME4PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(774, 549),
              style=wx.TAB_TRAVERSAL)

        self.staticText1 = wx.StaticText(id=wxID_FRAME4STATICTEXT1,
              label=u'ENTER COLUMN NAME', name='staticText1',
              parent=self.panel1, pos=wx.Point(264, 48), size=wx.Size(272, 33),
              style=0)
        self.staticText1.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))

        self.staticText2 = wx.StaticText(id=wxID_FRAME4STATICTEXT2,
              label=u'Name:', name='staticText2', parent=self.panel1,
              pos=wx.Point(64, 144), size=wx.Size(56, 23), style=0)
        self.staticText2.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME4TEXTCTRL1, name='textCtrl1',
              parent=self.panel1, pos=wx.Point(200, 144), size=wx.Size(120, 24),
              style=0, value='')

        self.toggleButton1 = wx.ToggleButton(id=wxID_FRAME4TOGGLEBUTTON1,
              label=u'ADD', name='toggleButton1', parent=self.panel1,
              pos=wx.Point(72, 216), size=wx.Size(88, 40), style=0)
        self.toggleButton1.SetValue(False)
        self.toggleButton1.Bind(wx.EVT_TOGGLEBUTTON,
              self.OnToggleButton1Togglebutton, id=wxID_FRAME4TOGGLEBUTTON1)

        self.toggleButton2 = wx.ToggleButton(id=wxID_FRAME4TOGGLEBUTTON2,
              label=u'REMOVE', name='toggleButton2', parent=self.panel1,
              pos=wx.Point(72, 280), size=wx.Size(88, 40), style=0)
        self.toggleButton2.SetValue(False)
        self.toggleButton2.Bind(wx.EVT_TOGGLEBUTTON,
              self.OnToggleButton2Togglebutton, id=wxID_FRAME4TOGGLEBUTTON2)

        self.listBox1 = wx.ListBox(choices=[], id=wxID_FRAME4LISTBOX1,
              name='listBox1', parent=self.panel1, pos=wx.Point(200, 216),
              size=wx.Size(112, 104), style=0)
        self.listBox1.Bind(wx.EVT_LISTBOX, self.OnListBox1Listbox,
              id=wxID_FRAME4LISTBOX1)

        self.toggleButton3 = wx.ToggleButton(id=wxID_FRAME4TOGGLEBUTTON3,
              label=u'SUBMIT', name='toggleButton3', parent=self.panel1,
              pos=wx.Point(360, 376), size=wx.Size(88, 40), style=0)
        self.toggleButton3.SetValue(True)
        self.toggleButton3.Bind(wx.EVT_TOGGLEBUTTON,
              self.OnToggleButton3Togglebutton, id=wxID_FRAME4TOGGLEBUTTON3)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnToggleButton1Togglebutton(self, event):
        s1=self.textCtrl1.GetValue()
        s2=''

        #f = open('First.txt','w')
        #f.close()
        if s1==s2:
            wx.MessageBox('Please Enter Value')
        else:
            
            self.listBox1.Append(self.textCtrl1.GetValue())
            self.textCtrl1.SetValue('')
                
                

    def OnToggleButton2Togglebutton(self, event):
        if self.listBox1.GetCount()==0:
            wx.MessageBox('No Values to Remove')
        else:    
            self.listBox1.Delete(self.listBox1.GetSelection())

    def OnToggleButton3Togglebutton(self, event):
        
        if self.listBox1.GetCount()==0:
            wx.MessageBox('Please Enter Values')
        
        else:
            try:
                j=0
                k=0
                flag=0
                for j in range(0,self.listBox1.GetCount()):
                    for k in range(j+1,self.listBox1.GetCount()):
                        if self.listBox1.GetString(j)==self.listBox1.GetString(k):
                            wx.MessageBox('Same column names. Please enter again')
                            flag=1
                            
                for j in range(0,self.listBox1.GetCount()):
                    if self.listBox1.GetString(j).lower()=='name':
                        wx.MessageBox('Do not enter name as an attribute(Column Name)')
                        flag=1
                    if self.listBox1.GetString(j).lower()=='latitude':
                        wx.MessageBox('Do not enter latitude as an attribute(Column Name)')
                        flag=1

                    if self.listBox1.GetString(j).lower()=='longitude':
                        wx.MessageBox('Do not enter longitude as an attribute(Column Name)')
                        flag=1

                    if self.listBox1.GetString(j).lower()=='altitude':
                        wx.MessageBox('Do not enter altitude as an attribute(Column Name)')
                        flag=1
                            
                if flag==0:           
                    for i in range(self.listBox1.GetCount()):
                        self.listBox1.GetString(i)
                        fw = open(r'C:\3d-Model\bin\curr_proj.txt','r')
                        pathDir = fw.readline()
                        print pathDir
                        fw.close()
                        os.chdir(pathDir)
                        paths = pathDir.split('\\')
                        index=len(paths)-1
                        projName ='column'+'.txt'
                        
                        fw=open(projName,'a')
                        fw.writelines(self.listBox1.GetString(i)+"\n")
                        f = open(r'C:\3d-Model\bin\curr_proj.txt','r')
                        pathDir = f.readline()
                        f.close()
                        os.chdir(pathDir)
                        paths = pathDir.split('\\')
                        index=len(paths)-1
                        projName = paths[index] + '.db'
                        conn= sqlite3.connect(projName)
 
                        cursor = conn.cursor()

                        cursor.execute('''ALTER TABLE information ADD COLUMN '''+self.listBox1.GetString(i))
                        conn.commit()
                        conn.close()
                    wx.MessageBox('Values Entered Successfully. Your Database has been created')
                    self.Destroy()
            except:
                wx.MessageBox('Same column names Or Connection to Database Server lost. Try again')
                #f.close()
                #os.remove('column.txt')
                        
                
                    
                            

    def OnListBox1Listbox(self, event):
        event.Skip()
