.PHONY: test format lint all

test:
	pytest

format:
	black .

lint:
	flake8 .

all: format lint test
