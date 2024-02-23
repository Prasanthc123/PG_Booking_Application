from app.models import *
from django import forms


class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        help_texts={'username':''}
        widgets={'password':forms.PasswordInput}

        
class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['address','profile_pic']


class pgform(forms.ModelForm):
    class Meta():
        model=Pgs
        fields='__all__'