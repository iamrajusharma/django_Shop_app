from django.db import models
import datetime
from django.utils.timezone import now

# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=50,)
    email=models.EmailField(max_length=20)
    phone=models.CharField(max_length=12)
    password=models.CharField(max_length=500)
    Role=models.CharField(default="Custumer",max_length=8)

    def __str__(self):
     return self.name

class catagry(models.Model):
   name=models.CharField(max_length=20,default=1)    
   def __str__(self):
     return self.name


class product(models.Model):
    product_name=models.CharField(max_length=50)  
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    Catagry=models.ForeignKey(catagry, null=True, on_delete=models.SET_NULL)
    description = models.CharField(max_length=255, default='Default description')
    image = models.ImageField(upload_to='product/', blank=True, null=True)    
    def __str__(self):
     return self.product_name


class order(models.Model):
  product=models.ForeignKey(product,on_delete=models.CASCADE)
  user=models.ForeignKey(user,on_delete=models.CASCADE)
  quantity=models.IntegerField(default=1)
  price=models.IntegerField()
  address=models.CharField(max_length=50,default='',blank=True)
  phone=models.CharField(max_length=50,default='',blank=True)
  date=models.DateField(default=datetime.datetime.today) 
  user_name = models.CharField(max_length=100, default='')
  cart = models.JSONField(null=True, blank=True)

  def __str__(self):
        return f"Order {self.id} by {self.user_name}"
  
  