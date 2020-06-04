test: install
	~/.local/bin/poetry run pytest -v

install:
	pip -q install poetry --user
	~/.local/bin/poetry install -q
