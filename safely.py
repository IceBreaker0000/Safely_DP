import httpx
from flask import Flask

app = Flask(__name__)

query_params = {
    "latitude": "52.52,48.85",
    "longitude": "13.41,2.35",
}

res = httpx.get("https://api.open-meteo.com/v1/meteofrance", params=query_params)

@app.route("/")
def hello_world():
    return f"<p>{res.json()}</p>"
print(res.json())
