from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='mlmodel_index'),
    # path('mlmodels/', views.mlmodelhome, name='mlhome'),
    # path('mlmodels/fakenews/',views.fakenews, name='fakenews'),
    # path('mlmodels/fakenews/result/', views.fakenewsresult, name="fakenewsresult"),
    path('fakenews/',views.fakenews, name='fakenews'),
    path('fakenews/result/', views.fakenewsresult, name="fakenewsresult"),
]