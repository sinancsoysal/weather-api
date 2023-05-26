import requests

url = 'http://localhost:5000/weather' 

city = 'London'  # Replace with the desired city name

data = {'city': city}

response = requests.post(url, data=data)

print(response.json())
