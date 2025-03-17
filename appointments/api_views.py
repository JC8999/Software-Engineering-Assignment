from rest_framework import generics, permissions
from .models import Appointment
from .serializers import AppointmentSerializer

class AppointmentListView(generics.ListCreateAPIView):
    """
    API endpoint that allows authenticated users to view and create appointments.
    """
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

class AppointmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows client users to view, edit, and delete appointments.
    """
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]
