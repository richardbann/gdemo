.PHONY: init
init:
	python3 -m venv ./.venv
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install -r requirements_dev.txt
