from django.contrib import admin
from django.urls import path,include
from customer.views import*
urlpatterns = [
         path('get-customer',GetCustomerView. as_view()),
         path('get-Address',GetCustomerView. as_view()),
    
]
