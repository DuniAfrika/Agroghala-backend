import datetime
from rest_framework import generics
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from services.models import *
from .serializers import *


class MyghalaView(generics.CreateAPIView):
    queryset = Myghala.objects.all()
    serializer_class = MyghalaSerializer
    def get(self, request):
        myghalas = Myghala.objects.all()
        output = []

        for myghala in myghalas:
            if myghala.ghala in output:
                amount = myghala.amount_paid_new
            else:
                amount = myghala.amount_paid
            details = {
                "id": myghala.id,
                "ghala": myghala.ghala.title,
                "bags_stored": myghala.bags_stored,
                "duration_of_storage": myghala.duration_of_storage,
                "amount_paid": amount,
                "rented_on": myghala.rented_on
            }

            output.append(details)

        return Response(output)


    def post(self, request):
        user = request.farmer
        try:
            ghala_id = request.data.get('ghala_id')
            ghala = Ghala.objects.get(pk=ghala_id)
            rental = Myghala(ghala=ghala, sold_on=datetime.datetime.now())
            rental.user = user

            rental.save()

            return Response({'message':'ghala rented successfully', 'rental': serializer.data})
        except Ghala.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class MySokoView(generics.CreateAPIView):
    queryset = Mysoko.objects.all()
    serializer_class = MysokoSerializer
    def get(self, request):
        mysokos = Mysoko.objects.all()
        output = []

        for mysoko in mysokos:
            details = {
                "id": mysoko.id,
                "commodity": mysoko.soko.commodity,
                "bags_sold": mysoko.bags_sold,
                "amount_accredited": mysoko.amount_accredited,
                "sold_on": mysoko.sold_on,
            }

            output.append(details)

        return Response(output)


    def post(self, request):
        user = request.farmer
        try:
            soko_id = request.data.get('soko_id')
            soko = Soko.objects.get(pk=soko_id)
            sell = Mysoko(soko=soko, sold_on=datetime.datetime.now())
            sell.user = user

            sell.save()

            serializer = MysokoSerializer(sell)
            return Response(serializer.data)
        except Soko.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

