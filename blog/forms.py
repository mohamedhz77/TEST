from django import forms

class SearchForm(forms.Form):
       query = forms.CharField()

class EmailPostForm(forms.Form):
       name = forms.CharField(max_length=25)
       email = forms.EmailField()
       to = forms.EmailField()
       comments = forms.CharField(required = False, widget = forms.Textarea)
       
class ContactForm(forms.Form):
       name = forms.CharField(max_length=20)
       email = forms.EmailField()
       message = forms.CharField(widget= forms.Textarea)       