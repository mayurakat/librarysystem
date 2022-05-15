from Book import views
from django.urls import path

urlpatterns = [
    path('upload/',views.upload_file,name='upload'),
    ]