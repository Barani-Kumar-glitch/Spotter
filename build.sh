#!/usr/bin/env bash

pip install -r requirements.txt

python manage.py collectstatic --noinput

<<<<<<< HEAD
python manage.py migrate
=======
python manage.py migrate
>>>>>>> c8fb2ac92ec83949e11f57c83eb3e3e30f57e82b
