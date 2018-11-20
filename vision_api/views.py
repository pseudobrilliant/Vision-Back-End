from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.views import APIView
from .models import VisionUser
from .serializers import VisionUserSerializer
from django.http import JsonResponse, Http404
from rest_framework.response import Response
from rest_framework import status

class VisionUserExists(APIView):

    def get(self, request, *args, **kwargs):

        # use this if username is being sent as a query parameter
        username = self.request.query_params.get('user')

        try:
            print(username)
            user = VisionUser.objects.get(user=username) # retrieve the user using username
        except VisionUser.DoesNotExist:
            return JsonResponse({'message':False}) # return false as user does not exist
        else:
            return JsonResponse({'message':True}) # Otherwise, return True

class AllVisionUsers(APIView):

    def get(self, request, format=None):

        users = VisionUser.objects.all()

        serializer = VisionUserSerializer(users, many=True)

        return Response(serializer.data)

class VisionUsers(APIView):

    def get_object(self, usr):
        try:
            return VisionUser.objects.get(user=usr)
        except VisionUser.DoesNotExist:
            raise Http404

    def get(self, request, usr, format=None):

        user = self.get_object(usr)
        serializer = VisionUserSerializer(user)
        return Response(serializer.data)

    def post(self, request, format=None):

        serializer = VisionUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
