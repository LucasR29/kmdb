from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from permissions.permissions import IsAdmOrCreation
from .models import User
from .serializers import UserSerializer


class UserView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdmOrCreation]
    queryset = User.objects.all()
    serializer_class = UserSerializer
