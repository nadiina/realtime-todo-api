from django import forms
from .models import Task, AppInfo, Profile

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'is_completed']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class AppInfoForm(forms.ModelForm):
    class Meta:
        model = AppInfo
        fields = '__all__'

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'