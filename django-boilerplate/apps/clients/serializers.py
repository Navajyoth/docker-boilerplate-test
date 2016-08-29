from rest_framework import serializers
from apps.tasks.models import Task
from .models import Client  # Feed


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client


class ClientMiniSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name']

class ClientGoalSerializer(serializers.ModelSerializer):


    class Meta:
        model = Client
        fields = ['goal_weight','goal_achieved','sit_more_than_30hrs_per_week']

class ClientMedicalSerializer(serializers.ModelSerializer):


    class Meta:
        model = Client
        fields = ['time_of_injury','medical_remarks']


# class ClientMiniSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Client
#         fields


