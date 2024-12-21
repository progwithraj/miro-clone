# backend/urls.py
from django.urls import path, include

urlpatterns = [
    path('boards/', include('boards.urls')),  # Example API endpoint
    path('users/', include('users.urls')),  # Example user management endpoint
    path('collab/', include('collaboration.urls')),  # WebSocket endpoint for collaboration
]
