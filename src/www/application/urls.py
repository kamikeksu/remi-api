from django.conf.urls import include, url
from helpers import debug_views

urlpatterns =  [
    url(r'^user/',                   include('application.modules.user.urls')),
]
