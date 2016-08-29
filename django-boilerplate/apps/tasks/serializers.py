from rest_framework import serializers

from apps.tasks.models import Task
from apps.exercises.serializers import ExerciseMiniSerializer
from apps.clients.serializers import ClientMiniSerializer


class TaskSerializer(serializers.ModelSerializer):
    exercise = ExerciseMiniSerializer()
    client = ClientMiniSerializer()

    class Meta:

        model = Task
        fields = ['date', 'count', 'comment', 'client', 'exercise', 'index']
