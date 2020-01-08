from django.db import models

# Create your models here.

class Todo(models.Model):
  content = models.CharField(max_length=512)
  update_at = models.DateTimeField(auto_now=True)
  create_at = models.DateTimeField(auto_now_add=True)