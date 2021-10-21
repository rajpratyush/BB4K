"""bb4k_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from bb4kApp_backend.views import homepage_view, kid_register_view, parent_register_view, kid_app_view, parent_app_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage_view, name='homepage'),
    path('KidsRegister', kid_register_view, name='register kids'),
    path('ParentsRegister', parent_register_view, name='register parents'),
    path('kids', kid_app_view, name='kid view'),
    path('parents', parent_app_view, name='parent view'),
    
]
