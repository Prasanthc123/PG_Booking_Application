from app.models import *
from django import forms



class pgform(forms.ModelForm):
    class Meta():
        model=Pgs
        fields='__all__'