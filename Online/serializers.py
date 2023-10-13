from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import *

#Serializer to Get User Details using Django Token Authentication
#class StudentSerializer(serializers.ModelSerializer):
  #class Meta:
    #model = Student
    #fields = "__all__"

#Serializer to Register User
#class StudentRegisterSerializer(serializers.ModelSerializer):
  #email = serializers.EmailField(
    #required=True,
    #validators=[UniqueValidator(queryset=Student.objects.all())]
 # )
  #password = serializers.CharField(
   # write_only=True, required=True, validators=[validate_password])
  #password2 = serializers.CharField(write_only=True, required=True)
  #class Meta:
   # model = Student
   # fields = ('username', 'password', 'password2',
  #       'email', 'first_name', 'last_name','reg_no','gender')
    #extra_kwargs = {
     # 'first_name': {'required': True},
     # 'last_name': {'required': True}
   # }
  #def validate(self, attrs):
  #  if attrs['password'] != attrs['password2']:
  #    raise serializers.ValidationError(
  #      {"password": "Password fields didn't match."})
  #  return attrs
 # def create(self, validated_data):
 #   user = Student.objects.create(
   #   username=validated_data['username'],
   #   email=validated_data['email'],
   #   first_name=validated_data['first_name'],
   #   last_name=validated_data['last_name'],
  #    reg_no=validated_data['reg_no']
  #  )
  #  user.set_password(validated_data['password'])
  #  user.save()
  #  return user

#class LecturerSerializer(serializers.ModelSerializer):
  #class Meta:
   # model = Lecturer
   # fields = "__all__"

#Serializer to Register User


    


class SassSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    options = serializers.HyperlinkedRelatedField(
    view_name='student-detail',
    lookup_field = 'proposal_name',
    many=True,
    read_only=True)

    class Meta:
        model = SassProposal
        fields = '__all__'
        lookup_field = 'proposal_name'
        extra_kwargs = {
            'url': {'lookup_field': 'proposal_name'}
        }

class SonasSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    options = serializers.HyperlinkedRelatedField(
    view_name='student-detail',
    lookup_field = 'proposal_name',
    many=True,
    read_only=True)

    class Meta:
        model = SonasProposal
        fields = '__all__'
        lookup_field = 'proposal_name'
        extra_kwargs = {
            'url': {'lookup_field': 'proposal_name'}
        }