"""app URL Configuration

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
from django.conf.urls import url, include
from todo.apis import HealthCheckAPI, TodoViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HealthCheckAPI.as_view(), name='healthcheck'),
    url(r'^todo/$', TodoViewSet.as_view({ 'get': 'list', 'post': 'create' }), name='list'),
    url(r'^todo/(?P<pk>[0-9]+)/$', TodoViewSet.as_view({ 'patch': 'partial_update', 'delete': 'destroy' }), name='snippet-detail'),
]
