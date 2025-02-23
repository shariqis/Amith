from django.db.models import fields
from rest_framework import serializers

from myapp.models import Item

class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model=Item
        fields=('id','category','name','amount')