from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework import genrics
from rest_framework.response import Response
from rest_framework import viewsets

from apps.feeds.models import Feed
from apps.feeds.serializers import FeedSerializer


class FeedViewSet(viewsets.ModelViewset):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
