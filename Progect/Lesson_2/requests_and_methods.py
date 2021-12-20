import json
import requests

API_URL = "https://playground.learnqa.ru/ajax/api/compare_query_type"
metods = ['POST', 'GET', 'PUT', 'DELETE']
request_body = {"method": "methodName"}
types_requests = [requests.post, requests.get, requests.put, requests.delete]

for type in types_requests:
    for metod in metods:
        request_body["method"] = metod
        if type == requests.get:
            response = type(API_URL, params=request_body)
        else:
            response = type(API_URL, data=request_body)
        print(type)
        print(metod, 'Ответ: ', response.text)
    print()