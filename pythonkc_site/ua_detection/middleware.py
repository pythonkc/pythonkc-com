# -*- coding: utf-8 -*-


from pythonkc_site.ua_detection.types import is_mobile_browser


class UserAgentTypeDetectionMiddleware(object):

    def process_request(self, request):
        request.is_mobile = is_mobile_browser(request)
