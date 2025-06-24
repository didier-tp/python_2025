
import tkinter as tk

#create (default) top level window first:
mainWindow = tk.Tk()
mainWindow.title("counter")
mainWindow.geometry("300x100")# width x height + x + y

counterTkStringVar = tk.StringVar() # for binding content of labelCounter
counterTkStringVar.set("0") #default value


def onOpButtonPress(event):
    button = event.widget
    buttonText= button['text']
    v=int(counterTkStringVar.get())
    if buttonText=="++" :
        v+=1
    else:
        v-=1
    counterTkStringVar.set(str(v))

def onResetCommand():
    counterTkStringVar.set("0") 


labelCounter = tk.Label(mainWindow, textvariable=counterTkStringVar)
labelCounter.pack()

btnFrame = tk.Frame(mainWindow)

buttonIncrement = tk.Button(btnFrame,text="++")
#buttonIncrement.pack() #without grid 
buttonIncrement.grid(row=1,column=1,padx=4,pady=2)
buttonIncrement.bind("<ButtonPress>",onOpButtonPress)

buttonDecrement = tk.Button(btnFrame,text="--")
buttonDecrement.bind("<ButtonPress>",onOpButtonPress)
#buttonDecrement.pack() #without grid 
buttonDecrement.grid(row=1,column=2,padx=4,pady=2)

buttonReset = tk.Button(btnFrame,text="reset",command=onResetCommand)
#buttonReset.pack() #without grid 
buttonReset.grid(row=1,column=3,padx=4,pady=2)

btnFrame.pack()

mainWindow.mainloop()