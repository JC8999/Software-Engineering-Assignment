from rest_framework import generics, permissions
from .models import LawyerProfile
from .serializers import LawyerSerializer

class LawyerListView(generics.ListCreateAPIView):
    """
    API endpoint that allows users to view all lawyers.
    """
    queryset = LawyerProfile.objects.all()
    serializer_class = LawyerSerializer
    permission_classes = [permissions.AllowAny]

class LawyerDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows admin users to edit and delete lawyer profiles.
    """
    queryset = LawyerProfile.objects.all()
    serializer_class = LawyerSerializer
    permission_classes = [permissions.IsAdminUser]
