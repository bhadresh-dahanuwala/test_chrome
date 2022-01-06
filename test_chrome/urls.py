
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', include('test_app.urls')),
    path('admin/', admin.site.urls),
]
