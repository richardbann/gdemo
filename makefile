SHELL=/bin/bash
export UID=$(shell id -u)
export GID=$(shell id -g)


.PHONY: init
init:
	python3 -m venv ./.venv
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install -r requirements.txt

.PHONY: up
up:
	.venv/bin/docker-compose up -d

.PHONY: build
build:
	.venv/bin/docker-compose run --rm frontend node_modules/.bin/webpack --mode development
