import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spotter.settings')
django.setup()

from django.db import connection

sql = """
CREATE TABLE IF NOT EXISTS weight_loss_plan (
    plan_id integer NOT NULL PRIMARY KEY,
    gender varchar(10) NOT NULL,
    weight_range_kg varchar(20) NOT NULL,
    experience varchar(20) NOT NULL,
    full_week_routine text NOT NULL,
    diet_plan text NOT NULL
);

CREATE TABLE IF NOT EXISTS bodybuilding_plan (
    plan_id integer NOT NULL PRIMARY KEY,
    gender varchar(10) NOT NULL,
    weight_range_kg varchar(20) NOT NULL,
    experience varchar(20) NOT NULL,
    full_week_routine text NOT NULL,
    diet_plan text NOT NULL
);
"""

with connection.cursor() as cursor:
    cursor.execute(sql)
print("Tables created successfully using raw SQL.")
