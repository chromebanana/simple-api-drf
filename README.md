# Bookmarks API

This is a simple API created to practise using the Django Rest framework with JWT authentication.

- register, login a user, authenticate
- view saved bookmarks (once authenticated)


## Run this application
Create an environment according to dependencies in the Pipfile. Then do
```sh
    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py runserver
```

## Note
Database is not being tracked. If you are going to deploy this you may need to remove db.sqlite3 and migrations from .gitignore

## Testing

```sh 
    $ python manage.py test
```
## Thanks
Thank you @kasulani for this helpful [tutorial](https://medium.com/backticks-tildes/lets-build-an-api-with-django-rest-framework-32fcf40231e5)