# zentodo_backend/tasks/serializers.py

from rest_framework import serializers
from .models import Todo # Import your Todo model
from django.contrib.auth.models import User # Import Django's User model (NEW)

class TodoSerializer(serializers.ModelSerializer):
    # The 'owner' field needs special handling for display purposes,
    # but the backend will set it automatically.
    # We make it read-only so the client cannot send 'owner' in their request.
    owner = serializers.ReadOnlyField(source='owner.username') # Displays the username of the owner

    # Frontend uses camelCase `dueDate`. Map it to model field `due_date`.
    dueDate = serializers.CharField(source='due_date', required=False, allow_blank=True)

    class Meta:
        model = Todo # Specify the model this serializer is for
        fields = [
            'id',
            'title',
            'description',
            'completed',
            'priority',
            'category',
            'time',
            'dueDate',
            'trashed',
            'subtasks',
            'created_at',
            'updated_at',
            'owner' # Include the owner field
        ]
        # These fields are automatically set by Django and should not be provided by the client
        read_only_fields = ['created_at', 'updated_at']
        # Note: 'owner' is already read-only due to ReadOnlyField above.

# Your NEW UserSerializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name'] # Choose the fields you want to expose
        read_only_fields = ['username', 'email'] # Make them read-only if you don't want them editable via this serializer
