import time

import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from datetime import datetime


class TestUser(BaseCase):

    def setup(self):
        self.emails = []
        for f in range(2):
            base_part = "testing"
            domain = "example.com"
            random_part = datetime.now().strftime("%m%d%Y%H%M%S")
            email = f"{base_part}{random_part}@{domain}"
            self.emails.append(email)
            time.sleep(1)

    def test_create_user_successfully(self):
        # create first user
        data_1 = {
            'password': '123',
            'username': 'learntest_1',
            'firstName': 'larnqt',
            'lastName': 'lernqt',
            'email': self.emails[0]
        }
        response_1 = requests.post("https://playground.learnqa.ru/api/user/", data=data_1)
        Assertions.assert_code_status(response_1, 200)
        Assertions.assert_json_has_key(response_1, "id")

        # create second user
        data_2 = {
            'password': '123',
            'username': 'learntest_2',
            'firstName': 'larnqt',
            'lastName': 'lernqt',
            'email': self.emails[1]
        }
        response_2 = requests.post("https://playground.learnqa.ru/api/user/", data=data_2)

        Assertions.assert_code_status(response_2, 200)
        Assertions.assert_json_has_key(response_2, "id")

        # get user details auth as first user
        data_3 = {'email': self.emails[0],
                  'password': '123'
                  }
        response_3 = requests.post("https://playground.learnqa.ru/api/user/login", data=data_3)
        auth_sid = self.get_cookie(response_3, "auth_sid")
        token = self.get_header(response_3, "x-csrf-token")

        # get user details auth as second user
        data_4 = {'email': self.emails[1],
                  'password': '123'
                  }
        response_4 = requests.post("https://playground.learnqa.ru/api/user/login", data=data_4)
        user_id_from_auth_method_2 = self.get_json_value(response_4, "user_id")

        # request with someone else's id
        response_5 = requests.get(f"https://playground.learnqa.ru/api/user/{user_id_from_auth_method_2}",
                                  headers={"x-csrf-token": token},
                                  cookies={"auth_sid": auth_sid}
                                  )

        Assertions.assert_json_has_key(response_5, "username")
        Assertions.assert_json_value_has_not_key(response_5, "email")
        Assertions.assert_json_value_has_not_key(response_5, "firstname")
        Assertions.assert_json_value_has_not_key(response_5, "lastname")
        print(response_5.content)

# pytest -s tests/test_user_get_ex_16.py -k test_create_user_successfully
