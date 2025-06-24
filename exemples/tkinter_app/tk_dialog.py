
import tkinter.messagebox as tkmb;
import tkinter.simpledialog as tksd;
import tkinter.filedialog as tkfd;


#username = tksd.askstring("saisir username" , "username:")
age = tksd.askinteger("saisir age" , "age:")
#taille = tksd.askfloat("saisir taille (cm)" , "taille:")

if age < 0 :
    tkmb.showerror("erreur de saisie" , "age négatif invalide")
else:
    tkmb.showinfo("info",f'age={age}')
    if age < 18 :
        tkmb.showwarning("mineur" , "vente d'alcool interdite")

responseFouOuPas = tkmb.askyesno(message="Etes vous fou ?")
print(f'responseFouOuPas={responseFouOuPas}') # True or False