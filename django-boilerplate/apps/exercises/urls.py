from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter

from apps.exercises import views

router = DefaultRouter()
router.register(r'exercises', views.ExerciseViewSet)

urlpatterns = router.urls
