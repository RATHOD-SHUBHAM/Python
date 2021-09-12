FROM python:3.8
WORKDIR /fastapi-app

COPY requirements.txt .

RUN pip install -r requirements.txt 

COPY ./app ./appdocker

CMD ["python", "./appdocker/main.py"]
