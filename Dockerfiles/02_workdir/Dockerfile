FROM python:3.9.6

RUN mkdir app

WORKDIR ./app

COPY ./script.py ./script.py

WORKDIR /

CMD ["cat", "app/script.py"]
