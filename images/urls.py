from django.contrib import admin
from django.urls import path

from .views import home_view,delete_image_view

urlpatterns = [
	path('',home_view,name='home'),
	path('delete_image/<int:id>/',delete_image_view,name='delete_image')
]