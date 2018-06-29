from .import views
from django.conf.urls import url,include 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
app_name='dpyApp'

urlpatterns = [
    url(r'^$', views.home),
    url(r'^home/$', views.home),
    url(r'^login/$', views.login),
    url(r'^signup/$', views.signup),
    url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
    url(r'^ajax/insert_user/$', views.insert_user, name='insert_user'),
    url(r'^update_user/$', views.update_user, name='update_user'),
    url(r'^validate_login/', views.validate_login, name='validate_login'),
    url(r'^logout/', views.logout, name='logout'),
]

urlpatterns += staticfiles_urlpatterns()