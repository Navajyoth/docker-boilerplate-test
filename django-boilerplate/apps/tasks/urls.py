from django.conf.urls import patterns, url
from apps.tasks.views import TaskViewSet
from rest_framework.routers import DefaultRouter

from apps.tasks import views

router = DefaultRouter()
router.register(r'tasks', views.TaskViewSet)


urlpatterns = router.urls
