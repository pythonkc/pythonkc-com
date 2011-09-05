=====================================
Contact App for the PythonKC.com Site
=====================================

Contact Form
------------
``pythonkc_site.contact.forms`` provides the contact form class.

Sending Contact Email
---------------------
The ``pythonkc_site.contact.email`` module provides a function to send an email
based on the data from a submitted contact form.

This app also provides templates that used to compose the email, so these can
be used to customize the email that is sent on contact form submission.

Settings
--------
The following settings are expected to be provided by the Django site for the
contact functionality to work.

``CONTACT_EMAIL_FROM``
    The email address to send contact form emails from.
``CONTACT_EMAIL_TO``
    The email addresses to send contact form email to.
