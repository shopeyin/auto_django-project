from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate,logout

from account.forms import RegistrationForm,AccountAuthenticateForm,AccountUpdateForm
from cars.models import Cars







def registration_view(request):
    

        context = {}
        if request.POST:
            form=RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                email           = form.cleaned_data.get('email')
                username        = form.cleaned_data.get('username')
                firstname       = form.cleaned_data.get('firstname')
                lastname        = form.cleaned_data.get('lastname')
                address         = form.cleaned_data.get('lastname')
                phonenumber     = form.cleaned_data.get('lastname')
                raw_password    = form.cleaned_data.get('password1')
                account = authenticate(email=email,password=raw_password)
                login(request,account)
                return redirect('home')
            else:
                context['registration_form'] = form
        else: #GET request
            form = RegistrationForm()
            context['registration_form'] = form
        return render(request, 'account/register.html', context)



def logout_view(request):
    logout(request)
    return redirect('home')




def login_view(request):

    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('home')

    if request.POST:
        form = AccountAuthenticateForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email,password=password)

            if user:
                login(request, user)
                return redirect('home')
    else:
        form = AccountAuthenticateForm()

    context['login_form'] = form
    return render(request, 'account/login.html',context) 






def account_view(request):

    if not request.user.is_authenticated:
        return redirect("login")

    context = {}

    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.initial = {
                "email"         : request.POST['email'],
                "username"      : request.POST['username'],
                "address"       : request.POST['address'],
                "phonenumber"   : request.POST['phonenumber'],
            }
            form.save()
            context['success_message']='updated'

    else:
        form = AccountUpdateForm(
                initial={
                    "email"         : request.user.email,
                    "username"      : request.user.username,
                    "address"       : request.user.address,
                    "phonenumber"   : request.user.phonenumber,

                }
        )


    context['account_form'] = form

    cars = Cars.objects.filter(seller=request.user)
    context['cars']= cars

    return render(request, 'account/account.html', context)



def must_authenticate_view(request):
    return render(request, 'account/must_authenticate.html',{})