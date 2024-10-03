from django.contrib.auth.models import User, Group
from rest_framework import serializers

from todo.models import Task

class TaskSerializer(serializers.ModelSerializer):
    assignees = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='username'
    )
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'completed', 'assignees']
        read_only_fields = ['id']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        read_only_fields = ['id']
