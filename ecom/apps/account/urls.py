from django.conf.urls import url
from . import views

urlpatterns = [
    # post views
    url(r'^login/$', views.user_login, name='login'),
    url(r'^signup/$', views.user_signup,name='signup'),
    # login / logout urls
    # url(r'^login/$',
    #     'django.contrib.auth.views.login',
    #     name='login'),
    # url(r'^logout/$',
    #     'django.contrib.auth.views.logout',
    #     name='logout'),
    # url(r'^logout-then-login/$',
    #     'django.contrib.auth.views.logout_then_login',
    #     name='logout_then_login'),
]
