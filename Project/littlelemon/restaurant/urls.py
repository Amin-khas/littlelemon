from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter 

router = DefaultRouter(trailing_slash = False)
router.register('tables',views.BookingViewSet,basename='tables')

urlpatterns = [
   
    path('menu/',views.MenuItemView.as_view()),
    path('menu/<int:pk>',views.SingleMenuItemView.as_view()),
    path('',include(router.urls)),
    
]
