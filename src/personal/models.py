from django.db import models

import datetime



class Contactus(models.Model):
    email                       = models.EmailField(verbose_name="email", max_length=60,blank=False)  
    phonenumber                 = models.BigIntegerField(verbose_name="phonenumber")  
    message                     = models.TextField(max_length=450,unique=False,blank=False) 
    date_sent                   = models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return self.email
    

class Aja(models.Model):
    email                       = models.EmailField(verbose_name="email", max_length=60,blank=False)  
    phonenumber                 = models.BigIntegerField(verbose_name="phonenumber" ,blank=False)  

    def __str__(self):
        return self.email










    