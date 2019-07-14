# Project Title

Rest-API for work with courses and students.

## Getting started

1. `python3.6 -m venv .venv`
2. `source .venv/bin/activate`
3. `pip install -r requirements/local.txt --user`
4. `./manage.py migrate` OR `make migrate`
5. `./manage.py createsuperuser` OR `make superuser`
6. `./manage.py runserver` OR `make server`

## Change default database

1) `touch .env`
2) Add to .env file `DATABASE_URL=postgres://{DB_USER}:{DB_PASS}@localhost:5432/{DB_NAME}`

## Running the tests
`pytest`
## Links for localhost
[Admin page](http://localhost:8000/admin)

[Swagger](http://localhost:8000/swagger)

### Note
There are lack of tests due to limited time. I added a test basis and one test to show which packages I 
prefer to use for this purposes.
