from django.db import models

# Create your models here.
class Customers(models.Model):
    first_name=models.CharField(max_length=15,null=True,blank=True)
    last_name=models.CharField(max_length=15,null=True,blank=True)
    mobile=models.IntegerField(null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    country=models.CharField(max_length=15,null=True,blank=True)
    city=models.CharField(max_length=15,null=True,blank=True)
    dob=models.DateField(max_length=15,null=True,blank=True)
    
    def __str__(self):
        return self.first_name
 #Create your models here.
class CustomerAddress(models.Model):
      Customers=models.ForeignKey(Customers,on_delete=models.CASCADE,null=True,related_name="Customer_Addresses")
      street_name=models.CharField(max_length=15,null=True,blank=True)
      street_number=models.IntegerField(null=True,blank=True)
      state=models.CharField(max_length=15,null=True,blank=True)
      country=models.CharField(max_length=15,null=True,blank=True)
      city=models.CharField(max_length=15,null=True,blank=True)
      pincode=models.IntegerField(null=True,blank=True)  
      
      def __str__(self):
        return str(self.street_name)
      
   
class Customer_Addhar(models.Model):
      Customers=models.OneToOneField(Customers,on_delete=models.CASCADE)
      addhar_name=models.CharField(max_length=15,null=True,blank=True)
      addhar_no=models.IntegerField(null=True,blank=True)
      
      def __str__(self):
        return str(self.addhar_name)

     