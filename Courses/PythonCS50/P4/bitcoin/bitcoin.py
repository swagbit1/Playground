# rest.coincap.io/v3/assets/bitcoin?apiKey=522ab6aa2b307a64da9e92fa1a31e7b58362b73842c6ef92030eb6e405b867c4

import sys
import requests


if len(sys.argv) < 2:
    sys.exit("Invalid prompt")
try:
    n = float(sys.argv[1])
    api = requests.get('https://rest.coincap.io/v3/assets/bitcoin?apiKey=522ab6aa2b307a64da9e92fa1a31e7b58362b73842c6ef92030eb6e405b867c4')
    cost = float(api.json()["data"]["priceUsd"])
    print(f"{(n * cost):,.4f}")
except (ValueError, TypeError):
    sys.exit("Invalid prompt")
