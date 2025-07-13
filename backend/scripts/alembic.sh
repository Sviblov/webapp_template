alembic init -t async db/migrations


alembic revision --autogenerate


alembic upgrade head
