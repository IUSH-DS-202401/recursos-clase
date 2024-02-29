import requests
import json

r = requests.get('https://pokeapi.co/api/v2/pokemon?limit=10', verify=False)

dict_pokemon = r.json()

for pokemon in dict_pokemon['results']:
    url_arr = pokemon['url'].split("/")
    numero = url_arr[-2]
    print("")
    print(f"Numero: {numero}")
    print(f"Nombre: {pokemon['name']}")

pokemon_json = json.dumps(dict_pokemon['results'], indent=2)

with open("pokemon.json","w") as archivo:
    archivo.write(pokemon_json)