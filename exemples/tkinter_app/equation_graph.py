import tkinter as tk
from math import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)

#--------------------------------------------------
plot1=None

def plotEquationCurve():
    xMin=-10
    xMax=10
    nbPoints=100
    dx=(xMax-xMin)/100
    strEq=eqStrVar.get()

    # the figure that will contain the plot (figsize=(width,height) in inches)
    fig = Figure(figsize = (5, 5),dpi = 100)

    #embbed fig in tkinter canvas in main_window:
    global canvas
    if not canvas :
        integrateMatplotlibFigureInTKinter(fig)

    #eval equation expression:
    xValues=[]
    yValues=[]
    for i in range(nbPoints+1):
        x=xMin + i*dx
        xValues.append(x)
        y=eval(strEq)
        #print(f'x={x} y={y}')
        yValues.append(y)

    # adding the subplot with classic/default option:
    global plot1
    if not plot1:
        plot1 = fig.add_subplot(1,1,1)
    else:
        plot1.clear()

    # plotting the graph
    plot1.plot(xValues,yValues)
    #refresh plot1 in fig in canvas:
    canvas.draw()

   

#--------------------------------------------------
canvas=None

def integrateMatplotlibFigureInTKinter(fig): 
    global canvas
    #print(f"integrateMatplotlibFigureInTKinter: canvas={canvas} fig={fig}")

    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master = main_window)  
    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   main_window)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()   

#--------------------------------------------------    

# the main Tkinter window
main_window = tk.Tk()
main_window.title('eval and matplotlib in tkinter')
main_window.geometry("600x600")

eqFrame = tk.Frame(main_window)

eqLabel = tk.Label(eqFrame,text="y=")
eqLabel.pack(side="left")

plot_button = tk.Button(eqFrame,command = plotEquationCurve,text = "Plot")
plot_button.pack(side="right")

eqStrVar = tk.StringVar(value="x*x")
eqEntry= tk.Entry(eqFrame,textvariable=eqStrVar)
eqEntry.pack(side="right",padx=5)

eqFrame.pack(side="top")

main_window.mainloop()