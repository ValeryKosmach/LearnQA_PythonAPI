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