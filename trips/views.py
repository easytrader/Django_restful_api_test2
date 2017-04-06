from django.shortcuts import render,render_to_response
from django.template import RequestContext
from rest_framework import viewsets
from .models import Task
from .Serializers import TaskSerializer
from rest_framework.views import APIView
import sys
import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
def hello_world(request):
    return render_to_response('hello_world.html',{},context_instance = RequestContext(request))

@api_view(['GET', 'POST'])
def TaskViewSet(request):
    """
    List all snippets, or create a new snippet.
    """
    print("leo test in TaskViewSet")
    print("request.GET[param1]")
    print(request.GET['id'])
    if request.method == 'GET':
        print("leo test in GET")
        Tasks = Task.objects.all()
        serializer = TaskSerializer(Tasks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        print("leo test in POST")
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)