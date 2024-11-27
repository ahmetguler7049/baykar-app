from django.urls import path
from .views import AircraftInventoryCreateListView, PartInventoryCreateListDeleteView, team_dashboard

urlpatterns = [
    path('create-aircraft-inventory/', AircraftInventoryCreateListView.as_view(), name='create-aircraft-inventory'),
    path('list-aircraft-inventory/', AircraftInventoryCreateListView.as_view(), name='list-aircraft-inventory'),

    path('create-part-inventory/', PartInventoryCreateListDeleteView.as_view(), name='create-part-inventory'),
    path('list-part-inventory/', PartInventoryCreateListDeleteView.as_view(), name='list-part-inventory'),
    path('delete-part-inventory/<int:part_id>/', PartInventoryCreateListDeleteView.as_view(),
         name='delete-part-inventory'),
    path('team-dashboard/', team_dashboard, name='team_dashboard'),
]
