# -*- coding: utf-8 -*-
"""
Sources of prefix and hint list:

* http://mobiforge.com/developing/story/build-a-mobile-and-desktop-friendly-application-django-15-minutes
* http://www.entzeroth.com/code
* http://www.useragentstring.com

"""


mobile_ua_prefixes = [
    'w3c ','acs-','alav','alca','amoi','audi','avan','benq','bird','blac',
    'blaz','brew','cell','cldc','cmd-','dang','doco','eric','hipt','inno',
    'ipaq','java','jigs','kddi','keji','leno','lg-c','lg-d','lg-g','lge-',
    'maui','maxo','midp','mits','mmef','mobi','mot-','moto','mwbp','nec-',
    'newt','noki','palm','pana','pant','phil','play','port','prox','qwap',
    'sage','sams','sany','sch-','sec-','send','seri','sgh-','shar','sie-',
    'siem','smal','smar','sony','sph-','symb','t-mo','teli','tim-','tosh',
    'tsm-','upg1','upsi','vk-v','voda','wap-','wapa','wapi','wapp','wapr',
    'webc','winw','winw','xda','xda-'
]


mobile_ua_hints = [
    'SymbianOS', 
    'Opera Mini',
    'iPhone',
    'Android',
    'Opera Mobi', 
    'webOS',
    'BlackBerry',
    # Portable game consoles
    'Bunjalloo', # Nintendo DS
    'PlayStation Portable'
]


def is_mobile_browser(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    ua_prefix = user_agent.lower()[:4]

    if ua_prefix in mobile_ua_prefixes:
        return True

    for hint in mobile_ua_hints:
        if user_agent.find(hint) >= 0:
            return True

    return False
