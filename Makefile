.PHONY: install format lint test clean

install:
	pip install -e .

install-dev:
	pip install -e ".[dev]"

format:
	black .
	isort .

lint:
	flake8
	mypy .

test:
	pytest

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .coverage
	rm -rf htmlcov/
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete 