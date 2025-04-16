import random

import requests

url = 'https://rickandmortyapi.com/api/character/'
pAl = random.randint(1,826)
webContent = requests.get(f"{url}{pAl}")
personaje = webContent.json()
claves = list(personaje.keys())
valores = list(personaje.values())

def estaVivo(personaje):
    if personaje["status"].lower() == "dead":
        return "muerto"
    elif personaje["status"].lower() == "unknown":
        return "desconocido"
    return "vivo"

def especie(personaje):
    return personaje["species"]

def genero(personaje):
    return personaje["gender"]

def origen(personaje):
    return personaje["origin"]["name"]

def localizacon(personaje):
    return personaje["location"]["name"]

def imagen(personaje):
    return personaje["image"]

print(claves)
print(valores)

nombre = personaje["name"].lower().capitalize()
print(f"{nombre}")
continuar = True
cont = 1
while continuar:
    print("Adivina el nombre del personaje (tienes tres intentos)")
    intento = input(f"Intento {cont}:\n").lower().capitalize()
    if intento == nombre:
        print("¡Enhorabuena!")
        continuar = False
    else:
        if cont == 1:
            print(f"El personaje está: {estaVivo(personaje)}")
            print(f"La especie del personaje es: {especie(personaje)}")
            print(f"El género del personaje es: {genero(personaje)}")
        elif cont == 2:
            print(f"El lugar de origen del personaje es: {origen(personaje)}")
            print(f"La localización del personaje es: {localizacon(personaje)}")
            print(f"Aquí tienes una imagen del personaje: {imagen(personaje)}")
        else:
            print(f"Has perdido.\nEl nombre es: {personaje['name']}")
            continuar = False
        cont+=1
