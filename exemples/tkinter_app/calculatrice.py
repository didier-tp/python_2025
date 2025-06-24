
import tkinter as tk 

#create (default) top level window first:
mainWindow = tk.Tk()
mainWindow.title("calculatrice")
mainWindow.geometry("400x200")

resTkStringVar = tk.StringVar() # for binding content of labelRes or entryRes
resTkStringVar.set("0") #defaut value

def computeRes(op):
    x=entryX.get()
    y=entryY.get()
    try:
        match op:
            case "+":
                z=float(x)+float(y)
            case "-":
                z=float(x)-float(y)
            case "*":
                z=float(x)*float(y)
            case "/":
                z=float(x)/float(y)
            case _:
                z=0
    except Exception:
        z=0
    resTkStringVar.set(str(z))

def onAdd():
    computeRes("+")

def onMult():
    computeRes("*")  

def onMinus():
    computeRes("-")

def onDiv():
    computeRes("/")  

panelX = tk.Frame(mainWindow)
labelX = tk.Label(panelX, text="x:");labelX.pack(side="left")
entryX = tk.Entry(panelX,width=50); entryX.pack(side="right")
panelX.pack()

panelY = tk.Frame(mainWindow)
labelY = tk.Label(panelY, text="y:");labelY.pack(side="left")
entryY = tk.Entry(panelY,width=50); entryY.pack(side="left")
panelY.pack()


panelBtn = tk.Frame(mainWindow)
buttonAdd = tk.Button(panelBtn,text="+" , command=onAdd)
buttonAdd.grid(row=1,column=1,padx=4,pady=2)
buttonMult = tk.Button(panelBtn,text="*" , command=onMult)
buttonMult.grid(row=1,column=2,padx=4,pady=2)
buttonMinus = tk.Button(panelBtn,text="-" , command=onMinus)
buttonMinus.grid(row=1,column=3,padx=4,pady=2)
buttonDiv = tk.Button(panelBtn,text="/" , command=onDiv)
buttonDiv.grid(row=1,column=4,padx=4,pady=2)
panelBtn.pack()

panelRes = tk.Frame(mainWindow)
labelOfLabelRes = tk.Label(panelRes, text="res:")
labelOfLabelRes.pack(side="left")
#labelRes = tk.Label(panelRes, textvariable=resTkStringVar)
#labelRes.pack(side="right")
entryRes = tk.Entry(panelRes, textvariable=resTkStringVar,width=50)
entryRes.pack(side="right")
panelRes.pack()

mainWindow.mainloop()


