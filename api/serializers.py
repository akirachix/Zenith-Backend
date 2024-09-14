from rest_framework import serializers
from user .models import User , ROLE_CHOICES
from django.contrib.auth.models import User as DjangoUser
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'email', 'role', 'password']
        read_only_fields = ['id']

    def create(self, validated_data):
        django_user = DjangoUser.objects.create_user(
            username=validated_data['email'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        user = User.objects.create(
            user=django_user,
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number=validated_data['phone_number'],
            email=validated_data['email'],
            role=validated_data['role']
        )
        return user
class RoleSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    # role = serializers.ChoiceField(choices=User.ROLE_CHOICES)