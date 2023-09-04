from tkinter import *

raiz = Tk()
raiz.title("Interfaz Caliper")
raiz.config(bg="gray")
raiz.geometry("500x250")
raiz.resizable(0,0)

tablero = Entry(width=22,font=("Arial", 28))
tablero.config(bg="green")
tablero.config() 

tablero.place(x=15, y=90)


boton_rojo = Button(width=15,height=2,bg="red")
boton_rojo.place(x=60,y=180)
labelON = Label(text="ON",font=("Arial", 18),bg="gray")
labelON.place(x=180,y=185)
labelOFF = Label(text="OFF",font=("Arial", 18),bg="gray")
labelOFF.place(x=2,y=185)


boton_azul = Button(width=15,height=2,bg="blue")
boton_azul.place(x=300,y=180)
labelZero = Label(text="ZERO",font=("Arial", 18),bg="gray")
labelZero.place(x=420,y=185)

boton_amarillo = Button(width=15,height=2,bg="yellow")
boton_amarillo.place(x=330,y=25)
labelUnidad = Label(text="mm/inch",font=("Arial", 18),bg="gray")
labelUnidad.place(x=230,y=30)





raiz. mainloop()