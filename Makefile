.PHONY: install, format

install:
	@poetry install
format:
	@isort .
	@black .
test:
	pytest -v