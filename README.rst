=============================================
recipi - nutrition database and meal planner.
=============================================

.. image:: https://readthedocs.org/projects/recipi/badge/?version=latest
    :target: https://readthedocs.org/projects/recipi/?badge=latest
    :alt: Documentation Status

.. image:: https://travis-ci.org/recipi/recipi.png?branch=master
    :target: https://travis-ci.org/recipi/recipi

.. figure:: https://recipi.readthedocs.org/en/latest/_static/logo.jpg
   :align: right
   :target: http://thenounproject.com/term/pear/56646/


Features
========

...

Installation
------------

.. code-block:: bash

    $ Create your virtualenv (recommended, use virtualenvwrapper)
    $ mkvirtualenv recipi

    $ # Clone repository
    $ git clone git@github.com:recipi/recipi.git

    $ # Activate Environment and install. Note that this might take a while
    $ # and actually downloads tons of stuff (used for NLTK)
    $ workon recipi
    $ make develop

    $ # run tests
    $ make test


Edit settings
-------------

Create a new file ``src/recipi/settings.py`` with the following content:

.. code-block:: python

    from recipi.conf.development import *

Edit and adapt this file to your specific environment.


Setup the database
------------------

.. note::

    Please note that recipi was developed with PostgreSQL in mind. It may not be
    performant enough on other datastores or may not even support them.


Create an empty new PostgreSQL database (any other supported by Django works too).

.. code-block:: bash

    $ createdb recipi_dev

.. note::

    You might need to apply a postgresql user (``createdb -U youruser``) e.g ``postgres``
    for proper permissions.


.. code-block:: bash

    $ python manage.py migrate


Superuser
---------

.. code-block:: bash

    $ # Create a new super user
    $ python manage.py createsuperuser


Import nutrition data and recipes
---------------------------------

To import a pre-defined fixture:

.. code-block:: bash

    $ gunzip resources/fixtures/food.json.gz
    $ python manage.py loaddata resources/fixtures/food.json

Or to freshly import all data:

.. code-block:: bash

    $ python import.py

.. note::

    This will take some time...


Run the server, celery and other services
-----------------------------------------

Other services being used:

* Celery, is being used to run [regular] tasks, e.g for mail output.
* gulp-sass, is being used to compile our scss files and the foundation framework.


To start all of them (including the tls-server):

.. code-block:: bash

   $ gulp serve

.. note::

    Our celery configuration requires redis to be installed and running.
    Please make sure it's up!


Run the test-suite
------------------

.. code-block:: bash

    $ make test

Resources
---------

* `Documentation <http://recipi.readthedocs.org/>`_
* `Bug Tracker <https://github.com/recipi/recipi/issues>`_
* `Code <https://github.com/recipi/recipi>`_
