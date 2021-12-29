import pytest
import requests
import random
import string
from lib.base_case import BaseCase
from lib.assertions import Assertions
from datetime import datetime

heads = [{'password': '123', 'username': 'learnqa', 'firstName': 'larnqa', 'lastName': 'lernqa'},
         {'password': '123', 'username': 'learnqa', 'firstName': 'larnqa', 'email': 'vinkot@example.com'},
         {'password': '123', 'firstName': 'larnqa', 'lastName': 'lernqa', 'email': 'vinkot@example.com'},
         {'username': 'learnqa', 'firstName': 'larnqa', 'lastName': 'lernqa', 'email': 'vinkot@example.com'},
         {'password': '123', 'username': 'learnqa', 'lastName': 'lernqa', 'email': 'vinkot@example.com'}
         ]


# ['password', 'username', 'firstName', 'lastName', 'email']
class TestUserRegister(BaseCase):

    def setup(self):
        base_part = "learnqa"
        domain = "example.com"
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        self.email = f"{base_part}{random_part}{domain}"
        # создаем строку > 250 символов
        letters = string.ascii_lowercase
        self.firstName = ''.join(random.choice(letters) for i in range(251))

    def test_create_user_successfully(self):
        data_for_user = {
            'res_1': {'password': '123', 'username': 'learnqa', 'firstName': 'larnqa', 'lastName': 'lernqa',
                      'email': self.email},
            'res_2': {'password': '123', 'username': self.firstName, 'firstName': 'larnqa', 'lastName': 'l',
                      'email': 'vin@example.com'},
            'res_3': {'password': '123', 'username': 'l', 'firstName': 'larnqa', 'lastName': 'lernqaemail',
                      'email': 'vinkot@example.com'}
        }

        for key, value in data_for_user.items():
            response = requests.post("https://playground.learnqa.ru/api/user/", data=value)

            Assertions.assert_code_status(response, 400)
            if key == 'res_1':
                assert response.content.decode("utf-8") == f"The following required params are missed: email"
            if key == 'res_2':
                assert response.content.decode("utf-8") == f"The following required params are missed: email"
            if key == 'res_3':
                assert response.content.decode("utf-8") == f"The value of 'username' field is too short"

    @pytest.mark.parametrize("head", heads)
    def test_create_user_successfully_without_one_parameter(self, head):
        response1 = requests.post("https://playground.learnqa.ru/api/user/", data=head)
        Assertions.assert_code_status(response1, 400)
        expected_fields = ["username", "email", "firstName", "lastName", "password"]
        for f in expected_fields:
            if f not in head:
                assert response1.content.decode(
                    "utf-8") == f"The following required params are missed: {f}"

        # Assertions.assert_json_has_not_keys(response1, expected_fields)
        # print(response1.text)
        # print(response1.json())

# pytest -s tests/test_user_register_ex_15.py -k test_create_user_successfully
# pytest -s tests/test_user_register_ex_15.py -k test_create_user_successfully_without_one_parameter
