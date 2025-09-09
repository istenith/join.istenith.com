FROM python:3.10

WORKDIR /app
COPY requirements.txt .

RUN pip install --default-timeout=200 -r requirements.txt
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

COPY . .

EXPOSE 8081

