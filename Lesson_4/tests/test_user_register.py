import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


class TestUserRegister(BaseCase):
    def test_create_user_successfully(self):
        data = self.prepare_registration_data()

        response = MyRequests.post("/user/", data=data)

        # assert response.status_code == 200, f"Unexpected status code {response.status_code}"
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")
        # print(response.content)
        # print(response.text)
        # print(response.json())

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 400)

        assert response.content.decode(
            "utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content.decode('utf-8')}"
        # print(response.status_code)
        # print(response.content)

# pytest -s tests/test_user_register.py -k test_create_user_successfully
# pytest -s tests/test_user_register.py
