
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.table,name='table'),
    path('homepage/', views.homepage,name='homepage'),
    path('form/', views.form,name='form')

]
