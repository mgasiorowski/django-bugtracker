from django import forms
from django.forms import ModelForm

from .models import Bug


class AddBugForm(ModelForm):
    class Meta:
        model = Bug
        fields = ['title',
                  'description',
                  'assignee',
                  'state',
                  'level']
        
    def clean(self):
        return super(AddBugForm, self).clean()

        cleaned_data = self.cleaned_data

        state = cleaned_data.get('state')
        if state is None:
            msg = "Must put 'state' in bug."
            self.add_error('state', msg)
            raise forms.ValidationError("You have failed validation!")

        level = cleaned_data.get("level")
        if level is None:
            print 2
            msg = "Must put 'level' in bug."
            self.add_error('level', msg)
            raise forms.ValidationError("You have failed validation!")
