from rest_framework import serializers
from .models import Booking, Menu 


class MenuSerliazer (serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['title','price','inventory']
        
class BookingSerliazer (serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        
        