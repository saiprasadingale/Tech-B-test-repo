from .models import Usermodel
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usermodel
        fields = '__all__'