# -*- coding: utf-8 -*-


from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import FormView
from pythonkc_site.contact.email import send_contact_form_email
from pythonkc_site.contact.forms import ContactForm
from pythonkc_site.meetups import events


# 1. function-based view
def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_contact_form_email(**form.cleaned_data)
            return redirect('{0}?contact_sent=yes'.format(reverse('home')))
    else:
        form = ContactForm()

    context = {
        'next_event': events.get_next_event(),
        'past_events': events.get_past_events(),
        'form': form
    }
    return render(request, 'index.html', context)


# 2. identical class-based view
class PythonKCHome(FormView):
    template_name = 'index.html'
    form_class = ContactForm

    def get_success_url(self):
        return '{0}?contact_sent=yes'.format(reverse('home'))

    def form_valid(self, form):
        send_contact_form_email(**form.cleaned_data)
        return super(PythonKCHome, self).form_valid(form)

    def get_context_data(self, **kwargs):
        return {
            'next_event': events.get_next_event(),
            'past_events': events.get_past_events(),
            'form': kwargs.get('form', None) or ContactForm()
        }
