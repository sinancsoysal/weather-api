from flask import Flask, jsonify, render_template, request
import requests
from flask_restful import Resource,Api
app=Flask(__name__)
api=Api(app)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather',methods=['POST'], endpoint='weather')
def result():
    city_name = request.form['city']
    geocoding = "https://geocoding-api.open-meteo.com/v1/search?name={}&count=10&language=en&format=json"
    weather = "https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&hourly=temperature_2m"
    try:
        coordinations = requests.get(geocoding.format(city_name)).json()
        lat = coordinations["results"][0]["latitude"]
        long = coordinations["results"][0]["longitude"]
        result = requests.get(weather.format(lat, long)).json()
        return render_template('results.html', result=result['hourly']['temperature_2m'][0], city=city_name)
    except:
        return render_template('results.html', result=None)

if __name__ == '__main__':
    app.run()
