#!/bin/bash

# This script is responsible for database migrations, seeding of
# demonstrational data and preparing static files.

# Run this script after all Python dependencies are installed.

SEED_DEMO_DATA=False python manage.py migrate shelter
SEED_DEMO_DATA=True python manage.py migrate

python manage.py collectstatic --noinput # prepare static files
