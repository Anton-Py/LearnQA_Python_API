import json
import requests

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
print(response.text)
print(response.status_code)


