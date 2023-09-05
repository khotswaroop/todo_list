from django import forms
from .models import Todo,ExtendUser

class TodoForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields='__all__'

class ExtendUserForm(forms.ModelForm):
    class Meta:
        model=ExtendUser
        fields=['username','password']

class TokenForm(forms.ModelForm):
    class Meta:
        model=ExtendUser
        fields='__all__'
