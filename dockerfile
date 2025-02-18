FROM python:3.10.4-alpine3.16

ENV pythonunbuffered 1
ENV pythondontwritebytecode 1

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt && \
    pip install --upgrade pip && \
    pip install whitenoise

COPY ./entrypoint.sh /app/entrypoint.sh

CMD ["sh", "/app/entrypoint.sh"]