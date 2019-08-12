from rest_framework import serializers

from account.models import Account


class RegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    
    class Meta:
        model = Account
        fields = ['email','username', 'firstname', 'lastname','phonenumber', 'address','password','password2']
        extra_kwargs = {
            'password' : {'write_only':True}
        }

    def save(self):
        account = Account(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
            firstname = self.validated_data['firstname'],
            lastname = self.validated_data['lastname'],
            phonenumber = self.validated_data['phonenumber'],
            address = self.validated_data['address'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password':'Passwords must match'})
        account.set_password(password)
        account.save()
        return account

    
class AccountPropertiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['pk','email','username']
      