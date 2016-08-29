from django.conf.urls import patterns, url

from rest_framework.routers import DefaultRouter

from apps.trainers import views


router = DefaultRouter()
router.register(r'trainers', views.TrainerViewSet)
urlpatterns = router.urls
