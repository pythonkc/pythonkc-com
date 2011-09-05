# -*- coding: utf-8 -*-
"""
Provides a function for sending the email when the site's contact form is
submitted by a visitor.

"""


from django.conf import settings
from django.core.mail import BadHeaderError
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
import logging


logger = logging.getLogger(__name__)
_SUBJECT_TEMPLATE = 'pythonkc_site/contact/email_subject.txt'
_TEXT_TEMPLATE = 'pythonkc_site/contact/email_contents.txt'
_HTML_TEMPLATE = 'pythonkc_site/contact/email_contents.html'


def send_contact_form_email(first_name, last_name, email, message):
    """
    Send an email based on the submission of the site's contact form.

    """
    context = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'message': message
    }

    subject = render_to_string(_SUBJECT_TEMPLATE, context)
    text_content = render_to_string(_TEXT_TEMPLATE, context)
    html_content = render_to_string(_HTML_TEMPLATE, context)
    from_email = settings.CONTACT_EMAIL_FROM
    to_emails = settings.CONTACT_EMAIL_TO

    message = EmailMultiAlternatives(subject, text_content, from_email,
                                     to_emails)
    message.attach_alternative(html_content, "text/html")

    try:
        message.send()
    except BadHeaderError:
        logger.exception('Exception occurred while sending contact form email')
