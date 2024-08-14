from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=40);
    age = models.IntegerField();
    job_description = models.CharField(max_length=20);
    education = models.CharField(max_length=20);
    marital_status = models.CharField(max_length=20);