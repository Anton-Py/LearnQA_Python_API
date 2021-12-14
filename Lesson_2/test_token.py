import json
import requests
import time

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
token_for_response = json.loads(response.text)
print(response.text)

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job",
                        params={"token": token_for_response["token"]})
print(response.text)

time.sleep(token_for_response["seconds"])
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job",
                        params={"token": token_for_response["token"]})
print(response.text)
