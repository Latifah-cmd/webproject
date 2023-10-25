from django.db import models
class Client(models.Model):
    #PAYMENT_OPTIONS =[
     #   ("MM","mobilemoney")
      #  ("VC","visacard")
       # ("CD","cashondelievery")
  
    #]
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    contact = models.CharField(max_length=15)
    email = models.EmailField(max_length=200)
    address = models.CharField(max_length=20)
    product = models.CharField(max_length=30)
    size = models.CharField(max_length=15)
    #payment_opts = models.CharField(max_length=15, choices=PAYMENT_OPTIONS)


    class Order(models.Model):
         product_name = models.CharField(max_length=30)
         product_color = models.CharField(max_length=30)
         order_date = models.DateTimeField(auto_now=True)
         delievery_date = models.DateTimeField(auto_now=True)
        # size = models.ForeignKey(Client, on_delete= models.CASCADE)



    
