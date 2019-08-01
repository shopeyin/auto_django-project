from django.shortcuts import render, redirect,get_object_or_404
from django.db.models import Q
from django.http import HttpResponse
from cars.models import Cars
from cars.forms import CreateCarsForm,UpdateCarsForm
from account.models import Account







def create_cars_view(request):
    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')

    form = CreateCarsForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        seller = Account.objects.filter(email=user.email).first()
        obj.seller = seller
        obj.save()
        context['success'] = 'Uploaded successfully'
        form = CreateCarsForm()
    context['form'] = form

    return render(request, "cars/create_cars.html",context)



def detail_cars_view(request,slug):

	context = {}

	cars = get_object_or_404(Cars, slug=slug)
	context['cars'] = cars

	return render(request, 'cars/detail_cars.html', context)




def delete_cars_view(request,slug):

	cars = get_object_or_404(Cars,slug=slug)

	cars.delete()
	
	return redirect('/account/')






def edit_cars_view(request, slug):

	context = {}

	user = request.user
	if not user.is_authenticated:
		return redirect("must_authenticate")
	
	cars = get_object_or_404(Cars,slug=slug)

	if cars.seller !=user:
		return HttpResponse("NOT THE SELLER")

	if request.POST:
		form = UpdateCarsForm(request.POST or None, request.FILES or None, instance=cars)
		if form.is_valid():
			obj = form.save()
			obj.save()
			context['success_message'] = 'Updated'
			cars = obj

	form = UpdateCarsForm(
		initial = {
			"brand" : cars.brand,
			"model" :cars.model,
            "price" :cars.price,
			"image" : cars.image,
		}
	)

	context['form'] = form
	return render(request,"cars/edit_cars.html", context)





def get_car_queryset(query=None):
	queryset = []
	queries = query.split(" ")
	for q in queries:
		cars = Cars.objects.filter(
			Q(brand__icontains=q) |
			Q(model__icontains=q) 
			).distinct()
		for car in cars:
			queryset.append(car)
	return list(set(queryset))