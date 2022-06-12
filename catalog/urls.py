from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='catalog_index'),
    path('books/', views.BookListView.as_view(), name='books'),
]