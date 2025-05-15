FROM python:3.10.4-alpine3.16

ENV pythonunbuffered 1
ENV pythondontwritebytecode 1

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt 
# Optimización de orden de instalación para maximizar la caché de Docker

COPY . /app

CMD ["sh", "/app/entrypoint.sh"]