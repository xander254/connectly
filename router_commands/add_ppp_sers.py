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

url = f"{host}rest/ppp/active"

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
print(resources)
