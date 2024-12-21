from django.urls import path
from . import views

urlpatterns = [
    path('', views.board_list, name='board-list'),
    path('<int:board_id>/', views.board_detail, name='board-detail'),
]