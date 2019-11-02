rm db.sqlite3
python sample_app/fixtures/generate_sample_data.py > sample_app/fixtures/fixture.json
python manage.py migrate
python manage.py loaddata sample_app/fixtures/users.json
python manage.py loaddata sample_app/fixtures/fixture.json
