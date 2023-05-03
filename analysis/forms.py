from django import forms

from analysis.models import Twittertext


class TwittertextForm(forms.ModelForm):
    class Meta:
        model = Twittertext
        fields = "__all__" 
    