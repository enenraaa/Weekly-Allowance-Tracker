from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_week/', views.create_week, name='create_week'),
    path('edit_week/<int:week_id>/', views.edit_week, name='edit_week'),
    path('delete_week/<int:week_id>/', views.delete_week, name='delete_week'),
]
