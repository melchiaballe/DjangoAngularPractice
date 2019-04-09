from django.shortcuts import render
from .models import User
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import UserSerializer


# Create your views here.
class UserViewSet(viewsets.ViewSet):
    def list_user(self, request, **kwargs):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status=200)