
import tkinter as tk 
from my_tkinter_util import buttonsInRowFrame,entryStringVarWithLabelInFrame

# V1 with Entry and Button

#create (default) top level window first:
mainWindow = tk.Tk()
mainWindow.title("calcul de tva")
mainWindow.geometry("400x200")

tvaTkStringVar = tk.StringVar(value="0") 
ttcTkStringVar = tk.StringVar(value="0") 

def computeTvaAndTtc():
    ht=entryHtStrVar.get()
    tauxTvaPct=entryTauxStrVar.get()
    try:
        tva=float(ht)*(float(tauxTvaPct)/100)
        ttc=float(ht)+tva
    except Exception:
        tva=0
        ttc=0
    tvaTkStringVar.set(str(tva))
    ttcTkStringVar.set(str(ttc))

 
entryHtStrVar =   entryStringVarWithLabelInFrame(mainWindow,"ht: ")
entryTauxStrVar = entryStringVarWithLabelInFrame(mainWindow,"taux(%):",
                                                 textvariable=tk.StringVar(value="20"))

buttonsInRowFrame(mainWindow,[
    ("calculer tva et ttc",computeTvaAndTtc)
    ])


entryStringVarWithLabelInFrame(mainWindow,"tva:",textvariable=tvaTkStringVar)
entryStringVarWithLabelInFrame(mainWindow,"ttc:",textvariable=ttcTkStringVar) 


mainWindow.mainloop()




