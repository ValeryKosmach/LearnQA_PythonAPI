import os
# export MY_VAR="123" для linux, MacOS
#set MY_VAR="123" - для WIN,

class Environment:
    DEV = 'dev'
    PROD = 'prod'

    URLS = {
        DEV: 'https://playground.learnqa.ru/api_dev',
        PROD: 'https://playground.learnqa.ru/api'
    }

    #метод, который читает значение env
    def __init__(self):
        try:
            self.env = os.environ['ENV']
        except KeyError:
            self.env = self.DEV

    def get_base_url(self):
        if self.env in self.URLS:
            return self.URLS[self.env]
        else:
            raise Exception(f"Unknown value of ENV variable {self.env}")

ENV_OBJECT = Environment()


# Запуск тестов меняя env через terminal
# 1. Задать env, в моем случае: set ENV=prod
# 2. Проверить какой env сейчас: echo %ENV%
# 3. Запустить все тесты: python -m pytest tests/