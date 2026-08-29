from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list_create, name='item-list-create'),
    path('<uuid:pk>', views.item_detail, name='item-detail'),
    path('<str:pk>', views.item_detail, name='item-detail-str'),
]
