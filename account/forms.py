import builtins
from account.models import CustomerUser
from django import forms
from django.contrib.auth.models import User
from .models import BusinessUser, CustomerUser

class CustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerUser    
        fields = ('address1','address2','city','state','zip_code',)

class BusinessForm(forms.ModelForm):
    class Meta:
        model = BusinessUser
        fields = ('business_name','address1', 'address2', 'city', 'state', 'zip_code', 'about', 'yr_est', 'profile_pic', 'the_slug',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["the_slug"].label = "https://autowiz.com/yourURL"

class NewUserForm(forms.ModelForm):
    password = forms.CharField(
        widget = forms.PasswordInput()
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    class Meta():
        model = User
        fields = ('username','email','password') 
