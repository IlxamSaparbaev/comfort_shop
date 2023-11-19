from django.urls import path
from .views import (
    ProductList,
    ProductDetail,
    ProductPost,
    ProductPut,
    ProductDelete
)

urlpatterns = [
    path('product/list/', ProductList.as_view()),
    path('product/<int:pk>/', ProductDetail.as_view()),
    path('product/create/', ProductPost.as_view()),
    path('product/update/<int:pk>/', ProductPut.as_view()),
    path('product/delete/<int:pk>/', ProductDelete.as_view())
]