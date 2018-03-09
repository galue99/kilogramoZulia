from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status, views
from .models import User, Company, Weight
from competitions.models import Competition, CompetitionType
from competitions import serializers as competitions_serializer
from accounts import serializers as accounts_serializers
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
import random, string
from django.db.models import Q

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

# Create your views here.
"""
obtain_auth_token = ObtainAuthToken.as_view(
    serializer_class=accounts_serializers.AuthTokenSerializer
)
"""
class WeightsViews(views.APIView):

    def get(self, request, *args, **kwargs):
        weights = Weight.objects.all()
        serializer = accounts_serializers.WeightSerializer(weights, many=True)

        return Response(serializer.data, status=200)

    def post(self, request, format=None):
        serializer = accounts_serializers.WeightSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WeightsDetailsViews(views.APIView):

    def get_object(self, pk):
        try:
            return Weight.objects.get(pk=pk)
        except Weight.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        account = self.get_object(pk)
        serializer = accounts_serializers.UserSerializer(account)
        return Response(serializer.data, status=200)

    def put(self, request, pk, format=None):
        account = self.get_object(pk)
        serializer = accounts_serializers.UserSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        account = self.get_object(pk)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LoginView(views.APIView):
    def post(self, request, *args, **kwargs ):
        if 'username' not in request.data or 'password' not in request.data:
            return Response("'username' and 'password' is needed", status=400)

        username = request.data['username']
        password = request.data['password']

        user = authenticate(username=username, password=password)

        if not user:
            return Response("'username' and 'password' incorrect", status=400)

        if not user.is_active:
            return Response("'username' and 'password' incorrect", status=400)

        token, created = Token.objects.get_or_create(user=user)

        value = User.objects.get(pk=user.id)
        serializer = accounts_serializers.UserSerializer(value)

        return Response({'token': token.key, 'user': serializer.data}, status=200)