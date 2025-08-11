from rest_framework import serializers
from .models import Student
from django.contrib.auth.models import User

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'


    def to_representation(self, instance):
        data=super().to_representation(instance)
        data['message']='This is the message added in the json'

        return data
                            
    def create(self,validated_data):

        password=validated_data.pop('password')
        user=User(**validated_data)
        user.set_password('Moise74659')
        user.save()
                                
        return  user
    


    
