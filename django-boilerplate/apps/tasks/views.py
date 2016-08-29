from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics
from rest_framework import serializers
from rest_framework import viewsets


from apps.tasks.models import Task
from apps.tasks.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
