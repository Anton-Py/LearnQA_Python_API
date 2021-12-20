import pytest
import requests
import json

class TestUserAuth:
    def test_auth_user(self):

        data = {'email': 'vinkotov@example.com',
                'password': '1234'
                }

        response1 = requests.post("https://playground.learnqa.ru/api/hello", data=data)
        print(response1.text)
        assert "auth_sid" in response1.cookies, "There is no auth cookie in the response"
        assert "x-csrf-token" in response1.headers, "There is no CSRF token header in the response"
        assert "user_id" in response1.json(), "There is no user id in the response"



#  pytest -s Lesson_3/test_user_auth.py -k "test_auth_user"

