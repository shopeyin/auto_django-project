from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.decorators import api_view

from account.api.serializers import RegistrationSerializer,AccountPropertiesSerializer
from rest_framework.authtoken.models import Token

@api_view(['POST',])
@permission_classes((AllowAny,))
def registration_view(request):
    serializer=RegistrationSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        account = serializer.save()
        data['response'] = "successfully registered"
        data['email'] = account.email
        data['firstname'] = account.firstname
        data['lastname'] = account.lastname
        data['address'] = account.address
        data['phonenumber'] = account.phonenumber
        data['username'] = account.username
        token = Token.objects.get(user=account).key
        data['token'] = token
    else:
        data = serializer.errors
    return Response(data)


@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def account_properties_view(request):
    try:
        account = request.user
        serializer = AccountPropertiesSerializer(account)
        return Response(serializer.data)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    


@api_view(['PUT',])
@permission_classes((IsAuthenticated,))
def update_account_view(request):
    try:
        account = request.user
        serializer = AccountPropertiesSerializer(account,data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = "Account update success"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

