#!/usr/bin/env python3
"""Test client for Simple API server"""

import requests

url = "http://localhost:8080/"

try:
    response = requests.get(url)
    print(f"Status: {response.status_code}")
    print(f"Content: {response.text}")
except requests.exceptions.RequestException as e:
    print(f"Erreur de connexion : {e}")

