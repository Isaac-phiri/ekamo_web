# # from django.shortcuts import render,get_object_or_404,redirect
# # from django.contrib import messages
# from .serializers import UserSerializer
# from rest_framework import permissions
# from rest_framework import viewsets
# from  .models import User
# import json
# from django.views.generic import ListView , DetailView ,TemplateView
# # from django.views.generic.edit import CreateView, DeleteView, UpdateView

# from .models import Category
# from .forms import ReviewForm

from re import X
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .models import User, AgentProfile, AgentType
from .serializers import CustomUserSerializer, AgentTypeSerializer,AgentProfileSerializer
from rest_framework.decorators import action
from rest_framework import viewsets

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer

class AgentTypeViewSet(viewsets.ModelViewSet):
    queryset = AgentType.objects.all()
    serializer_class = AgentTypeSerializer

class AgentProfileViewSet(viewsets.ModelViewSet):
    queryset = AgentProfile.objects.all()
    serializer_class = AgentProfileSerializer