# Utility Locker Products API

A simple API for retrieving products and product types, built with Django and [Django Rest Framework](https://www.django-rest-framework.org/).

## Github Workflows

Workflows are in place for linting (using [pycodestyle](https://pypi.org/project/pycodestyle/)) and running tests each time the master branch is pushed to.  

## Deployment

The repository includes configuration files (.ebextensions) for automating deployment to AWS Elastic Beanstalk. This ensures that static files are collected, and database migrations are executed when deploying via Elastic Beanstalk CLI.

## Local installation (in a virtual environment)

Grab a copy of the project:
```
git clone https://github.com/rc3k/utility-locker-api.git
```

Create a virtual environment and install dependencies.
```
mkvirtualenv utility-locker-api
pip install -r requirements.txt
pip install -r requirements.dev.txt
```

Enter your database settings in app/settings.py (use app/example_settings.py as a basis)

Initialize your database:
```
python ./manage.py migrate
```

Run the development server:
```
python ./manage.py runserver
```

## Running tests locally
Tests are written in [Pytest](https://docs.pytest.org/en/stable/).

To execute the tests run:
```
pytest .
```
