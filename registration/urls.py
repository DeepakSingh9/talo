from django.conf.urls import url
from . import views

urlpatterns=[url(r'^signup/$',views.registration,name='registration'),
             url(r'^login/$',views.auth_login,name='login'),
             ]
