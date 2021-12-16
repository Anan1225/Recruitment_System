from django.conf.urls import url
from django.urls import path
from jobs import views

urlpatterns = [
    # 职位列表
    path(r"^joblist/", views.joblist, name="joblist"),
    url(r"^job/(?P<job_id>\d+)/$", views.detail, name="detail"),
    url(r"^$", views.joblist, name="name"),
]