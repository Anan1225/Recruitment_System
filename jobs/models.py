from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
# 使用列表
JobTypes = [
    (0, "Technical"),
    (1, "Product"),
    (2, "Operations"),
    (3, "Design")
]

Cities = [
    (0, "Beijing"),
    (1, "Shanghai"),
    (2, "Shenzhen"),
    (3, "Hangzhou"),
    (4, 'Guangzhou')
]

class Job(models.Model):
    job_type = models.SmallIntegerField(blank=False, choices=JobTypes, verbose_name="JOB type")
    job_name = models.CharField(max_length=250, blank=False, verbose_name="JOB name")
    job_city = models.SmallIntegerField(blank=False, choices=Cities, verbose_name="JOB City")
    jobs_reponsibility = models.TextField(max_length=1024, verbose_name="JOB Reponsibility")
    job_requirement = models.TextField(max_length=1024, verbose_name="JOB Requirement")
    # 使用外键引用
    creator = models.ForeignKey(User, verbose_name="Creator", null=True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(verbose_name="Created Date", default=datetime.now)
    modified_date = models.DateTimeField(verbose_name="Modified Date", default=datetime.now)