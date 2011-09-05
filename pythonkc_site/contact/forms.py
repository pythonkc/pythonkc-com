# -*- coding: utf-8 -*-


from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(
            widget=forms.TextInput(attrs={'placeholder': 'FIRST NAME',
                                          'class': 'contact-name'}))
    last_name = forms.CharField(
            widget=forms.TextInput(attrs={'placeholder': 'LAST NAME',
                                          'class': 'contact-name'}))
    email = forms.EmailField(
            widget=forms.TextInput(attrs={'placeholder': 'E-MAIL ADDRESS',
                                          'class': 'contact-email'}))
    message = forms.CharField(
            widget=forms.Textarea(attrs={'placeholder': 'MESSAGE',
                                         'class': 'contact-message', 
                                         'rows': '3'}))
