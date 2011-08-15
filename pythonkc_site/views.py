# -*- coding: utf-8 -*-


from django.conf import settings
from django.views.generic.base import TemplateView
from pythonkc_meetups import PythonKCMeetups


try:
    api_key = settings.MEETUP_API_KEY
except AttributeError:
    raise ImproperlyConfigured('MEETUP_API_KEY is required in settings')


meetups = PythonKCMeetups(api_key, http_timeout=6)
num_past_events = getattr(settings, 'MEETUP_SHOW_PAST_EVENTS', 3)


class PythonKCHome(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        # NOTE Instead of individually caching next/past events, we're
        # simply going to cache this whole page until things get more
        # complicated (see urls.py for caching decoration).

        def get_next_event():
            upcoming_events = meetups.get_upcoming_events()
            return upcoming_events[0] if upcoming_events else None

        def get_past_events():
            return meetups.get_past_events()[:num_past_events]

        return {
            'next_event': get_next_event(),
            'past_events': get_past_events()
        }
