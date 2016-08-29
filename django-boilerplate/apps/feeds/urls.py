from django.conf.urls import patterns, url
from apps.feeds.views import FeedViewSet
from rest_framework.routers import DefaultRouter

from apps.feeds import views

router = DefaultRouter()
router.register(r'feeds', views.FeedViewSet)

urlpatterns = patterns('',
                       )
urlpatterns += router.urls
