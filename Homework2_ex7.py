import requests

url_without_parameters = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print("Запрос без параметров: " + url_without_parameters.text, url_without_parameters.status_code)

url_options = requests.options("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method":"OPTIONS"})
print("Запрос не из ссписка: " + url_options.text, url_options.status_code)

correct_url_get = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method":"GET"})
print("Запрос с правильным значением method: " + correct_url_get.text, correct_url_get.status_code)

methods = [requests.get, requests.post, requests.put, requests.delete, requests.head]
params = "GET", "POST", "PUT", "DELETE", "HEAD"
for method in methods:
    for param in params:
        if method == requests.get:
            response = method("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": param})
            print(f"{response.text}, {response.status_code} from {method} with param {param}")
        else:
            response = method("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": param})
            print(f"{response.text}, {response.status_code} from {method} with param {param}")

# вывел отдельно, чтобы проверить дополнительно (на всякий случай)
not_correct_method = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method":"GET"})
print("Запрос с Не правильным значением method: " + not_correct_method.text, not_correct_method.status_code)



