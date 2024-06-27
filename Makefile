export COMPOSE_FILE=docker-compose.yml
SHELL := /bin/bash

build:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Building in dev mode"
	@echo "------------------------------------------------------------------"
	@docker-compose build


dev:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Running in dev mode"
	@echo "------------------------------------------------------------------"
	@docker-compose up