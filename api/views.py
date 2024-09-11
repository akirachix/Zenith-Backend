from django.shortcuts import render
from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from drainagesystem.models import DrainageSystem
from .serializers import DrainageSystemSerializer
from rest_framework.views import APIView


class DrainageSystemList(generics.ListCreateAPIView):
    queryset = DrainageSystem.objects.all()
    serializer_class = DrainageSystemSerializer
    def get (self, request):
        serializer = DrainageSystemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class DrainageSystemDetail(APIView):
      def post(self, request, *args, **kwargs):
        serializer = DrainageSystemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
