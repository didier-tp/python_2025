import tkinter as tk # partie principale/native de tkinter
from tkinter import ttk # extension classique de tkinter (Combobox, ...)
import tkinter.messagebox as tkmb;
import tkinter.filedialog  as tkfd;
from my_tkinter_util import buttonsInRowFrame,withinFrameWithLabel

#NB: PIL is for Python Image Library , cette extension necessite de lancer pip install pillow
#avec python3 , PIL/pillow sert à gérer plus de formats d'images (ex: .jpeg et autres en plus de .png)
#from  PIL import Image as PilImage, ImageTk as PilImageTk #necessite pip install pillow
#pilImage = PilImage.open('fleur.jpeg')
#tkImage = PilImageTk.PhotoImage(pilImage)

#create (default) top level window first:
mainWindow = tk.Tk()
mainWindow.title("principaux widgets de tkinter")
mainWindow.geometry("600x600")

fileImageName="python.png" # by default (or "user_icon.png")

#nb: display order = order of subComponent.pack() or .grid()

formLabelFrame = tk.LabelFrame(mainWindow,text="formulaire",padx=2,pady=2)#internal padding

def dualDisplay(label,val):
    print(label,val)
    valuesText.insert(tk.END,f'{label}={val}\n')

def displayValues():
    valuesText.delete('1.0',tk.END)
    dualDisplay("username",usernameStrVar.get())
    dualDisplay("sportif",sportifStrVar.get())
    dualDisplay("ville",villeStrVar.get())
    dualDisplay("situation",situationStrVar.get())
    dualDisplay("level",levelStrVar.get())
    dualDisplay("temperature",temperatureVar.get())
    dualDisplay("fileImageName",fileImageName)

def clearCanvas():
    #canvas.delete(1,3) # delete elements of index 1 and 3 s'ils existent
    canvas.delete(tk.ALL)

def drawInCanvas():
    ligne1Index = canvas.create_line(5, 5, 175, 70 , width=2 ,fill="blue")
    cercle1Index = canvas.create_oval(5,75,125,100,fill="red")
    rectangle1Index = canvas.create_rectangle(165,75,225,100,fill="green")
    print(f'ligne1Index={ligne1Index} cercle1Index={cercle1Index} rectangle1Index={rectangle1Index}')


def imageInCanvas(): 
    #photo1 = tk.PhotoImage(file="python.png")
    #photo1 = tk.PhotoImage(file="user_icon.png")
    photo1 = tk.PhotoImage(file=fileImageName)

    #pilImage = PilImage.open('fleur.jpeg')
    #tkImage = PilImageTk.PhotoImage(pilImage)
    #photo1=tkImage
    
    #image_label = tk.Label(mainWindow, image=photo1,width=100,height=100)
    #image_label.image=photo1
    #image_label.pack()
    
    #photo1=photo1.zoom(2,2)#coefX, coefY as int (larger image)
    #photo1=photo1.subsample(2,2) # smaller image
    image1 = canvas.create_image(0, 0, anchor=tk.NW, image=photo1)
    canvas.image=photo1 # ??? but necessary !!!
 


panelRowUsername = tk.Frame(formLabelFrame)
usernameStrVar = tk.StringVar(value="super_user")
usernameEntry= tk.Entry(panelRowUsername,textvariable=usernameStrVar)
withinFrameWithLabel(panelRowUsername,"username:",usernameEntry)  

panelRowSportif = tk.Frame(formLabelFrame)
sportifStrVar = tk.BooleanVar()
sportifCheckbox= tk.Checkbutton(panelRowSportif,text="sportif",variable=sportifStrVar)
withinFrameWithLabel(panelRowSportif,"   ",sportifCheckbox)

panelRowEnCouple = tk.Frame(formLabelFrame)
situationStrVar = tk.StringVar(value="?")
inconnuRadioButton= tk.Radiobutton(panelRowEnCouple,text="?",value="?" ,variable=situationStrVar)
enCoupleRadioButton= tk.Radiobutton(panelRowEnCouple,text="en couple",value="en_couple",variable=situationStrVar)
celibataireRadioButton= tk.Radiobutton(panelRowEnCouple,text="celibataire",value="celibataire",variable=situationStrVar)
withinFrameWithLabel(panelRowEnCouple,"situation:",inconnuRadioButton,enCoupleRadioButton,celibataireRadioButton)

