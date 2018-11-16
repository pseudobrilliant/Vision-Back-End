# snippets/serializers
from rest_framework import serializers
from .models import VisionUser


class VisionUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = VisionUser
        fields = ('user', 'left', 'right', 'center')