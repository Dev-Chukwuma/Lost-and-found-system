from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lost/', views.report_lost, name='report_lost'),
    path('found/', views.report_found, name='report_found'),
    path('lost-items/', views.lost_items, name='lost_items'),
    path('found-items/', views.found_items, name='found_items'),
    path('sucess/', views.sucess, name='sucess'),
    path('sucess2/', views.sucess2, name='sucess2'),
    path('post/<str:pk>', views.post, name='post'),
]
