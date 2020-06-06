from django.conf.urls import url

from . import views


urlpatterns = [

    url(r"^$",views.index),
    url(r"^(\d+)/$",views.detail),
    url(r"^schools/$",views.schools),
    url(r"^students/$",views.students),
    url(r"^grades/$",views.grades),
    url(r"^plans/$",views.plans),
    url(r'^schools/(\d+)$',views.schoolsgrade),
    url(r'^grades/(\d+)$',views.gradesstudent),
    url(r'^students/(\d+)$',views.studentsplan),
    url(r'^plans/(\d+)$',views.plans)

]