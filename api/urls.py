from django.urls import path
from .views import RoomView

app_name = 'api'

urlpatterns = [
    path('room', RoomView.as_view()),
   
]