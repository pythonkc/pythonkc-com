# -*- coding: utf-8 -*-


from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import FormView
from django.views.generic import TemplateView
from pythonkc_site.contact.email import send_contact_form_email
from pythonkc_site.contact.forms import ContactForm
from pythonkc_site.meetups import events


class StandardHome(FormView):
    template_name = 'home.html'
    form_class = ContactForm

    def get_success_url(self):
        return '{0}?contact_sent=yes'.format(reverse('home'))

    def form_valid(self, form):
        send_contact_form_email(**form.cleaned_data)
        return super(StandardHome, self).form_valid(form)

    def get_context_data(self, **kwargs):
        return {
            'next_event': events.get_next_event(),
            'past_events': events.get_past_events(),
            'form': kwargs.get('form', None) or ContactForm()
        }


class MobileHome(TemplateView):
    template_name = 'mobile/home.html'

    def get_context_data(self, **kwargs):
        return {
            'next_event': events.get_next_event(),
            'contact_email': settings.CONTACT_EMAIL_TO[0]
        }


class MobilePastMeetups(TemplateView):
    template_name = 'mobile/past_meetups.html'

    def get_context_data(self, **kwargs):
        return {
            'past_events': events.get_past_events()
        }


standard_home_view = StandardHome.as_view()
mobile_home_view = MobileHome.as_view()
mobile_past_view = MobilePastMeetups.as_view()


def home(request, *args, **kwargs):
    """
    Standard browsers: show home page with next and past meetups
    Mobile browsers: show home page with next meetup

    """
    if request.is_mobile:
        return mobile_home_view(request, *args, **kwargs)
    return standard_home_view(request, *args, **kwargs)


def past_meetups(request, *args, **kwargs):
    """
    Standard browsers: redirect to home page
    Mobile browsers: show list of past meetups with links to meetup.com

    """
    if request.is_mobile:
        return mobile_past_view(request, *args, **kwargs)
    return redirect(reverse('home'))
