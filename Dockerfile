FROM python
WORKDIR /test_project/
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV ENV=dev
CMD python -m pytest -s --alluredir=test_results/ /test_project/tests/

# Создание образа docker build -t pytest_runner
# docker run --rm --mount type=bind, src=C:\LearnQA_PythonAPI>, target=/test_project/ pytest_runner

#!!!! Запуск docker-compose:  docker-compose up --build
