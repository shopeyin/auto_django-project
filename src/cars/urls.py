from django.urls import path
from cars.views import(
    create_cars_view,
    detail_cars_view,
    edit_cars_view,
    delete_cars_view,
    

    
)

app_name = 'cars' 

urlpatterns= [
    path('create/',create_cars_view,name='create'),
    path('<slug>/',detail_cars_view,name='detail'),
    path('<slug>/edit',edit_cars_view,name='edit'),
    path('<slug>/delete',delete_cars_view,name='delete')
]