============================
Running PythonKC.com Locally
============================

#. ``git clone git://github.com/pythonkc/pythonkc.com.git``

#. ``cd pythonkc.com/pythonkc_site``

#. ``mkvirtualenv --no-site-packages --distribute pykc`` (you're using virtualenv, right? :))

#. ``pip install -r requirements/project.txt``

#. Create ``local_settings.py``, with::

    DEBUG = TEMPLATE_DEBUG = True
    # OPTIONAL  If you don't want to send emails while running locally:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    # Otherwise, you probably want emails you test with to come to you:
    CONTACT_EMAIL_TO = ['me@gmail.com']

#. Create a `.env` file with::

    #!/bin/sh
    export MEETUP_API_KEY="<your meetup.com API key>"
    export DJANGO_SECRET_KEY="<your secret key>"
    
    # if you're not using console.EmailBackend:
    export EMAIL_HOST_USER="<your email user>"
    export EMAIL_HOST_PASSWORD="<your email password>"

#. Source your .env file: ``source .env``.

#. ``python manage.py syncdb``

#. ``python manage.py runserver``

#. Profit!!!

Note that both ``local_settings.py`` and ``.env`` are in our ``.gitignore``, so you don't commit what you do there.
