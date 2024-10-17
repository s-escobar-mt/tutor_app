from django.contrib.auth.models import AbstractUser
from django.db import models

class Schedules(models.Model):
    # Holds the time tutors are available
    start_time = models.DateTimeField(null=False, blank=False)
    end_time = models.DateTimeField(null=False, blank=False)

class Subjects(models.Model): 
    # each subject level combination will have a numeric primary key auto gened
    subject = models.CharField(null=False, blank=False,max_length=5)
    level = models.PositiveIntegerField(null =False, blank=False)

class CustomUser(AbstractUser):
    # Each user can opt to add from the subjects or time schedules
    subjects = models.ManyToManyField(Subjects)
    schedule = models.ManyToManyField(Schedules)

