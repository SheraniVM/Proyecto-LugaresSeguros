from django.contrib.auth.models import User   
from rest_framework import serializers

class RegisterUserSerializer(serializers.Serializer):
    #No estará basado en un modelo
    username = serializers.CharField(max_length=50)    
    password = serializers.CharField(max_length=50)

    #El método create del serializador permite crear la información como tal y va a recibir la información validada para poderlo crear
    #Objects va a permitir por medio del user manager crear los objetos
    
    def create(self, validated_data):
        try:
            user = User.objects.create_user(**validated_data)
        except:
            raise serializers.ValidationError({"error":"Usuario con este username ya existe. "})
        return user 

class LoginUserSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=50)    
    password = serializers.CharField(max_length=50)


        
