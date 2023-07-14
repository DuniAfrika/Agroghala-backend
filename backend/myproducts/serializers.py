from rest_framework import serializers
from .models import *
from services.serializers import *

class MyghalaSerializer(serializers.ModelSerializer):
    ghala = GhalaSerializer(read_only=True)

    class Meta:
        model = Myghala
        fields = '__all__'

class MysokoSerializer(serializers.ModelSerializer):
    soko = SokoSerializer(read_only=True)

    class Meta:
        model = Mysoko
        fields = '__all__'