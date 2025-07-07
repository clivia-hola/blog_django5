from django.urls import path
from . import views
app_name='authory'
urlpatterns = [
    path('login/',views.wmlogin,name='wmlogin'),
    path('logout/',views.wmlogout,name='wmlogout'),
    path('register/',views.register,name='register'),
    path('emailcode',views.email_code,name='emailcode'),
]