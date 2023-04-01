## before run
- change .env.example to .env AND also in the project settings, don't forget about tests folder
## run project
- `docker compose up --build` OR `make up`

## down docker
- `docker compose down && docker network prune --force` OR `make down`

## database
- connect to postgres: `docker exec -it postgres psql -U postgres`

## migrations
- apply migrations: `alembic upgrade head` in fastapi container
- create new migrations: `alembic revision --autogenerate -m "<migration name>"` in fastapi container

## formatting and linting
- run ufmt: `ufmt format .`
- run black: `black --config=configs/.black.toml app`
- run ruff: `ruff check --config=configs/.ruff.toml --fix app`
- run flake8: `flake8 --config=configs/.flake8 app`

- OR `nox` in root

## run tests
- `pytest .` OR `pytest ./tests` OR run `nox`
