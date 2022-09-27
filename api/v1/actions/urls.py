from django.urls import path
from api.v1.actions import views

urlpatterns = [
    path('', views.actions),
    path('<str:pk>/', views.actions_read),
    path('create/', views.actions_post),
    path('update/<str:pk>', views.actions_update),
    path('delete/<str:pk>', views.actions_delete),
]