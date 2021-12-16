from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

from django.utils.translation import gettext_lazy as _
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
# 候选人学历
DEGREE_TYPE = ((u'本科', u'本科'), (u'硕士', u'硕士'), (u'博士', u'博士'))

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


class Resume(models.Model):
    # Translators: 简历实体的翻译
    username = models.CharField(max_length=135, verbose_name=_('姓名'))
    applicant = models.ForeignKey(User, verbose_name=_("申请人"), null=True, on_delete=models.SET_NULL)
    city = models.CharField(max_length=135, verbose_name=_('城市'))
    phone = models.CharField(max_length=135, verbose_name=_('手机号码'))
    email = models.EmailField(max_length=135, blank=True, verbose_name=_('邮箱'))
    apply_position = models.CharField(max_length=135, blank=True, verbose_name=_('应聘职位'))
    born_address = models.CharField(max_length=135, blank=True, verbose_name=_('生源地'))
    gender = models.CharField(max_length=135, blank=True, verbose_name=_('性别'))
    picture = models.ImageField(upload_to='images/', blank=True, verbose_name=_('个人照片'))
    attachment = models.FileField(upload_to='file/', blank=True, verbose_name=_('简历附件'))

    # 学校与学历信息
    bachelor_school = models.CharField(max_length=135, blank=True, verbose_name=_('本科学校'))
    master_school = models.CharField(max_length=135, blank=True, verbose_name=_('研究生学校'))
    doctor_school = models.CharField(max_length=135, blank=True, verbose_name=u'博士生学校')
    major = models.CharField(max_length=135, blank=True, verbose_name=_('专业'))
    degree = models.CharField(max_length=135, choices=DEGREE_TYPE, blank=True, verbose_name=_('学历'))
    created_date = models.DateTimeField(verbose_name="创建日期", default=datetime.now)
    modified_date = models.DateTimeField(verbose_name="修改日期", auto_now=True)

    # 候选人自我介绍，工作经历，项目经历
    candidate_introduction = models.TextField(max_length=1024, blank=True, verbose_name=u'自我介绍')
    work_experience = models.TextField(max_length=1024, blank=True, verbose_name=u'工作经历')
    project_experience = models.TextField(max_length=1024, blank=True, verbose_name=u'项目经历')

    class Meta:
        verbose_name = _('简历')
        verbose_name_plural = _('简历列表')

    def __str__(self):
        return self.username