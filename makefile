.PHONY: init
init:
	python3 -m venv ./.venv
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install -r requirements.txt

tailwind:
	.venv/bin/docker-compose run --rm frontend node_modules/.bin/tailwind \
		build css/styles.css -o build/styles.css
