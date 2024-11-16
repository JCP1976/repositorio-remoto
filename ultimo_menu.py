import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess

# Funciones para las opciones del submenú
def submenu_opcion_1():
    messagebox.showinfo("Submenú Opción 1", "Has seleccionado la Subopción 1")

def submenu_opcion_2():
    messagebox.showinfo("Submenú Opción 2", "Has seleccionado la Subopción 2")

def submenu_opcion_3():
    messagebox.showinfo("Submenú Opción 3", "Has seleccionado la Subopción 3")

def mostrar_submenu():
    # Crear una nueva ventana para el submenú
    submenu_ventana = tk.Toplevel(ventana)
    submenu_ventana.title("Submenú")
    submenu_ventana.geometry("250x150")

    # Crear botones en la ventana del submenú
    boton_subopcion_1 = tk.Button(submenu_ventana, text="Subopción 1", command=submenu_opcion_1, font=("Helvetica", 10), bg="lightblue")
    boton_subopcion_1.pack(pady=3)

    boton_subopcion_2 = tk.Button(submenu_ventana, text="Subopción 2", command=submenu_opcion_2, font=("Helvetica", 10), bg="lightgreen")
    boton_subopcion_2.pack(pady=3)

    boton_subopcion_3 = tk.Button(submenu_ventana, text="Subopción 3", command=submenu_opcion_3, font=("Helvetica", 10), bg="lightyellow")
    boton_subopcion_3.pack(pady=3)

# Función para ejecutar el script externo
def ejecutar_script():
    try:
        # Ejecutar script1.py usando subprocess
        subprocess.run(["python", "script1.py"], check=True)  # Usar "python3" si es necesario
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Hubo un error al ejecutar el script: {e}")

def opcion_1():
    mostrar_submenu()

def opcion_2():
    # Llamar a la función para ejecutar el script
    ejecutar_script()

def salir():
    ventana.quit()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Menú Gráfico")
ventana.geometry("800x600")

# Cargar la imagen de fondo
imagen_fondo = Image.open("G:\\Unidades compartidas\\RPA_Torija\\menu\\mi_icono.ico")  # Cambia por el nombre de tu imagen
imagen_fondo = imagen_fondo.resize((300, 300))
imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)

# Colocar la imagen de fondo
label_fondo = tk.Label(ventana, image=imagen_fondo_tk)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

# Crear un marco para organizar los botones
frame_botonera = tk.Frame(ventana, bg="white", bd=5)
frame_botonera.place(x=10, y=10)  # Posicionar el marco en la esquina superior izquierda

# Crear botones en la ventana que representan las opciones del menú
boton_opcion_1 = tk.Button(frame_botonera, text="Control de Stock", command=opcion_1, font=("Helvetica", 10), bg="lightblue")
boton_opcion_1.pack(pady=3)

boton_opcion_2 = tk.Button(frame_botonera, text="Tránsito             ", command=opcion_2, font=("Helvetica", 10), bg="lightgreen")
boton_opcion_2.pack(pady=3)

boton_salir = tk.Button(frame_botonera, text="Salir                   ", command=salir, font=("Helvetica", 10), bg="lightcoral")
boton_salir.pack(pady=40)

# Iniciar el bucle principal de la ventana
ventana.mainloop()
