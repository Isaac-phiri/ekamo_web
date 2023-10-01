 
# serializers.py
from rest_framework import serializers
from .models import User, AgentType, AgentProfile
from transactions.models import FispTransaction

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('ID_TYPE','ROLE','id_front', 'id_back','code','email','first_name',
        'last_name','phone','dob','idtype','idNo','province','district', 
        'is_staff','is_verified' )  # Adjust fields as needed


class AgentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentType
        fields = ('commission', 'salary', 'title','timestamp', 'updated')

class AgentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentProfile
        fields = ('floatLimit','first_name','last_name','code','phonenumber','agent_type','idtype','idNo','id_front','id_back','dob','province','district','timestamp','updated')


class FispTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FispTransaction
        fields = ('id','transAdt','numberOfFarmers','isSuccess','transAmount','totalCommis','transCommisAgent','transOldBalance','transNewBalance',
                  'transNewComBalance','transOldComBalance','timestamp','updated','agent')