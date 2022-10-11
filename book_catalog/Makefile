# COLORS
GREEN  := $(shell tput -Txterm setaf 2)
WHITE  := $(shell tput -Txterm setaf 7)
YELLOW := $(shell tput -Txterm setaf 3)
RESET  := $(shell tput -Txterm sgr0)

.DEFAULT_GOAL := help
.PHONY: setup run makemigrations migrate shell lint type flake8 mypy clean

VENV=../.venv
PYTHON=$(VENV)/bin/python
CELERY=$(VENV)/bin/celery

## Initialize venv and install dependencies
setup: $(VENV)/bin/activate
$(VENV)/bin/activate:
	python -m venv $(VENV)
	$(PYTHON) -m pip install pipenv==2022.1.8
	$(PYTHON) -m pipenv sync -d

migrate: setup
	$(PYTHON) manage.py migrate --run-syncdb

## Run project
run: migrate
	$(PYTHON) manage.py runserver 8003


makemigrations:
	$(PYTHON) manage.py makemigrations

## Run django shell
shell:
	$(PYTHON) manage.py shell

## Analyze project source code for slylistic errors
lint: setup
	$(PYTHON) -m flake8 api book_catalog

## Analyze project source code for typing errors
type: setup
	$(PYTHON) -m mypy api book_catalog

## Run flake8
flake8: setup
	$(PYTHON) -m flake8 api book_catalog

## Run mypy
mypy: setup
	$(PYTHON) -m mypy api book_catalog

## Clean up project environment
clean:
	rm -rf $(VENV) *.egg-info .eggs .coverage htmlcov .pytest_cache
	find . -type f -name '*.pyc' -delete

## Show help
help:
	@echo ''
	@echo 'Usage:'
	@echo '  ${YELLOW}make${RESET} ${GREEN}<target>${RESET}'
	@echo ''
	@echo 'Targets:'
	@awk '/^[a-zA-Z\-\_0-9]+:/ { \
		helpMessage = match(lastLine, /^## (.*)/); \
		if (helpMessage) { \
			helpCommand = $$1; sub(/:$$/, "", helpCommand); \
			helpMessage = substr(lastLine, RSTART + 3, RLENGTH); \
			printf "  ${YELLOW}%-$(TARGET_MAX_CHAR_NUM)15s${RESET} ${GREEN}%s${RESET}\n", helpCommand, helpMessage; \
		} \
	} \
	{ lastLine = $$0 }' $(MAKEFILE_LIST)
	@echo ''
