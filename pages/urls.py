from django.urls import path
from .views import (
    create,
    electronics,
    sale_detail,
    transport,
    transport_detail,
    furniture,
    furniture_detail,
    clothes,
    clothes_detail,
    sport,
    sport_detail,
    home,
    sale_delete,
    sale_update,
)

urlpatterns = [
    path('', home, name='home'),
    path('create/', create, name='create'),
    path('electronics/', electronics, name='electronics'),
    path('electronics/<pk>/delete', sale_delete, name='sale_delete'),
    path('electronics/<pk>/update', sale_update, name='sale_update'),
    path('electronics/<pk>/', sale_detail, name='sale_detail'),
    path('transport/', transport, name='transport'),
    path('transport/<pk>/', transport_detail, name='transport_detail'),
    path('furniture/', furniture, name='furniture'),
    path('furniture/<pk>/', furniture_detail, name='furniture_detail'),
    path('clothes/', clothes, name='clothes'),
    path('clothes/<pk>/', clothes_detail, name='clothes_detail'),
    path('sport/', sport, name='sport'),
    path('sport/<pk>/', sport_detail, name='sport_detail'),
]