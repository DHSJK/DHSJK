import requests # llamada a la POCKEAPI

URL = "https://pokeapi.co/api/v2/pokemon/"

pokemon = input("Escribe el pokemon: ")

respuesta = requests.get(URL + pokemon)

datos = respuesta.json() #traer en formato json

print(datos)