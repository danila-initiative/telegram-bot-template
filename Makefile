check-pep8:
	flake8 code codegen --exclude=code/generated
	mypy code codegen --exclude=code/generated
	flake8 --ignore=E501 code/generated

format:
	black code codegen

docker-run:
	/usr/bin/supervisord -n

start-bot:
	python3 /app/codegen/gen.py
	python3 /app/code/scripts/migrate.py
	python3 /app/code/user_bot.py

gen:
	python3 codegen/gen.py