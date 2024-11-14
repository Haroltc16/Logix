#!/usr/bin/env bash

set -o errexit

pip install - requeriments.txt

python manage.py collectstatic --noinput
python manage.py migrate
