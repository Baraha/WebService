from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Car
from .serializers import CarSerializer
# Create your views here.

def CarView(APIView):

    def get(self, request):
        cars = Car.objects
        serializer = CarSerializer(cars,many=True)
        return Response(serializer.data)
