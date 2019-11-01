from django import forms
from .models import Author

class AuthorAdd (forms.Form):
    name = forms.CharField(max_length=50)
    bio = forms.CharField(widget=forms.Textarea)


class RecipeAdd (forms.Form):
    title = forms.CharField(max_length=50)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(widget=forms.Textarea) 
    instructions = forms.CharField(widget=forms.Textarea)
    reqtime = forms.CharField(widget=forms.Textarea)
    
