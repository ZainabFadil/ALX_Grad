from django.urls import path
from .views import meal_list, meal_detail, meal_create, meal_update, meal_delete

urlpatterns = [
    path('', meal_list, name='meal_list'),
    path('<int:pk>/', meal_detail, name='meal_detail'),
    path('new/', meal_create, name='meal_create'),
    path('<int:pk>/edit/', meal_update, name='meal_update'),
    path('<int:pk>/delete/', meal_delete, name='meal_delete'),
]