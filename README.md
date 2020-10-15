API with authentication using JWT

The simplest style of permission would be to allow access to any authenticated user, and deny access to any unauthenticated user. This corresponds the IsAuthenticated class in DRF.

read only for unauthenticated

please note the database has been removed. If you want to deploy or track your database you will most likely have to remove dp.sqlite3 from .gitignore