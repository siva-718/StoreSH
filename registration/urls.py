from django.urls import path
from . import views

app_name = 'registration'

urlpatterns=[
  path('login/',views.login,name='login'),
  path('register/',views.register,name='register'),
  path('order/',views.order,name='order'),
  path('dashboard/', views.dashboard, name='dashboard'),


]