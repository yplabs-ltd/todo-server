from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import viewsets, views
from todo.models import Todo

class TodoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Todo
    fields = ['id', 'content', 'update_at', 'create_at']

class TodoViewSet(viewsets.ModelViewSet):
  queryset = Todo.objects.all()
  serializer_class = TodoSerializer


class HealthCheckAPI(views.APIView):

  def get(self, request):
    return Response({})