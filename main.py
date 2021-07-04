import requests
from json.decoder import JSONDecodeError

print("Hello from Valery")
response1 = requests.get("https://playground.learnqa.ru/api/hello")
print(response1.text)


# передача параметров
payload = {"name": "User1"}
response2 = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
print(response2.text)

# + парсинг, параметры заданы сразу
response3 = requests.get("https://playground.learnqa.ru/api/hello", params={"name": "User"})
parsed_response_text = response3.json()
print(parsed_response_text["answer"])

# защита если не парсится JSON
response4 = requests.get("https://playground.learnqa.ru/api/get_text")
print(response4.text)

try:
    parsed_response_text = response4.json()
    print(parsed_response_text)
except JSONDecodeError:
    print("response is not JSON format")

#password = [123]

# удалить дубликаты
#new_data = list(set(password))
#print(new_data)
#for i in range(len(new_data)):
session = requests.Session()
authentication = session.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data={"login":"super_admin", "password":"000000"})
print(authentication.text)
    get_cookie = session.cookies.get_dict()["auth_cookie"]
    auth_cookie = requests.get("https://playground.learnqa.ru/ajax/api/check_auth_cookie")
    #if auth_cookie.text != "You are NOT authorized":
    print(auth_cookie.text)