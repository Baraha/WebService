from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from loguru import logger
from .models import Car
from .serializers import CarSerializer
from django.shortcuts import render

# Create your views here.


class CarView(APIView):

    def get(self, request):
        cars = Car.objects.all()
        serializer = CarSerializer(instance=cars, many=True)
        logger.debug(f"serializer LOGGER {serializer}")
        resp = Response(serializer.data)
        if Response(serializer.data)==None:
            return Response(status=400)
        return resp

    def post(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        else:
            return Response(status=400)


# class CarStatusFilter(APIView):
#
#     def get(self,status):
#         cars = Car.objects.get(status_active=status,draft=False)
#         serializer = CarSerializer(instance=cars, many=True)
#         resp = Response(serializer.data)
#         return resp
