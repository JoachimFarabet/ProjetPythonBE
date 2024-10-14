from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Auteur
from .serializers import AuteurSerializer

class AuteurViewSet(viewsets.ModelViewSet):
    queryset = Auteur.objects.all()
    serializer_class = AuteurSerializer
