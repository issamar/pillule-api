from django.urls import path, include
from .views import Home, AddSale, UpdateSales, AddPil, AllPils, DeleteSale,GetSale

urlpatterns = [
    path('sales/', Home.as_view()),
    path('add-sale/', AddSale.as_view()),
    path('sales/<int:pk>', GetSale.as_view()),
    path('update/<int:pk>', UpdateSales.as_view()),
    path('add-pil/', AddPil.as_view()),
    path('pils/', AllPils.as_view()),
    path('del/<int:pk>', DeleteSale.as_view()),

]
