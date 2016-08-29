from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework import viewsets
# Create your views here.
from apps.trainers.models import Trainer
from apps.trainers.serializers import TrainerSerializer


class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
