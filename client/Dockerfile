FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir /app

COPY . /app
COPY pyproject.toml /app
COPY poetry.lock /app

WORKDIR /app

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

RUN python client/get_dataset.py

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser