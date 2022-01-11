from rest_framework import viewsets, permissions
from .serialazers import CustomUserSerializer
from .models import CustomUser


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAdminUser]
