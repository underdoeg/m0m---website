from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    date = models.DateTimeField(blank=False)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User)
    
class Attachment(models.Model):
    event = models.ForeignKey(Event)
    description = models.TextField(blank = True)
    file = models.FileField(upload_to="uploads")