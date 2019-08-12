from django.urls import path

from cars.api.views import(
    api_detail_cars_view,
    api_create_cars_view,
    api_update_cars_view,
    api_delete_cars_view,
    ApiCarsListView,
) 

app_name= 'cars'

urlpatterns = [
    path('<slug>/',api_detail_cars_view, name="detail"),
    path('<slug>/update',api_update_cars_view, name="update"),
    path('<slug>/delete',api_delete_cars_view, name="delete"),
    path('create',api_create_cars_view, name="create"),
    path('list',ApiCarsListView.as_view(), name="list"),
]