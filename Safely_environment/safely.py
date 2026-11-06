import httpx
from flask import Flask, render_template

app = Flask(__name__, template_folder='../Safely_front')

query_params = {
    "latitude": "52.52,48.85",
    "longitude": "13.41,2.35",
}

res = httpx.get("https://api.open-meteo.com/v1/meteofrance", params=query_params)
print(res.json())

@app.route("/")
def homepage():
    return render_template(
        'page1.html', 
        title='Home Page', 
        user_name='Alex', 
        weather_data=res.json()
    )
 

if __name__ == '__main__':
    app.run(debug=True)
