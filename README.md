# labcodes-wiki

A barebones Django app, which can easily be deployed to Heroku.

This application supports the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) article - check it out.

## Running Locally

Make sure you have Python 3.7 [installed locally](http://install.python-guide.org). To push to Heroku, you'll need to install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), as well as [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

For the wiki, we have a couple of system dependencies as well. [Take a look at their docs](https://django-wiki.readthedocs.io/en/latest/installation.html) to properly install them. After that, things should be set up as follows:

```sh
python3 -m venv .
source bin/activate
pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

Your app should now be running on [localhost:8000](http://localhost:8000/).

## Deploying to Heroku

Assuming you have added the 'heroku' remote, you may deploy to heroku like this:

```sh
git push heroku master
heroku run python manage.py migrate
heroku open
```

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)

For more information on Django:

- [Django docs](https://docs.djangoproject.com/en/2.2/)

For more information about the wiki app:

- [Wiki docs](https://django-wiki.readthedocs.io/en/latest/index.html)

The frontend uses bootstrap 3:

- [Bootstrap docs](https://getbootstrap.com/docs/3.3/)
