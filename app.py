
from flask import Flask, render_template, request, redirect, url_for, abort
import requests

app = Flask(__name__)

@app.route("/")
def index():
    search_query = request.args.get('search', '').strip().lower()
    response = requests.get("https://www.fruityvice.com/api/fruit/all")
    fruit_data = response.json()

    # Sort fruits by name alphabetically
    fruit_data.sort(key=lambda x: x["name"].lower())

    fruit_list = []
    for fruit in fruit_data:
        name = fruit["name"]
        fruit_id = str(fruit["id"])

        # Include fruit if search_query is empty, matches name, or matches ID
        if not search_query or search_query in name.lower() or search_query == fruit_id:
            fruit_list.append({
                'name': name,
                'id': fruit["id"]
            })

   
    if search_query and not fruit_list:
        abort(404)

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

    # Extract nutrition info
    fruit_names = []
    fruit_value = []
    for key, values in data.get('nutritions', {}).items():
        fruit_names.append(key)
        fruit_value.append(values)

    nutrition = zip(fruit_names, fruit_value)

    return render_template("fruit.html", fruit={
        'name': name,
        'family': family,
        'genus': genus,
        'order': order,
        'nutrition': nutrition
    })

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)
