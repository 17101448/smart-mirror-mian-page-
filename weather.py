import socket
import requests 
ip_address = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_address.connect(("8.8.8.8", 80))


response = requests.get(url = "https://api.ip2location.com/v2/?ip="+ip_address.getsockname()[0]+"&key=59LQZ8YIAH&package=WS25")

data = response.json()

data["latitude"]
data["longitude"]
data["city_name"]


print(data)