import time

import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserDelete(BaseCase):
    def test_delete_user(self):
        # LOGIN USER_2
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response = requests.post("https://playground.learnqa.ru/api/user/login", data=data)

        auth_sid = self.get_cookie(response, "auth_sid")
        token = self.get_header(response, "x-csrf-token")
        user_id_2 = self.get_json_value(response, "user_id")

        # DELETE USER_2
        response1 = requests.delete(
            f"https://playground.learnqa.ru/api/user/{user_id_2}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
        )

        Assertions.assert_code_status(response1, 400)
        assert response1.content.decode("utf-8") == "Please, do not delete test users with ID 1, 2, 3, 4 or 5."

        # REGISTER NEW USER_1
        register_data = self.prepare_registration_data()
        response2 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data)

        Assertions.assert_code_status(response2, 200)
        Assertions.assert_json_has_key(response2, "id")

        email_1 = register_data['email']
        first_name_1 = register_data['firstName']
        password_1 = register_data['password']
        user_id_new_1 = self.get_json_value(response2, "id")

        # REGISTER NEW USER_2
        register_data_2 = self.prepare_registration_data()
        response3 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data_2)

        Assertions.assert_code_status(response3, 200)
        Assertions.assert_json_has_key(response3, "id")

        email_2 = register_data_2['email']
        first_name_2 = register_data_2['firstName']
        password_2 = register_data_2['password']
        user_id_second_2 = self.get_json_value(response3, "id")

        # LOGIN NEW USER_1
        login_data_1 = {
            'email': email_1,
            'password': password_1
        }
        response4 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data_1)

        auth_sid_new_user_1 = self.get_cookie(response4, "auth_sid")
        token_new_user_1 = self.get_header(response4, "x-csrf-token")
        user_id_new_user_1 = self.get_json_value(response4, "user_id")

        # DELETE UNDER AN UNAUTHORIZED USER
        response6 = requests.delete(
            f"https://playground.learnqa.ru/api/user/{user_id_second_2}",
            headers={"x-csrf-token": token_new_user_1},
            cookies={"auth_sid": auth_sid_new_user_1},
        )
        Assertions.assert_code_status(response6, 200)

        response9 = requests.get(
            f"https://playground.learnqa.ru/api/user/{user_id_second_2}")
        Assertions.assert_json_has_key(response9, "username")

        # DELETE NEW USER_1
        response7 = requests.delete(
            f"https://playground.learnqa.ru/api/user/{user_id_new_user_1}",
            headers={"x-csrf-token": token_new_user_1},
            cookies={"auth_sid": auth_sid_new_user_1},
        )

        Assertions.assert_code_status(response7, 200)

        # GET NEW USER_1
        response8 = requests.get(
            f"https://playground.learnqa.ru/api/user/{user_id_new_user_1}",
            headers={"x-csrf-token": token_new_user_1},
            cookies={"auth_sid": auth_sid_new_user_1},
        )

        Assertions.assert_code_status(response8, 404)
        assert response8.content.decode("utf-8") == "User not found"
        print(response8.content)


# pytest -s tests/test_user_delete.py --disable-warnings --tb=short
