__author__ = 'edgar'
from rest_framework import serializers
from accounts.models import User, Company, Rol, Weight
from django.contrib.auth.hashers import make_password
from django.utils.translation import ugettext_lazy as _

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (
            'id',
            'first_name',
            'last_name'
        )

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = (
            'id',
            'name',
        )

class UserSerializer(serializers.ModelSerializer):
    company     = CompanySerializer(read_only=True)
    company_id  = serializers.IntegerField(required=True)
    rol         = RolSerializer(read_only=True)
    rol_id      = serializers.IntegerField(required=True)
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'dni',
            'position',
            'branch_office',
            'rol',
            'rol_id',
            'company',
            'company_id',
        )
        extra_kwargs = {
            'password': {'read_only': True},
        }

class WeightSerializer(serializers.ModelSerializer):
    provider = CompanySerializer(read_only=True)
    provider_id  = serializers.IntegerField(required=True)
    user = UserSerializer(read_only=True)
    user_id  = serializers.IntegerField(required=True)
    class Meta:
        model = Weight
        fields = (
            'id',
            'weight1',
            'weight2',
            'weight3',
            'weight4',
            'weight5',
            'date',
            'time',
            'user',
            'user_id',
            'provider',
            'provider_id',
        )