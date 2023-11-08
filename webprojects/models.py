
from django.db import models
class Client(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    contact = models.CharField(max_length=15)
    email = models.EmailField(max_length=200)
    address = models.CharField(max_length=20)
    product = models.CharField(max_length=30)
    size = models.CharField(max_length=15)

    PAYMENT_OPTIONS =[
        ("MM","mobilemoney"),
        ("VC","visacard"),
        ("CD","cashondelievery")
  
    ]
    payment_opts = models.CharField(max_length=15, choices=PAYMENT_OPTIONS)

class category (models.Model):
     
       category_id= models.IntegerField

class Product (models.Model):
     product_id = models.IntegerField
     category_id = models.ForeignKey(category,on_delete= models.CASCADE)
     product_name = models.CharField(max_length=30)
     unit_price = models.IntegerField
     sale_price = models.IntegerField
     available_stock = models.IntegerField
     unit_measure = models.CharField(max_length=35)
     date_updated = models.DateField

class Transaction (models.Model):
     transaction_id = models.IntegerField
     Product_id = models.ForeignKey(Product,on_delete= models.CASCADE)
     transaction_type = models.CharField(max_length=25)
     stock_taken = models.IntegerField
     transaction_amount = models.IntegerField
     transaction_date = models.DateField

    
