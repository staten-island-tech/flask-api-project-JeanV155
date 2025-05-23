
from flask import Flask, render_template
import requests

app = Flask(__name__)

from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    # Get fruit data from API
    response = requests.get("https://www.fruityvice.com/api/fruit/all")
    fruit_data = response.json()  # This returns a list

    # Create a list of fruits with desired fields
    fruit_list = []
    for fruit in fruit_data:
        fruit_list.append({
            'name': fruit["name"],
            'id': fruit["id"]
        }) 

    return render_template("index.html", fruits=fruit_list)

@app.route("/fruit/<int:id>")
def fruit_detail(id):
    # Get detailed info for a specific fruit using its id
    response = requests.get(f"https://www.fruityvice.com/api/fruit/{id}")
    
    if response.status_code != 200:
        return "Fruit not found", 404

    data = response.json()

    # Extract details
    name = data.get('name')
    family = data.get('family')
    genus = data.get('genus')
    order = data.get('order')
    nutritions = data.get('nutritions', {}) #look thgro8gh janet side quest for lamnda and map

    return render_template("fruit_detail.html",  
)
