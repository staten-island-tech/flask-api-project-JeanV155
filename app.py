from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    # Get the leagues from the API
    response = requests.get("https://api-football-standings.azharimm.site/leagues")
    data = response.json()
    league_list = data['data']  # The correct key is 'data', not 'results'
    print(data)

    leagues = []

    for league in league_list:
        url = league['slug']  # 'slug' usually contains a unique ID or path
        id = url
        
        leagues.append({
            'name': league['name'],
            'id': id,
            
        })

    return render_template("index.html", leagues=leagues)

if __name__ == '__main__':
    app.run(debug=True)


    

    
    
    