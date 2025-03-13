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

url = f"{host}rest/queue/simple/*75"

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
resources = json.dumps(response.json(), sort_keys=True, indent=4)
print(resources)
