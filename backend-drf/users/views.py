from django.shortcuts import render
from rest_framework.response import Response
from .serializers import UserRegisterSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #------------ Password should not be showed to frontend as showing all content------
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            #------------ So we have to modify Password field in Serializer.py
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ProfileView(APIView): # this profile should be private , bacause anyone can;t see your profile
    permission_classes = [IsAuthenticated] # it is also a class

    def get(self, request):
        serializer = UserSerializer(request.user) #-----> this .user giving me permission class, when you logged in then only it gives user
        return Response(serializer.data)