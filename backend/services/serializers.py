from rest_framework import serializers
from .models import *


class GhalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ghala
        fields = (
            'id', 'title', 'short_description', 'full_description',
            'contact','email', 'location','start_price', 'rent_price',
            'on_demand', 'space_available', 'image'
        )

class SokoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soko
        fields = (
            'id', 'commodity', 'last_price',
            'current_price', 'on_demand', 'image'
        )