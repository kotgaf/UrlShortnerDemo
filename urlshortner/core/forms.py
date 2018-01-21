from django import forms


class UrlShortnerGetForm(forms.Form):
    offset = forms.IntegerField(initial=0, required=False)

class UrlShortnerGetUrl(forms.Form):
    id = forms.IntegerField()

class UrlShortnerCreateUrl(forms.Form):
    url = forms.CharField(max_length=500)