Django Careers
==============

A simple app to render a careers-page on your website.

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    pip install django-careers

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://github.com/theartling/django-careers.git#egg=careers

Add ``careers`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'careers',
    )

Add the ``careers`` URLs to your ``urls.py``

.. code-block:: python

    urlpatterns = [
        url(r'^careers/', include('careers.urls')),
    ]

Don't forget to migrate your database

.. code-block:: bash

    ./manage.py migrate careers


Usage
-----

Simply visit the django admin and start creating career objects.

Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    mkvirtualenv -p python2.7 django-careers
    make develop

    git co -b feature_branch master
    # Implement your feature and tests
    git add . && git commit
    git push -u origin feature_branch
    # Send us a pull request for your feature branch

In order to run the tests, simply execute ``tox``. This will install two new
environments (for Django 1.8 and Django 1.9) and run the tests against both
environments.
