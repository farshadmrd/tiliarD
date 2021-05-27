from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # @action(detail=False, methods=["POST"], url_path="sign-up")
    # def signup(self, request):
    #     data = request.data
    #     User.object.create(**data)
    #     return Response({"message": "User created successfully"})