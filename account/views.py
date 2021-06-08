from django.shortcuts import render
from .forms import NewUserForm, CustomerForm, BusinessForm
from django.http import request, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def customer_register(request):
    
    registered = False
    if request.method == 'POST':
        user_form = NewUserForm(data=request.POST)
        customer_form = CustomerForm(data=request.POST)

        if user_form.is_valid() and customer_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            customer_user = customer_form.save(commit=False)
            customer_user.cust_user = user
            

            customer_user.save()
            registered = True
            
            
        else:
            print(user_form.errors,customer_form.errors)

    else:
        user_form = NewUserForm()
        customer_form = CustomerForm()  

    context = {
        'user_form':user_form,
        'customer_form':customer_form,
        'registered':registered
    } 

    return render(request,'account/customer_register.html',context=context) 

def business_register(request):
    
    registered = False
    if request.method == 'POST':
        user_form = NewUserForm(data=request.POST)
        business_form = BusinessForm(data=request.POST)

        if user_form.is_valid() and business_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            business_user = business_form.save(commit=False)
            business_user.bus_user = user
            

            business_user.save()
            registered = True
            
            
        else:
            print(user_form.errors,business_form.errors)

    else:
        user_form = NewUserForm()
        business_form = BusinessForm()  

    context = {
        'user_form':user_form,
        'business_form':business_form,
        'registered':registered
    } 

    return render(request,'account/business_register.html',context=context) 

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))

            else: 
                return HttpResponse('Account is not active!')
        
        else:
            print('someone tried to login unsuccessfully!')
            return HttpResponse('Username or Password does not match our records. Please try again.')

    else:
        return render(request, 'account/user_login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))