FROM python:3.10.10-slim-bullseye

RUN apt update && apt install -y curl

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt ./

RUN pip3 install --upgrade pip --no-cache-dir && pip3 install -r requirements.txt --no-cache-dir

COPY .env /code/
COPY ./alembic.ini ./
COPY ./migrations ./migrations
COPY ./app ./app

CMD ["alembic", "upgrade", "head"]