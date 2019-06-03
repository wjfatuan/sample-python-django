# Python Sample

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/65d216e1600e4566a3fda6d6ad5c3464)](https://app.codacy.com/app/wilson.forero/sample-python-django?utm_source=github.com&utm_medium=referral&utm_content=wjfatuan/sample-python-django&utm_campaign=Badge_Grade_Dashboard)
[![CircleCI](https://circleci.com/gh/wjfatuan/sample-python-django.svg?style=shield&circle-token=:circle-token)](https://circleci.com/gh/wjfatuan/sample-python-django)

A barebones Django app, which can easily be deployed to Heroku. This application is based on  the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) article - check it out. You can access an online version of it in this [site](https://stark-retreat-94725.herokuapp.com/).

## Course concepts

This application has examples of different design patterns from the class.

The original version of this sample project is implemented using plain Python, but this one is merged with the sample provided by Heroku. Navigate the source code to find the samples needed. 

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org). Also, install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) and [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```zsh
$ git clone https://github.com/wjfatuan/sample-python-django.git
$ cd sample-python-django

$ pipenv install

$ createdb python_getting_started

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```zsh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

-    [Python on Heroku](https://devcenter.heroku.com/categories/python)
