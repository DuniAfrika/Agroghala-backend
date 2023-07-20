from rest_framework import serializers
from .models import *

class MyGhalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyGhala
        fields = '__all__'

class MySokoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MySoko
        fields = '__all__'