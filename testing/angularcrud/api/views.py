from django.shortcuts import render
from .models import Todo
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import TodoSerializer


# Create your views here.
class TodoViewSet(viewsets.ViewSet):

    def get_Todo(self, request, **kwargs):
        todo = Todo.objects.all()
        serializer = TodoSerializer(todo, many=True)
        return Response(serializer.data, status=200)

    def create_Todo(self, request, **kwargs):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    
    def update_Todo(self, request, **kwargs):
        todo_id = kwargs.get('todo_id')
        instance = Todo.objects.get(id=todo_id)
        serializer = TodoSerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
    def delete_Todo(self, request, **kwargs):
        todo_id = kwargs.get('todo_id')
        instance = Todo.objects.get(id=todo_id)
        instance.delete()
        return Response({}, status=202)

    # def update_Movie(self, request, **kwargs):
    #     instance = Movie.objects.get(id=request.data.get('id'))
    #     user = Movie.objects.all()
    #     serializer = MovieSerializer(instance=instance, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=200)
    #     return Response(serializer.errors, status=400)

    # def create_Movie(self, request, **kwargs):
    #     serializer = MovieSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=200)
    #     return Response(serializer.errors, status=400)

    # def delete_Movie(self, request, **kwargs):
    #     movie_id = kwargs.get('movie_id')
    #     instance = Movie.objects.get(id=movie_id)
    #     instance.delete()
    #     return Response({}, status=202)