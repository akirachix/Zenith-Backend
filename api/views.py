

from django.shortcuts import render
# Create your views here.
import logging
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.hashers import make_password
from user.models import User
from .serializers import UserSerializer,RoleSerializer
import logging
from django.contrib.auth import authenticate
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
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        logger.info(f'User with ID {id} retrieved successfully.')
        return Response(serializer.data)




logger = logging.getLogger(__name__)

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = serializer.save()
                logger.info(f'User registered successfully: {user.email}')
                return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
            except Exception as e:
                logger.error(f'User registration failed: {str(e)}')
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        logger.error(f'User registration failed: {serializer.errors}')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from user.models import User
from .serializers import UserSerializer
import logging

logger = logging.getLogger(__name__)

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        if not email or not password:
            return Response({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            logger.info(f'Login attempt for non-existent user: {email}')
            return Response({
                'error': 'User does not exist',
                'signup_required': True
            }, status=status.HTTP_404_NOT_FOUND)
        
        django_user = authenticate(username=email, password=password)
        if django_user:
            token, _ = Token.objects.get_or_create(user=django_user)
            user_data = UserSerializer(user).data
            response_data = {
                'token': token.key,
                'user': user_data
            }
            logger.info(f'User logged in successfully: {email}')
            return Response({'message':'Login successful'})
        
        logger.error(f'Login failed for user: {email}')
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
class RoleBasedView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    def post(self, request):
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            user_id = serializer.validated_data['user_id']
            new_role = serializer.validated_data['role']
            try:
                user = User.objects.get(id=user_id)
                user.role = new_role
                user.save()
                logger.info(f'Role updated for user {user.email}: {new_role}')
                return Response({"detail": f"Role updated to {new_role} for user successfully"}, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                logger.error(f'User with ID {user_id} not found')
                return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            logger.error(f'Invalid role update data: {serializer.errors}')
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)