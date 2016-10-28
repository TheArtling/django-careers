Django Careers
==============

A simple app to render a careers-page on your website.

You can use the Django admin to create job offers via Markdown. You can
see the result in action at https://theartling.com/careers/

Installation
------------

To get the latest stable release from PyPi

::

    pip install django-careers

To get the latest commit from GitHub

::

    pip install -e git+git://github.com/theartling/django-careers.git#egg=careers

Add ``careers`` to your ``INSTALLED_APPS``

::

    INSTALLED_APPS = (
        ...,
        'careers',
    )

Add the ``careers`` URLs to your ``urls.py``

::

    urlpatterns = [
        url(r'^careers/', include('careers.urls')),
    ]

This app has
`django-markdown-app <https://github.com/sv0/django-markdown-app>`_ as
a dependency, so please have a look at their repo and follow their
installation instructions.

Don't forget to migrate your database

::

    ./manage.py migrate careers

Usage
-----

Simply visit the django admin and start creating ``CareerPosition``
objects.

Local Test
----------

If you want to give app a quick try on your local machine, you can do
the following:

::

    mkvirtualenv -p python2.7 django-careers
    pip install -r requirements.txt
    pip install -r test_requirements.txt
    ./manage.py migrate
    ./manage.py createsuperuser
    ./manage.py runserver
    # browse to the admin and create some objects
    # browse to /careers/

Contribute
----------

If you want to contribute to this project, please perform the following
steps

::

    # Fork this repository
    # Clone your fork
    mkvirtualenv -p python2.7 django-careers
    make develop

    git co -b feature_branch master
    # Implement your feature and tests
    git add . && git commit
    git push -u origin feature_branch
    # Send us a pull request for your feature branch

In order to run the tests, simply execute ``tox``. This will install two
new environments (for Django 1.8 and Django 1.9) and run the tests
against both environments.

If tox throws errors, you can also run the tests via ``./runtests.py``
