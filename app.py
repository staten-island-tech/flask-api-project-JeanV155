from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    # Get the first 150 Pokémon from the API
    response = requests.get("https://api-football-standings.azharimm.site/leagues")
    data = response.json()
    pokemon_list = data['results']
    
    # Create a list to hold Pokémon details
    pokemons = []
    
    for pokemon in pokemon_list:
        # Each Pokémon URL looks like "https://pokeapi.co/api/v2/pokemon/1/"
        url = pokemon['url']
        parts = url.strip("/").split("/")
        id = parts[-1]  # The last part is the Pokémon's ID
        
        # Create an image URL using the Pokémon's ID
        image_url = f"https://api-football-standings.azharimm.site/leagues/eng.1"
        
        pokemons.append({
            'name': pokemon['name'].capitalize(),
            'id': id,
            'image': image_url
        })
    
    # Send the Pokémon list to the index.html page
    return render_template("index.html", pokemons=pokemons)
    
    
    
    
    