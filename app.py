from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    # Get the first 150 Pokémon from the API
    
    
    