from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('index.html', views.index, name="index"),
    path('register.html', views.register, name="register"),
    path('handleRegister', views.handleRegister, name="handleRegister"),
    path('secScr', views.secScr, name="secScr"),
    path('handlesecScr', views.handlesecScr, name="handlesecScr"),
    path('handleLogin', views.handleLogin, name="handleLogin"),
]
