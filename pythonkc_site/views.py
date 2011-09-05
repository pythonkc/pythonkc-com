# -*- coding: utf-8 -*-


from django.conf import settings
from django.core.cache import cache
from django.core.exceptions import ImproperlyConfigured
from django.core.urlresolvers import reverse
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from functools import wraps
from pythonkc_meetups import PythonKCMeetups
from pythonkc_site.forms import ContactForm
import logging


logger = logging.getLogger(__name__)


try:
    api_key = settings.MEETUP_API_KEY
except AttributeError:
    raise ImproperlyConfigured('MEETUP_API_KEY is required in settings')


meetups = PythonKCMeetups(api_key, http_timeout=6)
num_past_events = getattr(settings, 'MEETUP_SHOW_PAST_EVENTS', 3)


class PythonKCHome(FormView):
    template_name = 'index.html'
    form_class = ContactForm

    def get_success_url(self):
        return reverse('home')

    def form_valid(self, form):
        # TODO send email
        # TODO create success msg with msg framework
        return super(PythonKCHome, self).form_valid(form)

    def get_context_data(self, **kwargs):

        @memoize_in_cache('next_event', 60 * 5)
        def get_next_event():
            logging.info('Retrieving next event from Meetup.com')
            upcoming_events = meetups.get_upcoming_events()
            return upcoming_events[0] if upcoming_events else None

        @memoize_in_cache('past_events', 60 * 60)
        def get_past_events():
            logging.info('Retrieving past events from Meetup.com')
            return meetups.get_past_events()[:num_past_events]

        return {
            'next_event': get_next_event(),
            'past_events': get_past_events(),
            'form': kwargs.get('form', None) or ContactForm()
        }


def memoize_in_cache(cache_key, cache_timeout_seconds=None):
    """Cache the result of a no-args function."""
    def decorator(func):
        @wraps(func)
        def decorated():
            value = cache.get(cache_key)
            if not value:
                value = func()
                cache.set(cache_key, value, cache_timeout_seconds)
            return value
        return decorated
    return decorator


class PythonKCComingSoon(TemplateView):
    template_name = 'coming_soon.html'
