from django.urls import path

from . import views

urlpatterns = [
    # Get API calls
    path('getTables/', views.getTables, name='get-tables'),
    path('getTable/<str:pk>/', views.getTable, name='get-table'),
    path('getSubjects/<str:pk>/', views.getSubjects, name='get-subjects'),
    path('getWeeks/<str:pk>/', views.getWeeks, name='get-weeks'),
    path('getNodes/<str:pk>/', views.getNodes, name='get-nodes'),

    # Create API calls
    path('createTable/', views.createTable, name='create-table'),
    path('createSubject/<str:pk>/', views.createSubject, name="create-subject"),
    path('createWeek/<str:pk>/', views.createWeek, name='create-week'),
    
    # Update API calls
    path('updateTable/<str:pk>/', views.updateTable, name='update-table'),
    path('updateSubject/<str:pk>/', views.updateSubject, name='update-subject'),
    path('updateNode/<str:pk>/', views.updateNode, name='update-node'),
    
    # Delete API calls
    path('deleteTable/<str:pk>/', views.deleteTable, name="delete-table"),
    path('deleteSubject/<str:pk>/', views.deleteSubject, name="delete-subject"),
    path('deleteWeek/<str:pk>/', views.deleteWeek, name="delete-week"),
]