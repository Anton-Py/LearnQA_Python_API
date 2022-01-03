import requests
import time
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserEdit(BaseCase):
    def test_edit_just_created_user(self):
        # REGISTER USER 1
        register_data_1 = self.prepare_registration_data()
        response1 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data_1)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email_1 = register_data_1['email']
        first_name_1 = register_data_1['firstName']
        password_1 = register_data_1['password']
        user_id_first = self.get_json_value(response1, "id")
        time.sleep(1)

        # REGISTER USER 2
        register_data_2 = self.prepare_registration_data()
        response2 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data_2)

        Assertions.assert_code_status(response2, 200)
        Assertions.assert_json_has_key(response2, "id")

        email_2 = register_data_2['email']
        first_name_2 = register_data_2['firstName']
        password_2 = register_data_2['password']
        user_id_second = self.get_json_value(response2, "id")

        # EDITING UNDER AN UNAUTHORIZED USER
        new_name = "New Name"
        response_unauthorized_user = requests.put(
            f"https://playground.learnqa.ru/api/user/{user_id_second}",
            data={"firstName": new_name}
        )

        Assertions.assert_code_status(response_unauthorized_user, 400)
        assert response_unauthorized_user.content.decode("utf-8") == "Auth token not supplied"

        # LOGIN USER 1
        login_data = {
            'email': email_1,
            'password': password_1
        }
        response3 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)

        auth_sid_1 = self.get_cookie(response3, "auth_sid")
        token_1 = self.get_header(response3, "x-csrf-token")

        # EDIT USER FIRST TO SECOND(UNAUTHORIZED USER)
        new_name = "Test for Test"

        response5 = requests.put(
            f"https://playground.learnqa.ru/api/user/{user_id_second}",
            headers={"x-csrf-token": token_1},
            cookies={"auth_sid": auth_sid_1},
            data={"firstName": new_name}
        )

        Assertions.assert_code_status(response5, 200)

        # GET
        response6 = requests.get(f"https://playground.learnqa.ru/api/user/{user_id_second}")
        Assertions.assert_code_status(response6, 200)
        Assertions.assert_json_has_key(response6, "username")

        # EDIT USER EMAIL
        email = "movmail.ru"
        response7 = requests.put(
            f"https://playground.learnqa.ru/api/user/{user_id_first}",
            headers={"x-csrf-token": token_1},
            cookies={"auth_sid": auth_sid_1},
            data={"email": email}
        )

        Assertions.assert_code_status(response7, 400)
        assert response7.content.decode("utf-8") == "Invalid email format"

        # EDIT USER firstName
        firstName = "m"
        response8 = requests.put(
            f"https://playground.learnqa.ru/api/user/{user_id_first}",
            headers={"x-csrf-token": token_1},
            cookies={"auth_sid": auth_sid_1},
            data={"firstName": firstName}
        )
        print(response8.content)
        Assertions.assert_code_status(response8, 400)
        Assertions.assert_json_has_key_for_error(response8, "error", "Too short value for field firstName")


    # pytest test_user_edit_ex_17.py --disable-warnings --tb=short -s