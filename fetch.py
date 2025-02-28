def fetch_pokemon_data(pokemon_identifier):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_identifier}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None