import random

import requests

url = 'https://rickandmortyapi.com/api/character/'
pAl = random.randint(1,826)
webContent = requests.get(f"{url}{pAl}")
personajes = webContent.json()
claves = list(personajes.keys())
valores = list(personajes.values())

def estaVivo(personaje):
    if personajes["status"].lower() == "dead":
        return "muerto"
    elif personajes["status"].lower() == "unknown":
        return "desconocido"
    return "vivo"

def especie(personaje):
    return personajes["species"]

def genero(personaje):
    return personajes["gender"]

def origen(personaje):
    return personajes["location"]

localizacion = valores[6]
loc = localizacion["name"]
"""
urllo = valores[6]["url]
localizacionRequest = requests.get(urllo)
localizacion = localizacionRequest.json()
print(f"localizacion: {localizacion["name"]}")
"""
print(claves)
continuar = True
while continuar:
    nombre = input("Adivina el nombre del personaje:\n")
    if nombre==personajes["name"]:
        print("Bien")
    else:
        print(f"El personaje está: {estaVivo(valores[2])}")
        print(f"La especie del personaje: {especie(valores[3])}")
        print(f"El género del personaje es: {genero(valores[5])}")
        print(f"El lugar de origen del usuario es: {valores[6]["name"]}")
print(f"El nombre es: {personajes["name"]}")
