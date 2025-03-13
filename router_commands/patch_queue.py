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

url = f"{host}rest/queue/simple/*92"

headers = {
        "Content-Type": "application/json"
        }

data = {
        "name":"Alex_api",
        "target":"192.168.10.14",
        "max-limit":"14M/14M",
        }

response = requests.put(
        url,
        json=data,
        auth=HTTPBasicAuth(username, password),
        headers=headers,
        verify=False
        )
print(response.json())

