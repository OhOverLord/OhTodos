from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import Http404

from .models import Todo
from .serializers import TodoSerializer


class TodoListAPI(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = TodoSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_todo(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Todo.DoesNotExist:
        raise Http404

@api_view(['GET'])
def todo_status(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
        todo.completed = not todo.completed
        todo.save()
        return Response(status=status.HTTP_205_RESET_CONTENT)
    except Todo.DoesNotExist:
        raise Http404