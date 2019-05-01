from django.conf.urls import url
from users import views

urlpatterns = [
    url(r'^hello/$', views.user_list),
    url(r'^hello/(?P<name>[a-zA-Z]+)/$', views.user_detail)
]
