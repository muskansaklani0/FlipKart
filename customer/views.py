from django.shortcuts import render
from customer.models import*
from customer.serializers import*
# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
# Create your views here.
class GetCustomerView(APIView):
    def get(self,request):
        instance=Customers.objects.all()
        serializers=GetCustomerSerializer(instance,many=True)
        return Response(serializers.data)
        
        # Create your views here.
class GetCustomerSerializers(APIView):
    def get(self,request):
        params=request.data
        print("data",params)
        serializers=GetCustomerSerializer(data=params)
        serializers.is_valid(FalseException=True)
        return Response(serializers.data)
        
        
        
        # Create your views here.
class GetCustomerSerializers(APIView):
    def get(self,request):
        instance=Customers.objects.all()
        serializers=GetCustomerSerializer(instance,many=True)
        return Response(serializers.data)
   
   
     # Create your views here.
class CustomerDetailAddressView(APIView):
    def get(self,request,pk):
        instance=Customers.objects.filter(pk)
        scr=CustomerDetailAddressSerializer(instance,many=True)
        return Response(scr.data)
   