from django.shortcuts import render 
from django.http import response
from .serializers import BookingSerliazer,MenuSerliazer
from .models import Booking,Menu
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView , DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

# Create your views here.

def index (request):
    return render(request,'index.html',{})

# @api_view()
# def menu_items (request):
#     item = Menu.objects.all()
#     serialized_item = MenuSerliazer(item)
#     return response(serialized_item.data)

class MenuItemView (ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerliazer
    
class SingleMenuItemView (RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerliazer
    
    
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerliazer
  
    
