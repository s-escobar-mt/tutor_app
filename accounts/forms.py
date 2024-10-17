from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from .models import CustomUser, Schedules, Subjects

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username","email",)
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email","subjects","schedule",)

class AddSchedule(ModelForm):
    class Meta:
        model = Schedules
        fields = ("start_time","end_time")

class AddSubject(ModelForm):
    class Meta:
        model = Subjects
        fields =("subject", "level")