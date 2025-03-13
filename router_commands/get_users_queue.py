#!/usr/bin/python3
"""
A module to quesry a mikrotik router for all active ip addresses on the device
"""

import requests
import json
from requests.auth import HTTPBasicAuth
from os import getenv
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

host = getenv('rhost')
username = getenv('rusername')
password = getenv('rpassword')

queue_id = "*92"
url = f"{host}rest/queue/simple/{queue_id}"

headers = {
        "Content-Type": "application/json"
        }

response = requests.get(
        url,
        auth=HTTPBasicAuth(username, password),
        headers=headers,
        verify=False
        )

print(response.status_code)
resources = response.json()
print("The id {} and name is {}".format(queue_id, resources["target"], resources["name"]))
print("The priority is {} and the speed is {}".format(resources["priority"], resources["max-limit"]))
