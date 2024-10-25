from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm, TextInput, NumberInput
from .models import CustomUser, Schedule, Subject

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username","email","subjects")
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email","subjects","schedule","name")

class ScheduleForm(ModelForm):
    class Meta:
        model = Schedule
        fields = ("start_time","end_time","day")

class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields =("subject", "level")

class AddSubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ['subject', 'level']
        widgets = {
            'subject': TextInput(attrs={'maxlength': 4}),  # Limit to 4 characters
            'level': NumberInput(attrs={'min': 100, 'max': 999}),  # Limit to 3-digit integer
        }