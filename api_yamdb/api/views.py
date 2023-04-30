from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView

class TokenView(APIView):
    pass


class UserRegView(APIView):
    pass

class UsersViewSet(viewsets.ModelViewSet):
    pass