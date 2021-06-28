from django_restframework import serializers
from .models import *

class accountsSerializer(serializers.Serializer):
    class Meta:
        model = Customer
        fields = [""]
