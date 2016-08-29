from rest_framework import serializers
from .models import Feed
from apps.clients.serializers import ClientMiniSerializer


class FeedSerializer(serializers.ModelSerializer):
    client = ClientMiniSerializer()

    class Meta:
        model = Feed
        Fields = ['client', 'datetime', 'message']
