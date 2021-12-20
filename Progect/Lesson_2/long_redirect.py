import json
import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
print(response.history)
for f in response.history:
    print(f.url)

final_response = response
print(final_response.url)

