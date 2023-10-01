# forms.py
from django import forms
from .models import AgentProfile

class AgentProfileForm(forms.ModelForm):
    class Meta:
        model = AgentProfile
        fields = '__all__'
