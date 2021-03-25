from django import forms


class AboutForm(forms.Form):
    title = forms.CharField(max_length=255)
    mobile = forms.CharField()
    details = forms.CharField()
    image = forms.FileField()
    cpy = forms.CharField()


class SocialLinkForm(forms.Form):
    name = forms.CharField()
    link = forms.CharField()
