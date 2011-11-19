# -*- coding: utf-8 -*-
"""
Overview
========
Simple detection of user agent types, where "type" is defined as one of:

* Standard
* Mobile

The idea is to generically categorize user agents with simple user agent string
matching, instead of full determination of user agent capabilities.

If we need to we could add tablet detection and that type as well.

Usage
=====
Simply install the middleware::

    pythonkc_site.ua_detection.middleware.UserAgentTypeDetectionMiddleware

Then request objects will have the following additional attributes:

is_mobile
    Boolean value indicating whether or not the request was made by a mobile
    user-agent.

Derived from:

* http://mobiforge.com/developing/story/build-a-mobile-and-desktop-friendly-application-django-15-minutes
* http://www.entzeroth.com/code

"""
