from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True) #-------------not models.CharField----
    
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password']


    def create(self, validated_data):
        # user = User.objects.create_user(
        #     validated_data['id'],
        #     validated_data['email'],
        #     validated_data['username'],
        #     validated_data['password']
        # ) -------------------------insteed of that we can use this
        user = User.objects.create_user(**validated_data) # ** means that whichever data is coming just took it and create an user

        return user
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password']
        # read_only_fields = ['id', 'email']

