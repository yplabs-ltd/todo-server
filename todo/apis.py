from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import viewsets
from todo.models import Todo

class TodoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Todo
    fields = ['id', 'content', 'update_at', 'create_at']

class TodoViewSet(viewsets.ModelViewSet):
  queryset = Todo.objects.all()
  serializer_class = TodoSerializer