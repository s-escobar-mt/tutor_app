from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.db.models import F

class Schedule(models.Model):
    # Holds the time and coressponding days tutors are available
    start_time = models.TimeField(null=False, blank=False)
    end_time = models.TimeField(null=False, blank=False)
    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(end_time__gte=F('start_time')),
                name='end_time_greater_than_start_time'
            )
        ]
    day = models.CharField(null=True, blank=False,max_length=9)
    def __str__(self): 
        s= f'{self.day} | {self.start_time} - {self.end_time}\n'
        return s

class Subject(models.Model): 
    # each subject level combination will have a numeric primary key auto gened
    subject = models.CharField(null=False, blank=False,max_length=5)
    level = models.PositiveIntegerField(null =False, blank=False)
    def __str__(self):
        return f'{self.subject} {self.level}'

class CustomUser(AbstractUser):
    # Each user can opt to add from the subjects or time schedules
    name = models.CharField(max_length=60,null=True,blank=True)
    subjects = models.ManyToManyField(Subject, blank=True)
    schedule = models.ManyToManyField(Schedule, blank=True)
    def __str__(self):
        return self.username
    def get_absolute_url(self): # new
        return reverse("tutor_detail", kwargs={"pk": self.pk})
