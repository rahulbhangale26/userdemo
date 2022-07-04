from django.conf.urls import url 
from . import views 
 
urlpatterns = [ 
    url(r'^api/pull_users/(?P<user_counts>[0-9]+)$', views.pull_users),
]