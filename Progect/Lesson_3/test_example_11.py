import pytest
import requests


class TestCookie:
    def test_cookie(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        cookie = dict(response.cookies)
        print(cookie['HomeWork'])
        assert cookie['HomeWork'] == "hw_value", "The cookie parameter is not correct"

#  pytest -s Lesson_3/test_example_11.py -k "test_cookie"
