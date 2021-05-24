"""studentmanagementsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path

from studentmanagementsystem import settings
from sms import views as sms_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/', sms_view.showDemoPage, name='demo'),
    path('', sms_view.showLoginPage),
    path('get_user_details', sms_view.GetUserDetails),
    path('logout_user', sms_view.logout_user),
    path('doLogin/', sms_view.doLogin),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
