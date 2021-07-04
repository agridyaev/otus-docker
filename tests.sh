#!/bin/bash

docker build -t tests .

docker run --name test_run tests pytest --browser $1 -n $2

docker cp test_run:/app/allure-report .

allure serve allure-report

docker rm test_run

# docker run --name test_run tests && docker cp test_run:/app/allure-report . && allure serve allure-report
