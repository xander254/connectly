#!/usr/bin/python3
"""
A script to add a queue to a mikrotik router using the rest api in router os 7 and above
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

url = f"{host}rest/queue/simple/add"

headers = {
        "Content-Type": "application/json"
        }

data = {
        "name":"Alex_api",
        "target":"192.168.10.14/32",
        "max-limit":"4M/4M",
        }

response = requests.post(
        url,
        json=data,
        auth=HTTPBasicAuth(username, password),
        headers=headers,
        verify=False
        )
print(response.json())
print(response.status_code)
print(response.text)

