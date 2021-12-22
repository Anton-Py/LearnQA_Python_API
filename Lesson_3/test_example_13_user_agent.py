import pytest
import requests
import json





heads = [
    ("Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30", {'platform': 'Mobile', 'browser': 'No', 'device': 'Android'}),
    ("Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1", {'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS'}),
    ("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)", {'platform': 'Googlebot', 'browser': 'Unknown', 'device': 'Unknown'}),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0", {'platform': 'Web', 'browser': 'Chrome', 'device': 'No'}),
    ("Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1", {'platform': 'Mobile', 'browser': 'No', 'device': 'iPhone'}),
]

expect_results = [{'platform': 'Mobile', 'browser': 'No', 'device': 'Android'},
                  {'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS'},
                  {'platform': 'Googlebot', 'browser': 'Unknown', 'device': 'Unknown'},
                  {'platform': 'Web', 'browser': 'Chrome', 'device': 'No'},
                  {'platform': 'Mobile', 'browser': 'No', 'device': 'iPhone'}
                  ]


@pytest.mark.parametrize("head, expec", heads)
class TestUserAgent:
    def test_user_agent(self, head, expec):
        url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
        head = {"User-Agent": head}
        response = requests.get(url, headers=head)
        assert response.status_code == 200, "wrong response code"
        obj = json.loads(response.text)
        for f in expec:
            assert expec[f] in obj[f], f"{expec} this username has a wrong parameter {f}"




#  pytest -s Lesson_3/test_example_13_user_agent.py -k "test_user_agent"