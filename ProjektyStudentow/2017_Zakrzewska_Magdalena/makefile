cleanProject:
	rm -r db.sqlite3
	find . -path "*/migrations/*.pyc"  -delete
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc"  -delete

run:
	python3 manage.py runserver

build:
	python3 manage.py makemigrations
	python3 manage.py migrate
	make run