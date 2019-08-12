from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter,OrderingFilter

from account.models import Account
from cars.models import Cars
from cars.api.serializers import CarsSerializer




@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def api_detail_cars_view(request,slug):

    try:
        cars = Cars.objects.get(slug=slug)
        serializer=CarsSerializer(cars)
        return Response(serializer.data)

    except Cars.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    
@api_view(['PUT',])
@permission_classes((IsAuthenticated,))
def api_update_cars_view(request,slug):

    
   
    try:
        cars = Cars.objects.get(slug=slug)

        user = request.user
        if cars.seller !=  user:
            return Response({'response':'You dont have permission to update  that'})
    
        serializer = CarsSerializer(cars,data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success']="updated succesfully"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Cars.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE',])
@permission_classes((IsAuthenticated,))
def api_delete_cars_view(request,slug):

   

    try:
        cars = Cars.objects.get(slug=slug)

        user = request.user
        if cars.seller != user:
            return Response({'response':'You dont have permission to delete that'})
        
        operation = cars.delete()
        data = {}
        if operation:
            data['success'] = "delete successful"
        else:
            data["failure"] = "unable to delete"
        return Response(data=data)
    except Cars.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['POST'],)
@permission_classes((IsAuthenticated,))
def api_create_cars_view(request):
    account = request.user
    cars = Cars(seller=account)
    serializer=CarsSerializer(cars,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class ApiCarsListView(ListAPIView):
    queryset=Cars.objects.all()
    serializer_class = CarsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter,OrderingFilter)
    search_fields = ('brand','model','seller__username')





