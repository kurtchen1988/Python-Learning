import wx

def load(event):
    file = open(filename.GetValue(),"r")
    contents.SetValue(file.read())
    file.close()


def save(event):
    file = open(filename.GetValue(),"w")
    file.write(contents.GetValue())
    file.close()

app=wx.App()
win=wx.Frame(None, title="我的记事本",size=(410,335))
loadButton=wx.Button(win, label="Open", pos=(225,5), size=(80,25))
saveButton=wx.Button(win, label="Save", pos=(315,5), size=(80,25))

loadButton.Bind(wx.EVT_BUTTON,load)
saveButton.Bind(wx.EVT_BUTTON, save)

filename = wx.TextCtrl(win, pos=(5,5), size=(210,25))

contents = wx.TextCtrl(win, pos=(5,35),size=(390,260),style=wx.TE_MULTILINE|wx.HSCROLL)
win.Show()
app.MainLoop()