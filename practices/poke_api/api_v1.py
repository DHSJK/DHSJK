#version del codigo: 1.0
# Descripción: Este script utiliza la API de Pokémon para obtener y mostrar información detallada sobre un Pokémon específico.
import requests

def imprimir_datos_pokemon(pokemon_nombre):
    URL = "https://pokeapi.co/api/v2/pokemon/"
    respuesta = requests.get(URL + pokemon_nombre.lower())
    
    if respuesta.status_code != 200:
        print(f"No se encontró el Pokémon {pokemon_nombre}")
        return
    
    datos = respuesta.json()
    
    # Encabezado con nombre del Pokémon y ID
    print(f"\n{'='*50}")
    print(f"{datos['name'].capitalize()} (ID: {datos['id']})")
    print(f"{'='*50}")
    
    # Información básica
    print("\n[INFORMACIÓN BÁSICA]")
    print(f"Altura: {datos['height']/10:.1f} m")  # Convertir a metros
    print(f"Peso: {datos['weight']/10:.1f} kg")   # Convertir a kg
    print(f"Especie: {datos['species']['name'].capitalize()}")
    
    # Tipos
    print("\n[TIPOS]")
    for tipo in datos["types"]:
        print(f"- {tipo['type']['name'].capitalize()}")
    
    # Habilidades
    print("\n[HABILIDADES]")
    for habilidad in datos["abilities"]:
        is_hidden = "(Oculta)" if habilidad['is_hidden'] else ""
        print(f"- {habilidad['ability']['name'].capitalize()} {is_hidden}")
    
    # Estadísticas
    print("\n[ESTADÍSTICAS]")
    for stat in datos["stats"]:
        nombre_stat = stat['stat']['name'].replace('-', ' ').capitalize()
        print(f"{nombre_stat}: {stat['base_stat']}")
    
    # Movimientos
    print("\n[MOVIMIENTOS]")
    movimientos = [move['move']['name'].capitalize() for move in datos['moves']]
    # Mostrar 5 movimientos por línea para mejor visualización
    for i in range(0, len(movimientos), 5):
        print(", ".join(movimientos[i:i+5]))
    
    print(f"\n{'='*50}\n")

# Ejemplo de uso
pokemon = input("Escribe el nombre del Pokémon: ")
imprimir_datos_pokemon(pokemon)