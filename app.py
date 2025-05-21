from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get("https://www.fruityvice.com/api/fruit/all")
data = response.json()


fruit_list = []

for fruit in fruit_list:
   
    
    fruit_list.append({
        'name': fruit['name'],
        'id': id,
        
    })
    print(fruit_list)
@app.route("/")
def index():
    # Get the leagues from the API
    fruit = requests.get("https://www.fruityvice.com/api/fruit/all")
    data = response.json()
    fruit_list = data['data']  # The correct key is 'data', not 'results'
    print(data)

    music = []

    for fruit in fruit_list:
        url = fruit['slug']  # 'slug' usually contains a unique ID or path
        id = url
        
        fruit.append({
            'name': fruit['name'],
            'id': id,
            
        })

    return render_template("index.html", fruit=fruit)



    

    
    
    