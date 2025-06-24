import tkinter as tk # partie principale/native de tkinter
from tkinter import ttk # extension classique de tkinter (Combobox, ...)
from my_tkinter_util import buttonsInRowFrame,withinFrameWithLabel

x1=0;y1=0 #coordonnées (à actualiser) du début la figure courante à dessiner

def onButtonPressOverCanvas(event):
    print("onButtonPressOverCanvas with event=",event)
    global x1,y1
    x1=event.x; y1=event.y

def onButtonReleaseOverCanvas(event):
    global x1,y1
    print("onButtonReleaseOverCanvas with event=",event) 
    x2=event.x; y2=event.y
    couleur=couleurStrVar.get()
    match typeFigStrVar.get() :
        case "ligne" :
            canvas.create_line(x1, y1, x2, y2 , width=1 ,fill=couleur)
        case "rectangle" :
            canvas.create_rectangle(x1, y1, x2, y2 , width=1 ,fill=couleur) 
        case "oval" :
            canvas.create_oval(x1, y1, x2, y2 , width=1 ,fill=couleur)  

def clearCanvas():
    canvas.delete(tk.ALL)

#create (default) top level window first:
mainWindow = tk.Tk()
mainWindow.title("dessin")
mainWindow.geometry("600x500")

panelRowTypefig = tk.Frame(mainWindow)
typeFigStrVar = tk.StringVar(value="ligne")
ligneRadioButton= tk.Radiobutton(panelRowTypefig,text="ligne",value="ligne" ,variable=typeFigStrVar)
rectangleRadioButton= tk.Radiobutton(panelRowTypefig,text="rectangle",value="rectangle",variable=typeFigStrVar)
ovalRadioButton= tk.Radiobutton(panelRowTypefig,text="oval",value="oval",variable=typeFigStrVar)
withinFrameWithLabel(panelRowTypefig,"type figure:",ligneRadioButton,rectangleRadioButton,ovalRadioButton)

panelRowCouleurs = tk.Frame(mainWindow)
couleurStrVar = tk.StringVar(value="black")
couleurComboBox= ttk.Combobox(panelRowCouleurs,textvariable=couleurStrVar)
couleurComboBox["values"] = ( "black" , "blue" , "red" , "green" , "orange", "yellow")
buttonClear = tk.Button(panelRowCouleurs,text="effacer", command=clearCanvas)
buttonClear.pack(side="right",padx=12)
withinFrameWithLabel(panelRowCouleurs,"couleur:",couleurComboBox)


canvasLabelFrame = tk.LabelFrame(mainWindow,text="canvas (drawing)",padx=2,pady=2)#internal padding
canvas = tk.Canvas(canvasLabelFrame, width=550, height=400, background='white')
canvas.pack()
canvasLabelFrame.pack(padx=2, pady=2)

canvas.bind("<ButtonPress>",onButtonPressOverCanvas)
canvas.bind("<ButtonRelease>",onButtonReleaseOverCanvas)

mainWindow.mainloop()