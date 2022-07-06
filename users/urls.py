from django.conf.urls import url 
from . import views 
 
urlpatterns = [ 
    url(r'^api/users/$', views.users),
    url(r'^api/user/(?P<user_id>[0-9]+)$', views.user),
]