#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
<<<<<<< HEAD
python manage.py collectstatic --noinput
=======
python manage.py collectstatic --noinput
>>>>>>> 21c92cddff268d23a9899c592f2ef665f0de7285
