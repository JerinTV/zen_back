# zentodo_backend/tasks/views.py

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser # <-- NEW: Import IsAdminUser
from django.contrib.auth.models import User # <-- NEW: Import Django's User model
from .models import Todo
from .serializers import TodoSerializer, UserSerializer # <-- NEW: Import UserSerializer

class TodoViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing Todo instances.
    """
    queryset = Todo.objects.all() # Define the base queryset for the viewset

    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list of all the todos
        for the currently authenticated user.
        """
        # This method will still filter the queryset based on the current user,
        # but the 'queryset' attribute provides the default for the router.
        return Todo.objects.filter(owner=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        """
        Assign the current authenticated user as the owner of the new todo.
        """
        serializer.save(owner=self.request.user)

# Your NEW UserViewSet
class UserViewSet(viewsets.ReadOnlyModelViewSet): # Use ReadOnlyModelViewSet for GET operations only
    queryset = User.objects.all() # Get all User objects
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser] # ONLY admin users can access this endpoint