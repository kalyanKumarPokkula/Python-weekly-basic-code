import requests
import json

request = requests.get("http://localhost:3001/api/v1/anime/64f15f439603a34dd0c90cdf")
print(json.dumps(request.json(), indent=2))
