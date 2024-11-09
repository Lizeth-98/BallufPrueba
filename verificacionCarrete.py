# -*- coding: utf-8 -*-
"""
@author: cs940
"""
#importar tkinte, json,asyncio
import tkinter as tk
import json
import asyncio
from tkinter import messagebox

# obtener los datos del archivo json
with open("C:/Users/cs940/OneDrive/Documentos/6A TIIA/Estadias/bd-carrete.txt") as file:
    data = json.load(file)

# Función asincrónica para verificar la descripción y el material
async def verificar_carrete(descripcion, material):
    # Simular la llamda a la base da dts
    await asyncio.sleep(0.1)
    for item in data:
        if item["description"] == descripcion and str(item["material"]) == material:
            return True
    return False

# boton de verificar
def verificar():
    descripcion_material = entry_descripcion.get()
    numero_material = entry_material.get()

    # tarea creacion
    asyncio.create_task(verificar_async(descripcion_material, numero_material))

# ejecutar la verificacion y motrar el cuadro de texto del resultado
async def verificar_async(descripcion_material, numero_material):
    resultado = await verificar_carrete(descripcion_material, numero_material)
    if resultado:
        messagebox.showinfo("Verificacion", "Carrete correcto")
    else:
        messagebox.showwarning("Verificacion", "Carrete incorrecto")

# interfaz
root = tk.Tk()
root.title("Carrete")

# etiquetas y campos de entrada
tk.Label(root, text="Descripcion").grid(row=0, column=0)
entry_descripcion = tk.Entry(root)
entry_descripcion.grid(row=0, column=1)

tk.Label(root, text="material").grid(row=1, column=0)
entry_material = tk.Entry(root)
entry_material.grid(row=1, column=1)

# Botón de verificación
btn_verificar = tk.Button(root, text="verificar", command=verificar)
btn_verificar.grid(row=2, column=0, columnspan=2)

root.mainloop()
