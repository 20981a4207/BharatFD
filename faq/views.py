# faq/views.py

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from .models import FAQ
from .serializers import FAQSerializer

# Home View (renders a simple home page)
def home(request):
    return HttpResponse("Welcome to the FAQ API!")  # Simple text message

# FAQ ViewSet for handling API requests
class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()  # Retrieves all FAQ objects
    serializer_class = FAQSerializer  # Specifies the serializer for the FAQ model
