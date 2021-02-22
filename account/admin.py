from account.models import BusinessUser, CustomerUser
from django.contrib import admin

# Register your models here.
admin.site.register(CustomerUser)
admin.site.register(BusinessUser)