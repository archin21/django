from django.conf.urls import url
from app_5_g import views
app_name='app'
urlpatterns=[
    url(r'^registeration/$',views.fun2,name='registeration'),
    url(r'^login/$',views.user_login,name='login'),
]
