FROM python:3.10

WORKDIR /app
COPY requirements.txt .

RUN pip install --default-timeout=200 -r requirements.txt


COPY . .

EXPOSE 8081

