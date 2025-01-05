from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user_list'),  # URL pattern for listing users
    path('<int:pk>/', views.user_detail, name='user_detail'),  # URL pattern for user details
    path('create/', views.user_create, name='user_create'),  # URL pattern for creating a new user
    path('<int:pk>/update/', views.user_update, name='user_update'),  # URL pattern for updating an existing user
    path('<int:pk>/delete/', views.user_delete, name='user_delete'),  # URL pattern for deleting a user
]
