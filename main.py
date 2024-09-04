from tkinter import Tk, Button, Entry, Label

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("402x320")

# Configuración pantalla de salida 
pantalla = Entry(root, width=40, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=200, padx=1, pady=0)

# Configuración botones
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command= lambda: boton_click(1)).grid(row=1, column=0, padx=1, pady=1)
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command= lambda: boton_click(2)).grid(row=1, column=1, padx=1, pady=1)
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command= lambda: boton_click(3)).grid(row=1, column=2, padx=1, pady=1)

boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command= lambda: boton_click(4)).grid(row=2, column=0, padx=1, pady=1)
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command= lambda: boton_click(5)).grid(row=2, column=1, padx=1, pady=1)
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command= lambda: boton_click(6)).grid(row=2, column=2, padx=1, pady=1)

boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command= lambda: boton_click(7)).grid(row=3, column=0, padx=1, pady=1)
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command= lambda: boton_click(8)).grid(row=3, column=1, padx=1, pady=1)
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command= lambda: boton_click(9)).grid(row=3, column=2, padx=1, pady=1)

boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2", command= lambda: calcularResultado()).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0).grid(row=4, column=2, padx=1, pady=1)
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command= lambda: boton_click("+")).grid(row=1, column=3, padx=1, pady=1)
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command= lambda: boton_click("-")).grid(row=2, column=3, padx=1, pady=1)
boton_multiplicacion = Button(root, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command= lambda: boton_click("*")).grid(row=3, column=3, padx=1, pady=1)
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command= lambda: boton_click("/")).grid(row=4, column=3, padx=1, pady=1)

#Eventos

boton_presionado_1 = None #Boton que guardar el primer valor numerico
boton_presionado_2 = None #Boton que guardar el la operación
boton_presionado_3 = None #Boton que guarda el segundo valor

def boton_click(valor):
    global boton_presionado_1, boton_presionado_2, boton_presionado_3
    if boton_presionado_1 is None:
        boton_presionado_1 = valor
        actualizarPantalla(boton_presionado_1)
    elif boton_presionado_2 is None:
        boton_presionado_2 = valor
        actualizarPantalla(boton_presionado_2)
    elif boton_presionado_3 is None:
        boton_presionado_3 = valor
        actualizarPantalla(boton_presionado_3)

#Configuracion para mostrar los numeros en la pantalla.
def actualizarPantalla(valor):
    pantalla.insert("end", str(valor))

def botonOperacion(operacion):
    global boton_presionado_2
    boton_presionado_2 = operacion
    pantalla.insert("end", " " + operacion + " ")

def calcularResultado():
    global boton_presionado_1, boton_presionado_2, boton_presionado_3

    if boton_presionado_1 is not None and boton_presionado_3 is not None and boton_presionado_2:
        try:
            if boton_presionado_2 == "+":
                resultado = boton_presionado_1 + boton_presionado_3
            elif boton_presionado_2 == "-":
                resultado = boton_presionado_1 - boton_presionado_3
            elif boton_presionado_2 == "*":
                resultado = boton_presionado_1 * boton_presionado_3
            elif boton_presionado_2 == "/":
                resultado = boton_presionado_1 / boton_presionado_3
                
            pantalla.delete(0, "end")
            pantalla.insert("end", str(resultado))
        except Exception as e:
            pantalla.delete(0, "end")
            pantalla.insert("end", "Error")
        
        boton_presionado_1 = None
        boton_presionado_2 = None
        boton_presionado_3 = None

def limpiarPantalla():
    global boton_presionado_1, boton_presionado_2, boton_presionado_3
    pantalla.delete(0, "end")
    boton_presionado_1 = None
    boton_presionado_2 = None
    boton_presionado_3 = None

root.mainloop()