from rest_framework import serializers


# userserializer
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        exclude = []

