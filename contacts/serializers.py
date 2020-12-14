from django.db.models import query
from rest_framework import serializers
from contacts.models import Address, Contact


class ContactSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=80)
    telephone = serializers.CharField(max_length=16, allow_blank=True)
    email = serializers.CharField(max_length=80, allow_blank=True)

    def create(self, user, validated_data):
        return Contact.objects.create(user=user, **validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.telephone = validated_data.get('telephone', instance.telephone)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance


class AddressSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    street = serializers.CharField(max_length=100)
    extra_info = serializers.CharField(max_length=100, allow_blank=True)
    zip_code = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=100)
    state = serializers.CharField(max_length=100)
    number = serializers.CharField(max_length=100)

    def create(self, contact, validated_data):
        return Address.objects.create(contact=contact, **validated_data)

    def update(self, instance, validated_data):
        instance.street = validated_data.get('street', instance.street)
        instance.extra_info = validated_data.get('extra_info', instance.extra_info)
        instance.zip_code = validated_data.get('zip_code', instance.zip_code)
        instance.city = validated_data.get('city', instance.city)
        instance.state = validated_data.get('state', instance.state)
        instance.number = validated_data.get('number', instance.number)
        instance.save()
        return instance