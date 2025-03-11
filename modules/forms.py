from django import forms
from .models import Module

class AddModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['name', 'version', 'repository', 'description']

class UpdateModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['name', 'version', 'repository', 'description']