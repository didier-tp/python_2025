
import tkinter as tk # partie principale/native de tkinter
from tkinter import ttk # extension classique de tkinter (Combobox, ...)
from my_tkinter_util import buttonsInRowFrame,entryStringVarWithLabelInFrame,withinFrameWithLabel

# V2 with button and ttk.Combobox (or Radiobuttons)

#create (default) top level window first:
mainWindow = tk.Tk()
mainWindow.title("calcul de tva")
mainWindow.geometry("400x200")

tvaTkStringVar = tk.StringVar(value="0") # for binding content of labelTva or entryTva
ttcTkStringVar = tk.StringVar(value="0") # for binding content of labelTtc or entryTtc

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

panelRowTaux = tk.Frame(mainWindow)
entryTauxStrVar = tk.StringVar(value="20")
tauxComboBox= ttk.Combobox(panelRowTaux,textvariable=entryTauxStrVar)
tauxComboBox["values"] = ( "5" , "10" , "20")
withinFrameWithLabel(panelRowTaux,"taux(%):",tauxComboBox)


buttonsInRowFrame(mainWindow,[
    ("calculer tva et ttc",computeTvaAndTtc)
    ])


entryStringVarWithLabelInFrame(mainWindow,"tva:",textvariable=tvaTkStringVar)
entryStringVarWithLabelInFrame(mainWindow,"ttc:",textvariable=ttcTkStringVar)

mainWindow.mainloop()




