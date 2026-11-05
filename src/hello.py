import tkinter as tk


def saludar():
    nombre = var_nombre.get().strip()
    apellido = var_apellido.get().strip()

    if nombre == "" or apellido == "":
        var_saludo.set("Completa nombre y apellido")
        etiqueta_resultado.config(fg="red")
    else:
        var_saludo.set("¡Hola, " + nombre + " " + apellido + "!")
        etiqueta_resultado.config(fg="#1E8449")
        print(var_saludo.get())


root = tk.Tk()
root.title("Saludo con StringVar")
root.geometry("400x320")
root.config(bg="#F4F6F7")

var_nombre = tk.StringVar()
var_apellido = tk.StringVar()
var_saludo = tk.StringVar()

etiqueta_titulo = tk.Label(root, text="Registro de saludo", font=("Arial", 16, "bold"),
                           bg="#F4F6F7", fg="#2C3E50")
etiqueta_titulo.grid(row=0, column=0, columnspan=2, pady=15)

etiqueta_nombre = tk.Label(root, text="Nombre:", font=("Arial", 11, "bold"),
                           bg="#F4F6F7", fg="#34495E")
etiqueta_nombre.grid(row=1, column=0, padx=10, pady=8, sticky="e")

entrada_nombre = tk.Entry(root, textvariable=var_nombre, width=22, font=("Arial", 11),
                          bg="white", fg="#2C3E50", relief="solid", bd=1)
entrada_nombre.grid(row=1, column=1, padx=10, pady=8)

etiqueta_apellido = tk.Label(root, text="Apellido:", font=("Arial", 11, "bold"),
                             bg="#F4F6F7", fg="#34495E")
etiqueta_apellido.grid(row=2, column=0, padx=10, pady=8, sticky="e")

entrada_apellido = tk.Entry(root, textvariable=var_apellido, width=22, font=("Arial", 11),
                            bg="white", fg="#2C3E50", relief="solid", bd=1)
entrada_apellido.grid(row=2, column=1, padx=10, pady=8)

boton_saludar = tk.Button(root, text="Saludar", font=("Arial", 11, "bold"),
                          bg="#2E86DE", fg="white", width=15, command=saludar)
boton_saludar.grid(row=3, column=0, columnspan=2, pady=15)

etiqueta_resultado = tk.Label(root, textvariable=var_saludo, font=("Arial", 13),
                              bg="#F4F6F7")
etiqueta_resultado.grid(row=4, column=0, columnspan=2, pady=10)

entrada_nombre.focus()

root.mainloop()