import tkinter as tk 

def withinFrameWithLabel(frame,labelText,tkControl,*othersControls):
    labelTk = tk.Label(frame, text=labelText,width=12)
    labelTk.pack(side="left")
    tkControl.pack(side="right")
    for otherControl in othersControls:
         otherControl.pack(side="right")
    frame.pack()


def entryStringVarWithLabelInFrame(master,labelText,textvariable=None):
       panelRow = tk.Frame(master)
       if not textvariable :
            textvariable = tk.StringVar()
       entryTk = tk.Entry(panelRow,width=48,textvariable=textvariable)
       withinFrameWithLabel(panelRow,labelText,entryTk)
       return textvariable

def buttonsInRowFrame(master,buttonLabelCommandTupleList):
    panelRow = tk.Frame(master)
    c=1
    for (btnLabel,btnCommand) in buttonLabelCommandTupleList:
        btn = tk.Button(panelRow,text=btnLabel , command=btnCommand)
        btn.grid(row=1,column=c,padx=2,pady=2)
        c+=1
    panelRow.pack()