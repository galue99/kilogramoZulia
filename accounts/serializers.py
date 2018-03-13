__author__ = 'edgar'
from rest_framework import serializers
from accounts.models import User, Company, Weight, Tara
from django.contrib.auth.hashers import make_password
from django.utils.translation import ugettext_lazy as _

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (
            'id',
            'name',
            'rif'
        )

class TaraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tara
        fields = (
            'id',
            'name',
            'peso'
        )

class UserSerializer(serializers.ModelSerializer):
    company     = CompanySerializer(read_only=True)
    company_id  = serializers.IntegerField(required=True)

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
            'company',
            'company_id',
        )
        extra_kwargs = {
            'password': {'read_only': True},
        }

class WeightSerializer(serializers.ModelSerializer):
    provider = CompanySerializer(read_only=True)
    provider_id = serializers.IntegerField(required=True)
    user = UserSerializer(read_only=True)
    user_id  = serializers.IntegerField(required=True)
    tara = TaraSerializer(read_only=True)
    tara_id  = serializers.IntegerField(required=True)
    code = serializers.SerializerMethodField()
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
            'code',
            'provider',
            'provider_id',
            'tara',
            'tara_id',
        )

    def get_code(self, obj):
        obj.incrementar()
        return obj.code