import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests
import allure


@allure.severity("blocker")
@allure.epic("Edit cases")
class TestUser(BaseCase):
    @allure.description("This test get user not auth")
    def test_get_user_details_not_auth(self):
        response = MyRequests.get("/user/2")

        Assertions.assert_json_has_key(response, "username")
        Assertions.assert_json_value_has_not_key(response, "email")
        Assertions.assert_json_value_has_not_key(response, "firstName")
        Assertions.assert_json_value_has_not_key(response, "lastName")

        # print(response.content)
        # print(response.text)
        # print(response.json())

    @allure.description("This test details auth as same use")
    def test_get_user_details_auth_as_same_user(self):
        data = {'email': 'vinkotov@example.com',
                'password': '1234'
                }

        response1 = MyRequests.post("/user/login", data=data)

        # print(response1.content)
        # print(response1.text)
        # print(response1.json())

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        response2 = MyRequests.get(
            f"/user/{user_id_from_auth_method}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        expected_fields = ["username", "email", "firstName", "lastName"]
        Assertions.assert_json_has_keys(response2, expected_fields)

        # Assertions.assert_json_has_key(response2, "username")
        # Assertions.assert_json_has_key(response2, "email")
        # Assertions.assert_json_has_key(response2, "firstname")
        # Assertions.assert_json_has_key(response2, "lastname")

        # pytest -s tests/test_user_get.py -k test_get_user_details_not_auth
        # pytest -s tests/test_user_get.py -k test_get_user_details_auth_as_same_user

        # pytest --alluredir=test_results/ tests/test_user_get.py
        # allure serve test_results/