panelRowVilles = tk.Frame(formLabelFrame)
villeStrVar = tk.StringVar(value="Paris")
villeComboBox= ttk.Combobox(panelRowVilles,textvariable=villeStrVar)
villeComboBox["values"] = ( "Lyon" , "Paris" , "Toulouse")
withinFrameWithLabel(panelRowVilles,"ville:",villeComboBox)

panelRowLevel = tk.Frame(formLabelFrame)
levelStrVar = tk.StringVar(value="1")
levelSpinbox= tk.Spinbox(panelRowLevel,from_="1",to="5",textvariable=levelStrVar)
withinFrameWithLabel(panelRowLevel,"level:",levelSpinbox)

panelRowTemperature = tk.Frame(formLabelFrame)
temperatureVar = tk.DoubleVar(value=22.5)
temperatureScale= tk.Scale(panelRowTemperature,from_=-30,to=50,
                           variable=temperatureVar,orient=tk.HORIZONTAL,resolution=0.5)
withinFrameWithLabel(panelRowTemperature,"temperature:",temperatureScale)

formLabelFrame.pack( padx=10, pady=10)
#formLabelFrame.pack(fill="x",expand="yes" , padx=10, pady=10)
#formLabelFrame.pack(fill="both",expand="yes" , padx=10, pady=10)

buttonsInRowFrame(mainWindow,[
    ("display values",displayValues),
    ("clear canvas",clearCanvas),
    ("drawing in canvas",drawInCanvas),
    ("image in canvas",imageInCanvas)
    ])


panelValues = tk.Frame(mainWindow)
valuesText= tk.Text(panelValues,width=50,height=8)#width,height in number of lines/columns
withinFrameWithLabel(panelValues,"values:",valuesText)

panedWindow = tk.PanedWindow(mainWindow, orient=tk.HORIZONTAL)
#panedWindow = Frame with resizable subcomponents (via slider)
panedWindow.add(tk.Label(panedWindow, text='Resizable part 1', background='lightgreen', anchor=tk.CENTER , height=5))
panedWindow.add(tk.Label(panedWindow, text='Resizable part 2', background='lightblue', anchor=tk.CENTER , height=5) )
panedWindow.pack(side=tk.BOTTOM, expand="yes", fill=tk.X, pady=2, padx=2)

canvasLabelFrame = tk.LabelFrame(mainWindow,text="canvas (drawing)",padx=2,pady=2)#internal padding
canvas = tk.Canvas(canvasLabelFrame, width=400, height=150, background='lightgrey')
canvas.pack()
canvasLabelFrame.pack(padx=2, pady=2)
#dessiner dans le canvas: --> voir fonction drawInCanvas()



#build and add menubar:

def showMessageDialog(message):
    tkmb.showinfo("info",message)

def cmde_choose_imageName():
    #showMessageDialog("choose_imageName")
    global fileImageName 
    fileImageName=tkfd.askopenfilename(title="Choisir une image",
                                       filetypes=[('png files','.png'),('all files','.*')])

def cmde_about():
    showMessageDialog("about / ex_widgets / python")    

menubar = tk.Menu(mainWindow)

subMenuFile = tk.Menu(menubar, tearoff=0)
subMenuFile.add_command(label="Choose image", command=cmde_choose_imageName)
subMenuFile.add_separator()
subMenuFile.add_command(label="Quit", command=mainWindow.quit)
menubar.add_cascade(label="File", menu=subMenuFile)

subMenuEdit = tk.Menu(menubar, tearoff=0)
subMenuEdit.add_command(label="displayValues", command=displayValues)
menubar.add_cascade(label="Edit", menu=subMenuEdit)

subMenuHelp = tk.Menu(menubar, tearoff=0)
subMenuHelp.add_command(label="about", command=cmde_about)
menubar.add_cascade(label="Help", menu=subMenuHelp)

mainWindow.config(menu=menubar)


mainWindow.mainloop()