============================
Running PythonKC.com Locally
============================

#. ``git clone git://github.com/pythonkc/pythonkc.com.git``

#. ``cd pythonkc.com/pythonkc_site``

#. ``mkvirtualenv --no-site-packages --distribute pykc`` (you're using virtualenv, right? :))

#. ``pip install -r requirements/project.txt``

#. ``python manage.py syncdb``

#. Create ``local_settings.py``, with::

    DEBUG = TEMPLATE_DEBUG = True
    # OPTIONAL  If you don't want to send emails while running locally:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    # Otherwise, you probably want emails you test with to come to you:
    CONTACT_EMAIL_TO = ['me@gmail.com']

#. Create ``private_settings.py`` with:

    #. Meetup.com API key::

        MEETUP_API_KEY = "<your API key for meetup.com>"

    #. SMTP settings (if you kept the default email backend of SMTP above)::

        # For example....
        EMAIL_HOST = "smtp.gmail.com"
        EMAIL_PORT = 587
        EMAIL_USE_TLS = True
        EMAIL_HOST_USER = "contact@pythonkc.com"
        EMAIL_HOST_PASSWORD = "*******************"

#. ``python manage.py runserver``

#. Profit!!!

Note that both ``local_settings.py`` and ``private_settings.py`` are in our ``.gitignore``, so you don't commit what you do there.
