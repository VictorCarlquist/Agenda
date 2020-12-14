from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from contacts.models import Contact, Address
from contacts.serializers import ContactSerializer, AddressSerializer


@api_view(['GET'])
@login_required
def list_contact(request):
    user = request.user
    if request.method == 'GET':
        contacts = Contact.objects.filter(user=user)
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
@login_required
def info_contact(request, pk):
    user = request.user

    try:
        contact = Contact.objects.get(pk=pk, user=user)
    except Contact.DoesNotExist:
        return redirect('/home')

    if request.method == 'GET':
        serializer = ContactSerializer(contact)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@login_required
def add_contact(request):
    user = request.user

    if request.method == 'POST':
        contact = Contact()
        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.create(user, serializer.validated_data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
@login_required
def info_address(request, pk):
    user = request.user

    try:
        address = Address.objects.get(pk=pk, contact__user=user)
    except Address.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AddressSerializer(address)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = AddressSerializer(address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@login_required
def add_address(request, pk_contact):
    user = request.user

    if request.method == 'POST':
        address = Address()
        serializer = AddressSerializer(address, data=request.data)
        if serializer.is_valid():
            try:
                contact = Contact.objects.get(pk=pk_contact, user=user)
            except Contact.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            serializer.create(contact, serializer.validated_data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@login_required
def list_address(request, pk_contact):
    user = request.user

    # A consulta também retorna o addresses, não havendo necessidade de 
    # requisitar novos dados ao banco.
    contact = (
        Contact
        .objects
        .filter(pk=pk_contact, user=user)
        .prefetch_related('addresses')
        .first()
    )

    if not contact:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = AddressSerializer(contact.addresses, many=True)
        return Response(serializer.data)

def home(request):
    return render(request, 'home.html')

def details(request, pk):
    user = request.user
    try:
        contact = Contact.objects.get(pk=pk, user=user)
    except Contact.DoesNotExist:
        return redirect('/home')
    return render(request, 'details.html', {'contact': contact})
