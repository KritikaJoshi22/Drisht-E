from django.contrib import admin
from django.urls import re_path as url, include

urlpatterns = [
    url(r'^admin/$', admin.site.urls),
    url(r'^',include('homepage.urls')),
    
]
