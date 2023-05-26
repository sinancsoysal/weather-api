from flask import Flask,jsonify,url_for,request
import requests
from flask_restful import Resource,Api
app=Flask(__name__)
api=Api(app)

@app.route('/weather',methods=['POST'])
def result():
    city_name = request.form['city']
    geocoding = "https://geocoding-api.open-meteo.com/v1/search?name={}&count=10&language=en&format=json"
    weather = "https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&hourly=temperature_2m"
    try:
        coordinations = requests.get(geocoding.format(city_name)).json()
        lat = coordinations["results"][0]["latitude"]
        long = coordinations["results"][0]["longitude"]
        result = requests.get(weather.format(lat, long)).json()
        return jsonify(result)
    except:
        return "<h1>Oops city not found. Try larger city name nearby</h1>"

if __name__ == '__main__':
    app.run()
