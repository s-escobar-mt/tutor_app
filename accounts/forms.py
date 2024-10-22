from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from .models import CustomUser, Schedule, Subject

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username","email","subjects")
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email","subjects","schedule","name")

class AddSchedule(ModelForm):
    class Meta:
        model = Schedule
        fields = ("start_time","end_time","day")

class AddSubject(ModelForm):
    class Meta:
        model = Subject
        fields =("subject", "level")