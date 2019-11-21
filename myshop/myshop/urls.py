"""myshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from garments.views import index,aboutus,formal_shirts,casual_shirts,t_shirts,contactus,trousers,thankyou,cart

urlpatterns = [
    path('',index),
    path('admin/', admin.site.urls),
    path('about',aboutus),
    path('contact',contactus),
    path('formal_shirts',formal_shirts),
    path('casual_shirts',casual_shirts),
    path('t_shirts',t_shirts),
    path('trousers',trousers),
    path('thankyou',thankyou),
    path('cart<int:x>',cart),
    ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
