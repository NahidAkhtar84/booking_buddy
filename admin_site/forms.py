from django import forms


class BlogPostForm(forms.Form):
    title = forms.CharField(max_length=255)
    category = forms.CharField()
    details = forms.CharField()
    image = forms.FileField()
