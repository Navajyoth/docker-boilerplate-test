from rest_framework import serializers
from .models import Trainer
from apps.clients.models import Client



class TrainerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trainer

class TrainerMiniSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ['trainer']
