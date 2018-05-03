from django.urls import path
from . import views

app_name = "mform"
urlpatterns = [
    path('', views.index, name='index'),
    path('form1/', views.form1, name='form1')
]