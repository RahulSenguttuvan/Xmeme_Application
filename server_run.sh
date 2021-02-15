#!/bin/bash


cd backend

py manage.py makemigrations
py manage.py migrate
py manage.py runserver 8081