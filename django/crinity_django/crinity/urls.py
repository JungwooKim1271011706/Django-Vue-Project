# mysite에서 include하여 urls.py를 참고할 수 있음

from django.urls import path
from . import views

urlpatterns = [
    path('', views.crinity, name='crinity_testdata'),
    path('testdata', views.getTestData, name='crinity_gettestdata'),
    path('moleg', views.crinity_moleg, name='crinity_moleg'),

]
