"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.contrib.auth import views as auth_views
from core.views import root_page
from rest_framework import routers
from rest_framework.authtoken import views as rest_authtoken_views
from core.api.v1.views import LikeViewSet, UserViewSet
from post.api.v1.views import PostViewSet
from event.api.v1.views import EventReadOnlyViewSet

router = routers.DefaultRouter()
router.register(r'likes', LikeViewSet)
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'events', EventReadOnlyViewSet)

urlpatterns = [
    url(r'^$', root_page),

    url(r'^api/v1/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^social/', include('social_django.urls', namespace='social')),
    url(r'^api-token-auth/', rest_authtoken_views.obtain_auth_token)
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
