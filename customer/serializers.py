from rest_framework import serializers
from customer.models import*

class GetCustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Customers
        fields="__all__"
        
class GetCustomerAddressSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=CustomerAddress 
        fields="__all__"
 
        
class CustomerDetailAddressSerializer(serializers.ModelSerializer):
    Customer_Adresses= GetCustomerAddressSerializer(Many=True)
    
    class Meta:
        Model= Customers
        fields=('first_name','last_number','mobile','address','age','country','city','dob')
        
   
    