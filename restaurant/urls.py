from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Reservationviews.as_view(), name="create-reservations"),
    path('<str:ticket_number>', views.ReservationDetailViews.as_view(), name='detail-reservations'),
    path('menu/', views.MenuListCreatViews.as_view(), name='create-menu'),
    path('menu/<int:pk>/', views.MenuRetrieveUpdateDestroyView.as_view(), name='detail-menu'),
    path('image/', views.ImageViews.as_view(), name='image-views')
] 