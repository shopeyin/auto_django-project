from django.shortcuts import render,redirect
from operator import attrgetter
from account.models import Account
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import JsonResponse
from cars.views import get_car_queryset

from cars.models import Cars

from personal.models import Contactus
from personal.forms import CreateMsgForm
from personal.forms import CreateAjaForm





# Create your views here.

def error_404(request,exception):
        data = {}
        return render(request,'personal/error_404.html', data)

def error_500(request):
        data = {}
        return render(request,'personal/error_500.html', data)



CARS_PER_PAGE = 6

def home_screen_view(request):

    context = {}

    query = ""
    if request.GET:
        query = request.GET.get('q', '')
        context['query'] = str(query)

    cars = sorted(get_car_queryset(query), key=attrgetter('date_updated'), reverse=True)
    context['cars'] = cars 



    #PAGINATION
    page = request.GET.get('page',1)
    cars_paginator = Paginator(cars,CARS_PER_PAGE)

    try:
        cars = cars_paginator.page(page)
    except PageNotAnInteger:
        cars = cars_paginator.page(CARS_PER_PAGE)
    except EmptyPage:
        cars = cars_paginator.page(cars_paginator.num_pages)


    context['cars'] = cars
    return render(request,'personal/home.html', context)







def contactus_view(request):
    context = {}

    if request.is_ajax():
        form=CreateMsgForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user=request.user
            instance.save()
            data = {
               'message' : 'You will be contacted shortly'
            }
            return JsonResponse(data)
        else:
            data = {
                'message' : 'invalid email address'
            }
        return JsonResponse(data)
        context['contactus_form'] = form
    return render(request,'personal/contactus.html',context)




