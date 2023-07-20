from rest_framework import serializers
from .models import *

class GhalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ghala
        fields = '__all__'

class SokoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soko
        fields = '__all__'