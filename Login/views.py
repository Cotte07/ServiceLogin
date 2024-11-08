from django.contrib.auth import  authenticate
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

# Create your views here.

class Login(viewsets.ViewSet):
    def login(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username= username, password= password)
        if user is not None:
            token, created = Token.objects.get_or_create(user = user)
            return Response({"exito": "logueado", "token": token.key})
        else:
             return Response({"error": " no logueado"})