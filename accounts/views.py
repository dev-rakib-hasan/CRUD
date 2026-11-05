from django.db.migrations import serializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .models import Todo
from .serializers import TodoSerializer

# Create your views here.

# create todo
@api_view(['POST'])
def create(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#get all todos
@api_view(['GET'])
def list(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)

#get single todo
@api_view(['GET'])
def get_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    serializer = TodoSerializer(todo)
    
    return Response(serializer.data,status=status.HTTP_200_OK)

#update todo
@api_view(['PATCH'])
def update(request, pk):
    todo = Todo.objects.get(pk=pk)

    serializer = TodoSerializer(todo,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# delete todo
@api_view(['DELETE'])
def delete_todo(request, pk):
    todo = Todo.objects.get(pk=pk)

    todo.delete()

    return Response(
        {'message': 'Todo deleted successfully'},
        status=status.HTTP_204_NO_CONTENT
    )