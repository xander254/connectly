import routeros_api
from os import getenv

connection = routeros_api.RouterOsApiPool(
        host= getenv('rhost'),
        username= getenv('rusername'),
        password= getenv('rpassword'),
        plaintext_login=True
)
api = connection.get_api()

ip_addresses = api.get_resource('ip/address').get()
for ip in ip_addresses:
    print(ip)

connection.disconnect()
