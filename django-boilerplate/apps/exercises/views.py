from django.shortcuts import render

from rest_framework import serializers
from rest_framework import generics
from rest_framework import viewsets

from apps.exercises.models import Exercise
from apps.exercises.serializers import ExerciseSerializer
# Create your views here.


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


exercise_list = ExerciseViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

exercise_detail = ExerciseViewSet.as_view({
    'get': 'list',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
