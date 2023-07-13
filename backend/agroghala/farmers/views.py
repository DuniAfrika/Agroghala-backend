from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import JsonResponse


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
                   "location": farmer.location
               }
           output.append(farmer_data)
        return Response(output)

    def post(self, request):
        serializer = FarmerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

def register_farmer(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return JsonResponse({'message': f'Welcome {username}'})
        else:
            return JsonResponse({'errors': form.errors}, status=400)