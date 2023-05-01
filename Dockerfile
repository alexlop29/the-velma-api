FROM python:3.11.3

WORKDIR /code

RUN pip3 install pipenv==2023.4.29

COPY Pipfile /code

RUN pipenv install

COPY ./app /code/app/

WORKDIR /code/app

ENV PYTHONPATH=.
