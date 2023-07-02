from django.urls import re_path as url
from . import views

app_name = 'homepage'

urlpatterns = [
    url(r'^$', views.login_view, name="login"),
    url(r'^compose/$', views.compose_view, name="compose"),
    url(r'^inbox/$', views.inbox_view, name="inbox"),
    
    url(r'^options/$', views.options_view, name="options")
   
]
