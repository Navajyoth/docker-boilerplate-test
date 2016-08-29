from rest_framework import serializers

from apps.exercises.models import Exercise


class ExerciseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exercise


class ExerciseMiniSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exercise
        fields = ['id', 'name', 'type']
