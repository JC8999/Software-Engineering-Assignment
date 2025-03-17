from django.urls import path
from .api_views import LawyerListView, LawyerDetailView

urlpatterns = [
    path("", LawyerListView.as_view(), name="lawyer-list"),
    path("<int:pk>/", LawyerDetailView.as_view(), name="lawyer-detail"),
]