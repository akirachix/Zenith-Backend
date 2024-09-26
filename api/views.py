from django.shortcuts import render
import logging
from rest_framework import status,generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.hashers import make_password
from user.models import User
from .serializers import UserSerializer, RoleSerializer
from django.contrib.auth import authenticate
from rest_framework import viewsets
from datamonitoring.models import MonitoringData
from .serializers import MonitoringDataSerializer
from drainagesystem.models import DrainageSystem
from .serializers import DrainageSystemSerializer
from .serializers import DeviceSerializer
from sensor.models import Sensor
from .serializers import SensorSerializer
from notification.models import Notification
from .serializers import NotificationSerializer


logger = logging.getLogger(__name__)


class UserListView(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserDetailView(APIView):
    def get(self, request, id):
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response(
                {"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = UserSerializer(user)
        logger.info(f"User with ID {id} retrieved successfully.")
        return Response(serializer.data)

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            serializer.validated_data["password"] = make_password(
                serializer.validated_data["password"]
            )

            user = serializer.save()
            logger.info(f"User registered successfully: {user.email}")
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        logger.error(f"User registration failed: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response(
                {"error": "Email and password are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            logger.info(f"Login attempt for non-existent user: {email}")
            return Response(
                {"error": "User does not exist", "signup_required": True},
                status=status.HTTP_404_NOT_FOUND,
            )

        django_user = authenticate(username=email, password=password)
        if django_user:
            logger.info(f"User logged in successfully: {email}")
            return Response({}, status=status.HTTP_200_OK)

        logger.error(f"Login failed for user: {email}")
        return Response(
            {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )


class RoleBasedView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request):
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            user_id = serializer.validated_data["user_id"]
            new_role = serializer.validated_data["role"]

            try:
                user = User.objects.get(id=user_id)
                user.role = new_role
                user.save()
                logger.info(f"Role updated for user {user.email}: {new_role}")
                return Response(
                    {"detail": f"Role updated to {new_role} for user successfully"},
                    status=status.HTTP_200_OK,
                )
            except User.DoesNotExist:
                logger.error(f"User with ID {user_id} not found")
                return Response(
                    {"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND
                )
        else:
            logger.error(f"Invalid role update data: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MonitoringDataViewSet(viewsets.ModelViewSet):
    queryset = MonitoringData.objects.all()
    serializer_class = MonitoringDataSerializer

    
class DrainageSystemList(APIView):
    def get(self, request):
        drainagesystems = DrainageSystem.objects.all()  
        serializer = DrainageSystemSerializer(drainagesystems, many=True)  
        return Response(serializer.data)


class DrainageSystemList(generics.ListCreateAPIView):
    queryset = DrainageSystem.objects.all()
    serializer_class = DrainageSystemSerializer

    def get(self, request, *args, **kwargs):
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


class SensorListCreateView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        serializer = SensorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        return Response({})


class SensorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def get(self, request, id):
        sensor = self.get_object()
        serializer = SensorSerializer(sensor)
        return Response(serializer.data)

    def put(self, request, id):
        sensor = self.get_object()
        serializer = SensorSerializer(sensor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        sensor = self.get_object()
        sensor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

