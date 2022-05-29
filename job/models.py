from operator import mod
from django.db import models

# Create your models here.

JOB_TYPES = (
    ('Full-Time','Full Time'),
    ('Part-Time','Part-Time')
)

class Job(models.Model):
    title = models.CharField(max_length=255,default=None,null=True)
    # location
    job_type = models.CharField(max_length=15,choices=JOB_TYPES,default='')
    description = models.TextField(max_length=1000,null=True)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.FloatField(default=10.0)
    # category
    experience = models.IntegerField(default=1)


    def __str__(self) -> str:
        return self.title