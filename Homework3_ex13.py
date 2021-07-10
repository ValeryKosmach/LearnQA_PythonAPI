import requests
import pytest

class TestUserAgent:
    data = [
        (
            {
                "user_agent": "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
                "expected_platform": "Mobile",
                "expected_browser": "No",
                "expected_device": "Android"
            }
        ),
        (
            {
                "user_agent": "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1",
                "expected_platform": "Mobile",
                "expected_browser": "Chrome",
                "expected_device": "iOS"
            }
        ),
        (
            {
                "user_agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
                "expected_platform": "Googlebot",
                "expected_browser": "Unknown",
                "expected_device": "Unknown"
            }
        ),
        (
            {
                "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0",
                "expected_platform": "Web",
                "expected_browser": "Chrome",
                "expected_device": "No"
            }
        ),
        (
            {
                "user_agent": "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
                "expected_platform": "Mobile",
                "expected_browser": "No",
                "expected_device": "iPhone"
            }
        )
    ]

    @pytest.mark.parametrize('data', data)
    def test_user_agent_one(self, data):
        user_agent = data['user_agent']
        expected_platform = data['expected_platform']
        expected_browser = data['expected_browser']
        expected_device = data['expected_device']

        response = requests.get(
            "https://playground.learnqa.ru/ajax/api/user_agent_check",
            headers={"User-Agent": user_agent}
        )

        answer = response.json()
        actual_platform = answer["platform"]
        actual_browser = answer["browser"]
        actual_device = answer["device"]

        assert expected_platform == actual_platform, f"Platform is not correct. Expected: {expected_platform}. Actual: {actual_platform}"
        assert expected_browser == actual_browser, f"Browser is not correct. Expected: {expected_platform}. Actual: {actual_platform}"
        assert expected_device == actual_device, f"Device is not correct. Expected: {expected_platform}. Actual: {actual_platform}"

