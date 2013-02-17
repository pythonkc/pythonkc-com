# -*- coding: utf-8 -*-
"""
Provides the Meetup.com events that will be used to populate the site homepage.

"""


from django.conf import settings
from django.core.cache import cache
from django.core.exceptions import ImproperlyConfigured
from functools import wraps
from pythonkc_meetups import PythonKCMeetups
import logging


logger = logging.getLogger(__name__)


try:
    api_key = settings.MEETUP_API_KEY
except AttributeError:
    raise ImproperlyConfigured('MEETUP_API_KEY is required in settings')


meetups = PythonKCMeetups(api_key, http_timeout=6)
num_past_events = getattr(settings, 'MEETUP_SHOW_PAST_EVENTS', 3)


def memoize_in_cache(cache_key, cache_timeout_seconds=None):
    """
    Caches the result of a no-args function. Further, a backup cache is
    maintained, updated as often as the primary but waits much longer to expire
    than the primary cache.

    NOTE This should all go away once gondor gets schedule celery tasks that
    can be used to periodically populate the meetup.com event cache (thereby
    allowing visitor requests to avoid the hit).
    """

    backup_cache_key = cache_key + '_backup'
    backup_cache_timeout_seconds = (cache_timeout_seconds * 10000
                                    if cache_timeout_seconds else
                                    60 * 60 * 24)

    def decorator(func):
        @wraps(func)
        def decorated():
            value = cache.get(cache_key)
            if not value:
                try:
                    value = func()
                    cache.set(cache_key, value, cache_timeout_seconds)
                    cache.set(backup_cache_key, value,
                              backup_cache_timeout_seconds)
                except:
                    value = cache.get(backup_cache_key)
                    if value:
                        logging.exception('Had to load backup value due to '
                                          'exception')
                    else:
                        raise
            return value
        return decorated
    return decorator


@memoize_in_cache('next_event', 60 * 5)
def get_next_event():
    logging.info('Retrieving next event from Meetup.com')
    upcoming_events = meetups.get_upcoming_events()
    return upcoming_events[0] if upcoming_events else None


@memoize_in_cache('past_events', 60 * 60)
def get_past_events():
    logging.info('Retrieving past events from Meetup.com')
    return meetups.get_past_events()[:num_past_events]
