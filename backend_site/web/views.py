from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
import logging
from .models import Car
from .serializers import CarSerializer
from django.shortcuts import render

# Create your views here.

logger = logging.getLogger(__name__)

class CarView(APIView):

    def get(self, request):
        cars = Car.objects.all()
        serializer = CarSerializer(instance=cars,many=True)
        resp = Response(serializer.data)
        if Response(serializer.data)==None:
            resp = {"status" : "none"}
        return resp
