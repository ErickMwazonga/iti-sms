#django
from django import forms

#local
from django.forms import Textarea
from models import *

#lib


class AddContactForm(forms.ModelForm):
    class Meta:
        model = contacts
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(AddContactForm, self).__init__(*args, **kwargs)
        self.fields['firstName'].widget.attrs.update({'class': 'form-control'})
        self.fields['lastName'].widget.attrs.update({'class': 'form-control'})
        self.fields['phoneNumber'].widget.attrs.update({'class': 'form-control form-horizontal'})

class AddContactToGroupForm(forms.ModelForm):
    class Meta:
        model = contactgroup
        exclude = ['contact']

    def __init__(self, *args, **kwargs):
        super(AddContactToGroupForm, self).__init__(*args, **kwargs)
        self.fields['groupName'].widget.attrs.update({'class': 'form-control'})


class SendMsgForm(forms.Form):
    phoneNumber = forms.CharField(label="Numero de Telephone", required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': "form-control", 'maxlength': "160"}))


class createTemplateForm(forms.ModelForm):
    class Meta:
        model = msgTemplates
        exclude = ['user']
        widgets = {
            'msgText': Textarea(),
        }

    def __init__(self, *args, **kwargs):
        super(createTemplateForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['msgText'].widget.attrs.update({'class': 'form-control'})