from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.urls.base import reverse

# Create your models here.

class BusinessUser(models.Model):
    bus_user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=254)
    address1 = models.CharField(max_length=254)
    address2 = models.CharField(max_length=254, blank=True)
    city = models.CharField(max_length=254)
    state = models.CharField(max_length=2)
    zip_code = models.PositiveIntegerField()
    about = models.TextField(max_length=9999, blank=True)
    # services_provided = models.ManyToManyField(ServicesProvided, blank=True)
    yr_est = models.CharField(max_length=4, null=True, blank=True)
    profile_pic = models.ImageField(blank=True)
    the_slug = models.SlugField(unique=True, null=True)
    
    def __str__(self):
        return str(self.bus_user)
    
    def save(self, *args, **kwargs):
        self.the_slug = slugify(self.business_name + ' ' + self.city)
        super(BusinessUser, self).save(*args, **kwargs)
    
    

class CustomerUser(models.Model):
    cust_user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    address1 = models.CharField(max_length=254)
    address2 = models.CharField(max_length=254, blank=True)
    city = models.CharField(max_length=254)
    state = models.CharField(max_length=2)
    zip_code = models.PositiveIntegerField()

    def __str__(self):
        return str(self.cust_user) 
    
    