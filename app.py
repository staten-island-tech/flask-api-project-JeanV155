from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get("https://www.fruityvice.com/api/fruit/all")
data = response.json()
music_list = data['data']  # The correct key is 'data', not 'results'
print(data)

leagues = []

for music in music_list:
    url = music['slug']  # 'slug' usually contains a unique ID or path
    id = url
    
    music.append({
        'name': league['name'],
        'id': id,
        
    })

@app.route("/")
def index():
    # Get the leagues from the API
    fruit = requests.get("https://www.fruityvice.com/api/fruit/all")
    data = response.json()
    fruit_list = data['data']  # The correct key is 'data', not 'results'
    print(data)

    music = []

    for music in music_list:
        url = fruit['slug']  # 'slug' usually contains a unique ID or path
        id = url
        
        leagues.append({
            'name': league['name'],
            'id': id,
            
        })

    return render_template("index.html", leagues=leagues)



    

    
    
    