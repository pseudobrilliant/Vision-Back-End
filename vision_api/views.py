from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.views import APIView
from .models import VisionUser
from .serializers import VisionUserSerializer
from django.http import JsonResponse

class VisionUserExists(APIView):

    def get(self, request, *args, **kwargs):
        # use this if username is in url kwargs
        username = self.kwargs.get('user')

        # use this if username is being sent as a query parameter
        username = self.request.query_params.get('user')

        try:
            print(username)
            user = VisionUser.objects.get(user=username) # retrieve the user using username
        except VisionUser.DoesNotExist:
            return JsonResponse({'message':False}) # return false as user does not exist
        else:
            return JsonResponse({'message':True}) # Otherwise, return True


class VisionUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = VisionUser.objects.all()
    serializer_class = VisionUserSerializer

