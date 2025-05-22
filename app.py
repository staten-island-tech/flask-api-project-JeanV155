


    

    
    
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
            'name': fruit.get('name'),
            'id': fruit.get('id')
        })

    return render_template("index.html", fruits=fruit_list)

if __name__ == "__main__":
    app.run(debug=True)
