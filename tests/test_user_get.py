import allure
from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions

@allure.epic("User get")
class TestUserGet(BaseCase):
    @allure.description("Attempts to get user details by unauthorized user")
    def test_get_user_details_not_auth(self):
        response = MyRequests.get("/user/2")

        Assertions.assert_json_has_key(response, "username")
        Assertions.assert_json_has_not_keys(response, "email")
        Assertions.assert_json_has_not_keys(response, "firstName")
        Assertions.assert_json_has_not_keys(response, "lastName")

    @allure.description("Attempts to get user details")
    def test_get_user_details_auth_as_same_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = MyRequests.post("/user/login", data=data)

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

    @allure.description("Preconditions. Auth of first user")
    def setup(self):
        # Auth of first user
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = MyRequests.post("/user/login", data=data)

        self.auth_sid = self.get_cookie(response1, "auth_sid")
        self.token = self.get_header(response1, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(response1, "user_id")

    @allure.description("Attempts to get one user details by another user")
    def test_authorized_user_gets_user_details_another_user(self):
        response = MyRequests.get(
            "/user/1",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
        )

        Assertions.assert_json_has_key(response, "username")
        Assertions.assert_json_has_not_keys(response, "email")
        Assertions.assert_json_has_not_keys(response, "firstName")
        Assertions.assert_json_has_not_keys(response, "lastName")
