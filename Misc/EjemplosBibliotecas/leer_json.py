from easygui import fileopenbox
import json

ruta = fileopenbox(msg="Seleccione Archivo", title="Seleccione Archivo JSON", filetypes=["*.json"])

with open(ruta, "r") as archivo:
    contenido_json = archivo.read()

dic_productos = json.loads(contenido_json)

for producto in dic_productos:
    print(f"Nombre del producto: {producto['name']}")