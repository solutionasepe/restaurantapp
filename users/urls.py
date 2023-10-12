from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.userview.as_view(), name="user-name"),
    path("<str:username>/", views.userDetailsView.as_view(), name='user-details')
]