import requests

def fetch_character():
    response = requests.get("https://rickandmortyapi.com/api/character/2")
    if response.status_code == 200:
        data = response.json()
        name = data.get("name")
        status = data.get("status")
        print(f"Nombre: {name}")
        print(f"Estado: {status}")
    else:
        print("Error al obtener los datos.")

fetch_character()