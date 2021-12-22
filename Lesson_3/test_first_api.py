import pytest
import requests
import json

class TestFirstAPI:
    names = [
        ("Vitalii"),
        ("Arseniy"),
        ("")
    ]
    @pytest.mark.parametrize('name', names)
    def test_hello_call(self, name):
        url = "https://playground.learnqa.ru/api/hello"
        data = {"name": name}

        response = requests.get(url, params=data)
        assert response.status_code == 200, "wrong response code"

        response_dict = response.json()
        # print(response_dict)
        # print(response.text)

        assert "answer" in response_dict, "Therre is no field 'answer' in the response"

        if len(name) == 0:
            expected_respone_text = "Hello, someone"
        else:
            expected_respone_text = f"Hello, {name}"

        actual_response_text = response_dict["answer"]
        assert actual_response_text == expected_respone_text, "Actual text in the response is no correct"


#  pytest -s Lesson_3/test_first_api.py -k "test_hello_call"

