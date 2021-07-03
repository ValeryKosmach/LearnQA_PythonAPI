import requests
import time

create_task = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
parsed_response_text = create_task.json()
print(parsed_response_text)
token_value = parsed_response_text["token"]
seconds_value = parsed_response_text["seconds"]

request_with_token = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token_value})
print(request_with_token.text)
time.sleep(seconds_value)
request_task_complete = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token_value})
print(request_task_complete.text)