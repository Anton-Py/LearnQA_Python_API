from requests import Response
import json


class Assertions:

    @staticmethod
    def assert_code_status(response: Response, expected_status_code):
        assert response.status_code == expected_status_code,\
            f"Unexpected status code! Expeted: {expected_status_code}. Actual: {response.status_code}"

    # @staticmethod
    # def assert_json_has_not_keys(response: Response, names: list):
    #
    #     for f in names:
    #         if f not in head:
    #             assert response.content.decode(
    #                 "utf-8") == f"The following required params are missed: {f}"


