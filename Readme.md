- Python 3.11.0
    - $ Python3 --version
- pipenv
    - $ pip3 install pipenv
- cd into project directory
    - $ pipenv install django
- enable django admin integration
    - $ django-admin
- create django project inside the working directory
    - $ django-admin startproject storefront .
- start the development server
    - $ python3 manage.py runserver 
    - http://localhost:8000/ is the default port
    - to start on a different port: 
        - $ python3 manage.py runserver 9000

- Install Django Debug Toolbar
    - $ pipenv install django-debug-toolbar
    - add 'debug_toolbar' to INSTALLED_APPS in settings.py
        - import debug_toolbar 
    - add 'debug_toolbar.middleware.DebugToolbarMiddleware' to middleware in settings.py
    - add the following to settings.py for local development
        - INTERNAL_IPS = [
            '127.0.0.1',
        ]


- create a new app
    - python3 manage.py startapp playground
- add the new app to the list of INSTALLED_APPS in settings.py
- create a urls.py inside the playground directory
    - import dependencies
    - define the route from /playground/... 
    - add the playground app to urlpatterns in urls.py within the main application directory
- in playground/views.py define a function to execute when the user hits the above endpoint


