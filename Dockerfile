FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /currency_yahoo_rest_api

# Install dependencies
COPY Pipfile Pipfile.lock /currency_yahoo_rest_api/
RUN pip install pipenv && pipenv install --system

COPY . /currency_yahoo_rest_api/