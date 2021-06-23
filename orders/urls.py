from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.apiOverview, name="orders-overview"),
    path('pizza-create/', views.pizzacreateandview, name='pizza-create'),
    path('pizza-list/', views.pizzaList, name="pizza-list"),
    path('pizza-detail/<str:pk>/', views.pizzaDetail, name="pizza-Detail"),
    url(r'^filter/$', views.search, name='search'),
    path('new/', views.index, name='form'),
]
