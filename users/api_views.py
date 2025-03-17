from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

User = get_user_model()

class UserListView(generics.ListAPIView):
    """
    API endpoint that allows admin users to view all registered users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser] 

class UserDetailView(generics.RetrieveAPIView):
    """
    API endpoint that allows users to view their own profile details.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
