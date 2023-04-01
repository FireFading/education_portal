connect to postgres: `docker exec -it postgres psql -U postgres`

apply migrations: `alembic upgrade head`
create new migrations: `alembic revision --autogenerate -m "<migration name>"` in fastapi container