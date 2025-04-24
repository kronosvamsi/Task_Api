from django.db import models

# Create your models here.

class Tasks(models.Model):
    choices=[("running","running"),("completed","completed")]
    id=models.IntegerField(primary_key=True,unique=True)
    name=models.CharField(max_length=500,unique=True)
    description=models.TextField(max_length=1000)
    created_at=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=500,choices=choices)