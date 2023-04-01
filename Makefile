up:
	docker compose up --build

down:
	docker compose down && docker network prune --force