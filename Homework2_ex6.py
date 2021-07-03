import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")
all_responses = response.history
print("Number of all responses: " + str(len(all_responses)))

first_response = response.history[0]
second_response = response.history[1]
last_response = response

print(first_response.url)
print(second_response.url)
print(last_response.url)
