import requests

class TestHeader:
    def test_get_header(self):
        url = "https://playground.learnqa.ru/api/homework_header"
        response = requests.get(url)
        header = response.headers
        print(header)

        assert response.status_code == 200, "Wrong response code"
        assert "x-secret-homework-header" in header, "Header is not correct"
        assert header["x-secret-homework-header"] == "Some secret value", "Header value not found"
