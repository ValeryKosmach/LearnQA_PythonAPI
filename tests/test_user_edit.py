from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from random import choice
from string import ascii_letters

class TestUserEdit(BaseCase):
    def test_edit_just_created_user(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data["email"]
        first_name = register_data["firstName"]
        password = register_data["password"]
        user_id = self.get_json_value(response1, "id")

        #LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        #EDIT
        new_name = "Changed Name"

        response3 = MyRequests.put(f"/user/{user_id}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid},
                                 data={"firstName": new_name}
                                 )
        Assertions.assert_code_status(response3, 200)

        #GET
        response4 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_json_value_by_name(
            response4,
            "firstName",
            new_name,
            "Wrong name of the user after edit"
        )

    def setup(self):
        # Register user 1
        first_user_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user", data=first_user_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        self.email = first_user_data["email"]
        self.first_name = first_user_data["firstName"]
        self.password = first_user_data["password"]
        self.user_id = self.get_json_value(response1, "id")
        self.login_data = {
            'email': self.email,
            'password': self.password
        }

        response2 = MyRequests.post("/user/login", data=self.login_data)

        self.auth_sid = self.get_cookie(response2, "auth_sid")
        self.token = self.get_header(response2, "x-csrf-token")

    def test_edit_unauthorized_user(self):
        new_name = "Changed Name Again"
        response = MyRequests.put(f"/user/{self.user_id}",
                                  data={"firstName": new_name}
                                  )

        Assertions.assert_code_status(response, 400)
        Assertions.assert_response_content(response, "Auth token not supplied")

    def test_edit_one_user_by_another(self):
        # Register user 2
        second_user_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user", data=second_user_data)
        second_user_id = self.get_json_value(response1, "id")
        second_username = second_user_data["username"]

        # Edit SECOND user by FIRST user
        new_name = "Second User Valery"

        response2 = MyRequests.put(f"/user/{second_user_id}",
                                   headers={"x-csrf-token": self.token},
                                   cookies={"auth_sid": self.auth_sid},
                                   data={"username": new_name}
                                   )
        Assertions.assert_code_status(response2, 200)

        # Check that name edition failed
        response3 = MyRequests.get(
            f"/user/{second_user_id}",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
        )

        Assertions.assert_json_value_by_name(
            response3,
            "username",
            second_username,
            "Oops!Username was edit by first user!"
        )

    def test_edit_user_with_incorrect_email(self):
        incorrect_email = "example.com"
        response = MyRequests.put(f"/user/{self.user_id}",
                                  headers={"x-csrf-token": self.token},
                                  cookies={"auth_sid": self.auth_sid},
                                  data={"email": incorrect_email}
                                  )
        Assertions.assert_code_status(response, 400)
        Assertions.assert_response_content(response, "Invalid email format")

    def test_edit_user_firstname_short(self):
        new_first_name = ''.join(choice(ascii_letters) for i in range(1))
        response = MyRequests.put(f"/user/{self.user_id}",
                                  headers={"x-csrf-token": self.token},
                                  cookies={"auth_sid": self.auth_sid},
                                  data={"firstName": new_first_name}
                                  )

        Assertions.assert_code_status(response, 400)
        Assertions.assert_json_value_by_name(
            response,
            "error",
            "Too short value for field firstName",
            "Oops!Username was edit!"
        )