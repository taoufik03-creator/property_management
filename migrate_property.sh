#!/bin/bash
set -e

echo "Step 1: Running migrations on original Postgres..."
python manage.py migrate

echo "Step 2: Dumping Property data..."
python manage.py dumpdata listings.Property > property_data.json

echo "Step 3: Switching to Postgres-UIwj..."
# The DATABASE_URL will be updated via Railway variables

echo "Step 4: Running migrations on Postgres-UIwj..."
python manage.py migrate

echo "Step 5: Loading dumped data..."
python manage.py loaddata property_data.json

echo "Migration complete!"
