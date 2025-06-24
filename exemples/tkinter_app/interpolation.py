import tkinter as tk # partie principale/native de tkinter
from tkinter import ttk # extension classique de tkinter (Combobox, ...)

import numpy as np # nécessite pip install numpy
# np.mean() calcule la moyenne
# np.var() calcule la variance
# numpy.cov(a, b, bias=True)[0][1]ou bien numpy.cov(a, b, ddof=0)[0][1]calcule la covariance
from my_tkinter_util import buttonsInRowFrame,withinFrameWithLabel

nbPoints=0
tabX=[]
tabY=[]

def onButtonReleaseOverCanvas(event):
    x=event.x; y=event.y
    print("onButtonReleaseOverCanvas with event=",event) 
    canvas.create_oval(x-1, y-1, x+1, y+1 , width=1 ,fill="black")
    global nbPoints,tabX,tabY
    y=inverserSensY(y)
    tabX.append(x); tabY.append(y)
    nbPoints+=1
    strPoint = f"(x={x},y={y})"
    listboxPoints.insert(tk.END , strPoint)


def clearAll():
    canvas.delete(tk.ALL)
    aTkStringVar.set("a=?")
    bTkStringVar.set("b=?")
    listboxPoints.delete(0,tk.END)
    global nbPoints,tabX,tabY
    nbPoints=0
    tabX=[]
    tabY=[]

def inverserSensY(originalY):
    return canvas.winfo_reqheight() - originalY

def tracerDroiteAfoisXplusB(a,b):
    x0=0; y0=b
    y0=canvas.winfo_reqheight() - y0
    x=canvas.winfo_reqwidth()
    y=a*x+b
    y=canvas.winfo_reqheight() - y
    canvas.create_line(x0, y0, x, y , width=1 ,fill="red")

def calculerInterpolation():
    global nbPoints,tabX,tabY
    print(f"calculerInterpolation: nbPoints={nbPoints}")
    moyenneX=np.mean(tabX)
    moyenneY=np.mean(tabY) 
    #varianceX=np.var(tabX)
    varianceX=np.var(tabX,ddof=0)
    #covarianceXY= np.cov(tabX, tabY)[0][1] 
    #covarianceXY= np.cov(tabX, tabY, bias=True)[0][1] 
    covarianceXY= np.cov(tabX, tabY, ddof=0)[0][1]   
    a = covarianceXY / varianceX
    b =  moyenneY - a * moyenneX
    aTkStringVar.set(f"a={a}")
    bTkStringVar.set(f"b={b}")
    tracerDroiteAfoisXplusB(a,b)

#create (default) top level window first:
mainWindow = tk.Tk()
mainWindow.title("interpolation (y=a*x+b)")
mainWindow.geometry("600x450")

panedWindow = tk.PanedWindow(mainWindow, orient=tk.HORIZONTAL)
#panedWindow = Frame with resizable subcomponents (via slider)

ptsEqLabelFrame = tk.LabelFrame(panedWindow,text="points et equation",padx=2,pady=2,background='lightgreen')

buttonClear = tk.Button(ptsEqLabelFrame,text="effacer", command=clearAll)
buttonClear.pack(side="top",padx=2)

buttonCalculerInterpolation = tk.Button(ptsEqLabelFrame,text="calculer interpolation", command=calculerInterpolation)
buttonCalculerInterpolation.pack(side="top",pady=2)


labelEq = tk.Label(ptsEqLabelFrame, text="y=a*x+b")
labelEq.pack()

aTkStringVar = tk.StringVar(value="a=?")
labelA = tk.Label(ptsEqLabelFrame, textvariable=aTkStringVar)
labelA.pack()

bTkStringVar = tk.StringVar(value="b=?")
labelB = tk.Label(ptsEqLabelFrame, textvariable=bTkStringVar)
labelB.pack()

listboxPoints = tk.Listbox(ptsEqLabelFrame,height=18)
listboxPoints.pack(side="bottom",pady=1)

ptsEqLabelFrame.pack()
panedWindow.add(ptsEqLabelFrame)


canvasLabelFrame = tk.LabelFrame(panedWindow,text="canvas",padx=2,pady=2)#internal padding
canvas = tk.Canvas(canvasLabelFrame, width=550, height=400, background='white')
canvas.pack()
canvasLabelFrame.pack(padx=2, pady=2)

panedWindow.add(canvasLabelFrame )

canvas.bind("<ButtonRelease>",onButtonReleaseOverCanvas)


panedWindow.pack(side=tk.BOTTOM, expand="yes", fill=tk.X, pady=2, padx=2)

mainWindow.mainloop()