'''Create a GUI application with calculator functionality. The application should include buttons for digits, as well as for the four basic 
arithmetic operations (addition, subtraction, multiplication, and division). Additionally, the application should maintain a history log for
each use of the calculator, and this information should be stored in a storage (type of the storage can be either text file, OR database). 
It should also be possible to retrieve the result of the last operation stored in the storage by clicking on a specific button.'''

import wx
import sqlite3

firstnum = None
oper = None
result = None

def bnclick(evt):
    p = evt.GetEventObject().Label
    q = t.GetValue()
    r = q + p
    t.SetValue(r)


def opclick(evt):
    global firstnum
    global oper
    firstnum = float(t.GetValue())
    oper = evt.GetEventObject().Label
    t.SetValue("")

def equclick(evt):
    global firstnum
    global oper
    global result
    secondnum = float(t.GetValue())
    if oper == '+':
        result = firstnum + secondnum
    elif oper == '-':
        result = firstnum - secondnum
    elif oper == 'x':
        result = firstnum * secondnum
    elif oper == '/':
        if secondnum == 0:
            result = "error"
        else:
            result = firstnum / secondnum
    else:
        result = ''
    t.SetValue(str(result))
        
def resclick(evt):
    '''global firstnum
    global oper
    firstnum = float(t.GetValue())
    oper = evt.GetEventObject().Label'''
    t.SetValue("")

def storevalue(evt):
    con = sqlite3.connect("CalculatorValues.db")
    cur = con.cursor()

    # Create the table if it doesn't exist
    cur.execute("CREATE TABLE IF NOT EXISTS CalculatorValues (id INTEGER PRIMARY KEY AUTOINCREMENT, value REAL)")

    # Insert the calculated value into the table
    cur.execute("INSERT INTO CalculatorValues (value) VALUES (?)", (result,))
    
    con.commit()
    cur.close()
    con.close()

def retrievevalue(evt):
    con = sqlite3.connect("CalculatorValues.db")
    cur = con.cursor()

    # Retrieve the last stored value
    cur.execute("SELECT value FROM CalculatorValues ORDER BY id DESC LIMIT 1")
    row = cur.fetchone()

    if row:
        last_result = row[0]
        t.SetValue(str(last_result))

    cur.close()
    con.close()



theApp = wx.App()
f = wx.Frame(parent=None, title="Calculater")
t = wx.TextCtrl(parent=f, size=(120,25))
t.SetPosition(wx.Point(10,10))

b7 = wx.Button(parent = f, label = "7", size=(25,25))
b7.SetPosition(wx.Point(10,70))
b7.Bind(wx.EVT_BUTTON, bnclick)

b8 = wx.Button(parent = f, label = "8", size=(25,25))
b8.SetPosition(wx.Point(40,70))
b8.Bind(wx.EVT_BUTTON, bnclick)

b9 = wx.Button(parent = f, label = "9", size=(25,25))
b9.SetPosition(wx.Point(70,70))
b9.Bind(wx.EVT_BUTTON, bnclick)

b4 = wx.Button(parent = f, label = "4", size=(25,25))
b4.SetPosition(wx.Point(10,100))
b4.Bind(wx.EVT_BUTTON, bnclick)

b5 = wx.Button(parent = f, label = "5", size=(25,25))
b5.SetPosition(wx.Point(40,100))
b5.Bind(wx.EVT_BUTTON, bnclick)

b6 = wx.Button(parent = f, label = "6", size=(25,25))
b6.SetPosition(wx.Point(70,100))
b6.Bind(wx.EVT_BUTTON, bnclick)

b1 = wx.Button(parent = f, label = "1", size=(25,25))
b1.SetPosition(wx.Point(10,130))
b1.Bind(wx.EVT_BUTTON, bnclick)

b2 = wx.Button(parent = f, label = "2", size=(25,25))
b2.SetPosition(wx.Point(40,130))
b2.Bind(wx.EVT_BUTTON, bnclick)

b3 = wx.Button(parent = f, label = "3", size=(25,25))
b3.SetPosition(wx.Point(70,130))
b3.Bind(wx.EVT_BUTTON, bnclick)

b0 = wx.Button(parent = f, label = "0", size=(55,25))
b0.SetPosition(wx.Point(10,160))
b0.Bind(wx.EVT_BUTTON, bnclick)



bplus = wx.Button(parent = f, label = "+", size=(25,25))
bplus.SetPosition(wx.Point(100,130))
bplus.Bind(wx.EVT_BUTTON, opclick)

bminus = wx.Button(parent = f, label = "-", size=(25,25))
bminus.SetPosition(wx.Point(100,100))
bminus.Bind(wx.EVT_BUTTON, opclick)

bmultiply = wx.Button(parent = f, label = "x", size=(25,25))
bmultiply.SetPosition(wx.Point(100,70))
bmultiply.Bind(wx.EVT_BUTTON, opclick)

bdivide = wx.Button(parent = f, label = "/", size=(25,25))
bdivide.SetPosition(wx.Point(100,40))
bdivide.Bind(wx.EVT_BUTTON, opclick)

bequals = wx.Button(parent = f, label = "=", size=(25,25))
bequals.SetPosition(wx.Point(100,160))
bequals.Bind(wx.EVT_BUTTON, equclick)

bequals = wx.Button(parent = f, label = "C", size=(25,25))
bequals.SetPosition(wx.Point(10,40))
bequals.Bind(wx.EVT_BUTTON, resclick)

bdecimal = wx.Button(parent = f, label = ".", size=(25,25))
bdecimal.SetPosition(wx.Point(70,160))
bdecimal.Bind(wx.EVT_BUTTON, bnclick)

mstorage = wx.Button(parent = f, label = "SV", size=(25,25))
mstorage.SetPosition(wx.Point(40,40))
mstorage.Bind(wx.EVT_BUTTON, storevalue) 

mstorage = wx.Button(parent = f, label = "RV", size=(25,25))
mstorage.SetPosition(wx.Point(70,40))
mstorage.Bind(wx.EVT_BUTTON, retrievevalue)


f.Show()
theApp.MainLoop()

