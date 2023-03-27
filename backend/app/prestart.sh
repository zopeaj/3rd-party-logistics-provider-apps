#! /usr/bin/ bash

python app/backend_pre_start.py

# Run First Migration
alembic revision --autogenerate -m "First Logistics App migration"

# Run upgrade head
alembic upgrade head

# Create initial data in DB
python app/initial_data.py

