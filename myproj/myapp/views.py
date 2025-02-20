from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status

from myapp.models import Item
from myapp.serlializers import ItemSerializers


# Create your views here.

@api_view(['POST'])
def add_item(request):
    item=ItemSerializers(data=request.data)
    
    if Item.objects.filter(**request.data).exists():
        raise serializers.ValidationError("alredy exist")
    
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    

@api_view(['GET'])
def view_item(request):
    if request.query_params:
        items=Item.objects.filter(**request.query_params.dict())  
    else:
        items=  Item.objects.all()  
        
        
    if  items:
        serializer=ItemSerializers(items,many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
@api_view(['DELETE'])
def delete_item(request,pk):
    item=get_object_or_404(Item,pk=pk)
    item.delete()
    return  Response(status=status.HTTP_202_ACCEPTED)   


@api_view(['POST'])
def update_item(request,pk):
    item=Item.objects.get(id=pk)
    data=ItemSerializers(instance=item,data=request.data)
    
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    