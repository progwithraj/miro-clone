from django.urls import path
from . import views

urlpatterns = [
    path('', views.users_list, name='users-list'),
    path('<int:users_id>/', views.users_detail, name='users-detail'),
]