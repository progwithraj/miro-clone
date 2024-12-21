from django.urls import path
from . import views

urlpatterns = [
    path('', views.collab_list, name='collab-list'),
    path('<int:collab_id>/', views.collab_detail, name='collab-detail'),
]