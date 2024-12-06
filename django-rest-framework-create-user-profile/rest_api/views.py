from django.shortcuts import render

from .serializers import UserSerializer
from django.contrib.auth.models import User 
from .models import Profiles , Profiles
from rest_framework import generics ,viewsets, views



class UserSerializerViewSets(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()



