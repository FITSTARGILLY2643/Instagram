from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    url(r'',include('maxigram.urls')),
    url(r'^accounts/', include('django_registration.backends.one_step.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^logout/$', views.logout, {"next_page": '/'},name='logout')
]