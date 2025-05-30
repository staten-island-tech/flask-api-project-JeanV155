
from flask import Flask, render_template, request, redirect, url_for, abort
import requests

app = Flask(__name__)

@app.route("/")
def index():
    response = requests.get("https://www.fruityvice.com/api/fruit/all")
    fruit_data = response.json()

    # Sort fruits by name alphabetically
    fruit_data.sort(key=lambda x: x["name"].lower())

    fruit_list = []
    for fruit in fruit_data:
        fruit_list.append({
            'name': fruit["name"],
            'id': fruit["id"]
        })

    return render_template("index.html", fruits=fruit_list)

@app.route("/fruit/<int:id>")
def fruit_detail(id):
    try:
        response = requests.get(f"https://www.fruityvice.com/api/fruit/{id}")
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException:
        abort(404)

    # Extract fruit details
    name = data.get('name', 'Unknown').capitalize()
    family = data.get('family', 'Unknown')
    genus = data.get('genus', 'Unknown')
    order = data.get('order', 'Unknown')

    # Your original nutrition extraction loop
    fruit_names = []
    fruit_value = []

    for key, values in data.get('nutritions', {}).items():
        fruit_names.append(key)
        fruit_value.append(values)

    nutrition = zip(fruit_names, fruit_value)

    return render_template("fruit_detail.html", fruit={
        'name': name,
        'family': family,
        'genus': genus,
        'order': order,
        'nutrition': nutrition
    })

if __name__ == "__main__":
    app.run(debug=True)
