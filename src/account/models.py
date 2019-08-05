from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager



# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username,firstname,lastname,phonenumber, address, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")
        if not firstname:
            raise ValueError("Users must have a firstname")
        if not lastname:
            raise ValueError("Users must have a lastname")
        if not address:
            raise ValueError("Users must have a address")
        if not phonenumber:
            raise ValueError("Users must have a address")


        
        user = self.model(
               email = self.normalize_email(email),
               username=username,
               firstname=firstname,
               lastname=lastname,
               address=address,
               phonenumber=phonenumber,

            )

        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, username,firstname,lastname, phonenumber,  address,password):
        user = self.create_user(
               email=self.normalize_email(email),
               password=password, 
               username=username,
               firstname=firstname,
               lastname=lastname,
               address=address,
               phonenumber=phonenumber,
            )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    email                   = models.EmailField(verbose_name="email", max_length=60,unique=True,blank=False)  
    firstname               = models.CharField(verbose_name="firstname", max_length=250,unique=False) 
    lastname                = models.CharField(verbose_name="lastname", max_length=250,unique=False)  
    address                 = models.CharField(verbose_name="address", max_length=250,unique=False) 
    phonenumber             = models.CharField(verbose_name="phonenumber", max_length=11,unique=True)  
    username                = models.CharField(max_length=30,unique=True)
    date_joined             = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_joined             = models.DateTimeField(verbose_name='last joined', auto_now=True)
    is_admin                = models.BooleanField(default=False)
    is_active               = models.BooleanField(default=True)
    is_staff                = models.BooleanField(default=False)
    is_superuser            = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','firstname','lastname','address','phonenumber',]

    objects=MyAccountManager()

    def __str__(self):
        return self.email 

    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
