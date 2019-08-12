from rest_framework import serializers

from cars.models import Cars 


class CarsSerializer(serializers.ModelSerializer):
    
    username = serializers.SerializerMethodField('get_username_from_seller')

    class Meta:
        model = Cars
        fields = ['brand', 'model', 'year','color','price','condition','fuel_type','image', 'date_updated','username']
    
    
    def get_username_from_seller(self,cars):
        username = cars.seller.username
        return username
        


       