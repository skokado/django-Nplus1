"""django_project URL Configuration

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
from django.urls import path, include

from django_project import settings
from app import views


urlpatterns = [
    path('good/', views.GoodView.as_view(), name='good'),
    path('bad/', views.BadView.as_view(), name='bad'),
    path('many-to-many-good/', views.ManyToManyGoodView.as_view(), name='many-to-many-good'),
    path('many-to-many-bad/', views.ManyToManyBadView.as_view(), name='many-to-many-bad'),
    path('admin/', admin.site.urls),
    path('', views.Home.as_view(), name='home'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('debug', include(debug_toolbar.urls)),
    ]
