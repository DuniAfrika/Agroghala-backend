from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import generics


class GhalaView(generics.CreateAPIView):
    queryset = Ghala.objects.all()
    serializer_class = GhalaSerializer
    def get(self, request):
        ghalas = Ghala.objects.all()
        output = []

        for ghala in ghalas:
            ghala_data = {
                "title": ghala.title,
                "short_description": ghala.short_description,
                "full_description": ghala.full_description,
                "contact": ghala.contact,
                "email": ghala.email,
                "location": ghala.location,
                "start_price": ghala.start_price,
                "rent_price": ghala.rent_price,
                "on_demand": ghala.on_demand,
                "space_available": ghala.space_available
            }
            output.append(ghala_data)

        return Response(output)


    def post(self, request):
        serializer = GhalaSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

class SokoView(generics.CreateAPIView):
    queryset = Soko.objects.all()
    serializer_class = SokoSerializer
    def get(self, request):
        sokos = Soko.objects.all()
        output = []

        for soko in sokos:
            soko_data = {
                "commodity": soko.commodity,
                "last_price": soko.last_price,
                "current_price": soko.current_price,
                "on_demand": soko.on_demand,
                "image": soko.image,
            }
            output.append(soko_data)

        return Response(output)

    def post(self, request):
        serializer = SokoSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response(serializer.data)
