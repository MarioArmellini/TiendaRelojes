# serializers.py
from rest_framework import serializers
from .models import Contact  # Asegúrate de que Contact está definido en models.py

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'phone']
