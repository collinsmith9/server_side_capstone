"""astronomy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.db import router
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from astronomyserverapi.views import PostView, PostLikesView, PostCommentsView, CategoryView
from django.conf.urls import include
from astronomyserverapi.views.auth import login_user, register_user
from astronomyserverapi.views.event_comments import EventCommentsView
from astronomyserverapi.views.event_likes import EventLikesView
from astronomyserverapi.views.event_types import EventTypeView
from astronomyserverapi.views import FollowView
from astronomyserverapi.views.events import EventView
from astronomyserverapi.views.site_user import UserView

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'posts', PostView, 'post')
router.register(r'postlikes', PostLikesView, 'postlikes')
router.register(r'postcomments', PostCommentsView, 'postcomments')
router.register(r'categories', CategoryView, 'categories')
router.register(r'events', EventView, 'events')
router.register(r'eventcomments', EventCommentsView, 'eventcomments')
router.register(r'eventlikes', EventLikesView, 'eventlikes')
router.register(r'eventtypes', EventTypeView, 'eventtypes')
router.register(r'users', UserView, 'users')
router.register(r'follows', FollowView, 'follows')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
