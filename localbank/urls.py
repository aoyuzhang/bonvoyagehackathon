from django.urls import path
from . import views

urlpatterns = [
    path('', views.localbank_index, name='localbank_index'),
    path('bankitems/', views.BankitemListView.as_view(), name = 'bankitems'),
    path('bankitem/<int:pk>',views.BankitemDetailView.as_view(), name='bankitem-detail'),
    path('myitems/', views.BankitemsownedByUserListView.as_view(), name='my-items'),
]