from rest_framework import serializers
from django.contrib.auth.models import User
from django.http import JsonResponse



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65, min_length=6, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=4)
    first_name = serializers.CharField(max_length=255, min_length=2)
    last_name = serializers.CharField(max_length=255, min_length=2)
    class Meta:
        model = User
        fields = [ 'username', 'first_name', 'last_name', 'email', 'password']

        def validate(self, attrs):
            email = attrs.get('email', '') 
            token = jwt.encode(payload, 'secret_key', algorithm='HS256').decode('utf-8')
            if User.objects.filter(email=email).exists():
                raise serializers.ValidationError({'email': ('Email is already in use')})
            return super().validate(attrs).JsonResponse({'token': token})
        
        def create(self, validated_data):
            return User.objects.create_user(**validated_data)
     
