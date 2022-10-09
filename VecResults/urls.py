"""VecResults URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('I_Year/', include('I_Year.urls')),
    path('II_Year/', include('II_Year.urls')),
    path('III_Year/', include('III_Year.urls')),
    path('IV_Year/', include('IV_Year.urls')),
]


admin.site.site_header = "VEC Results Administration"
admin.site.site_title = "Results"
admin.site.index_title = "VEC Admin"
