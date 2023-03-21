check-pep8:
	flake8 code & mypy code

format:
	black code

docker-run:
	python3 /app/code/scripts/migrate.py
	/usr/bin/supervisord -n