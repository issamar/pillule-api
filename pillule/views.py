from django.shortcuts import render
from rest_framework import generics
from .models import SalesDetails, PilsDetail
from .serializers import SalesDetailsSerializer, PilsdetailSerializer

# Create your views here.


class Home (generics.ListAPIView):
    queryset = SalesDetails.objects.all()
    serializer_class = SalesDetailsSerializer


class AddSale(generics.CreateAPIView):
    serializer_class = SalesDetailsSerializer

class GetSale(generics.RetrieveAPIView):
    queryset = SalesDetails.objects.all()
    serializer_class = SalesDetailsSerializer
    
class UpdateSales(generics.RetrieveUpdateDestroyAPIView):
    queryset = SalesDetails.objects.all()
    serializer_class = SalesDetailsSerializer


class DeleteSale(generics.DestroyAPIView):
    queryset = SalesDetails.objects.all()
    serializer_class = SalesDetailsSerializer


class AddPil(generics.CreateAPIView):
    serializer_class = PilsdetailSerializer


class AllPils(generics.ListAPIView):
    queryset = PilsDetail.objects.all()
    serializer_class = PilsdetailSerializer
