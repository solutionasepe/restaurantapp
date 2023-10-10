from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Reservationviews.as_view(), name="create-reservations"),
    path('<str:ticket_number>/', views.ReservationDetailViews.as_view(), name='detail-reservations')
] 