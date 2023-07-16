from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response


class FarmerView(APIView):
    def get(self, request):
        farmers = Farmer.objects.all()
        output = []
        for farmer in farmers:
           farmer_data = {
                    "first_name": farmer.first_name,
                    "last_name": farmer.last_name,
                    "email": farmer.email,
                    "phone": farmer.phone,
                    "location": farmer.location,
                    "date_joined": farmer.date_joined,
                    "is_active": farmer.is_active,
                    "is_staff": farmer.is_staff,
               }
           output.append(farmer_data)
        return Response(output)

    def post(self, request):
        serializer = FarmerSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response(serializer.data)
