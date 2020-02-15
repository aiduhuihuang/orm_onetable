from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("addstudents/",addstudents),
    path("getstudents/",getstudents),
    path("updates/",updates)
]
