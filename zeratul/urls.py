"""zeratul URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home, name='home'),
    url(r'^maps/$', views.maps, name='maps'),
    url(r'^map/(?P<slug>[\w-]+)/$', views.map_detail, name='map_detail'),
    url(r'^players/$', views.players, name='players'),
    url(r'^player/(?P<name>[\w-]+)/$', views.player_detail, name='player_detail'),
    url(r'^games/$', views.games, name='games'),
    url(r'^game/(?P<id>[0-9]+)/$', views.game_detail, name='game_detail'),
]
