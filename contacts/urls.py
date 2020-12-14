from django.contrib import admin
from django.urls import path, include

from contacts import views


urlpatterns = [
    path('list_contacts/', views.list_contact, name='list_contacts'),
    path('info_contact/<int:pk>', views.info_contact, name='info_contact'),
    path('info_address/<int:pk>', views.info_address, name='info_contact'),
    path('add_contact/', views.add_contact, name='add_contact'),
    path('add_address/<int:pk_contact>', views.add_address, name='add_address'),
    path('list_address/<int:pk_contact>', views.list_address, name='list_address'),
    path('home/', views.home, name='home'),
    path('details/<int:pk>', views.details, name='details'),

]
