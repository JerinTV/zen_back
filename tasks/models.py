# tasks/models.py

from django.db import models
from django.contrib.auth.models import User # Import Django's built-in User model

class Todo(models.Model):
    """
    Represents a single todo item in the Zentodo application.
    Each todo is associated with a specific user (owner).
    """
    title = models.CharField(
        max_length=200,
        help_text="The main title or short description of the todo item."
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text="An optional longer description for the todo item."
    )
    priority = models.CharField(
        max_length=20,
        blank=True,
        default='',
        help_text="Optional priority (easy/medium/hard/urgent). Stored as a string for frontend compatibility.",
    )
    category = models.CharField(
        max_length=50,
        blank=True,
        default='',
        help_text="Optional category label (e.g., Work, Personal).",
    )
    time = models.CharField(
        max_length=20,
        blank=True,
        default='',
        help_text="Optional scheduled time as a display string (e.g., '09:30 AM').",
    )
    due_date = models.CharField(
        max_length=10,
        blank=True,
        default='',
        help_text="Optional due date as YYYY-MM-DD string (frontend uses this format).",
    )
    trashed = models.BooleanField(
        default=False,
        help_text="Soft-delete flag used by the frontend Trash view.",
    )
    subtasks = models.JSONField(
        blank=True,
        default=list,
        help_text="Optional list of subtasks (frontend sends an array).",
    )
    completed = models.BooleanField(
        default=False,
        help_text="Indicates whether the todo item has been completed."
    )
    created_at = models.DateTimeField(
        auto_now_add=True, # Automatically sets the creation timestamp when the object is first created
        help_text="The date and time when the todo item was created."
    )
    updated_at = models.DateTimeField(
        auto_now=True,     # Automatically updates the timestamp every time the object is saved
        help_text="The date and time when the todo item was last updated."
    )
    # Foreign Key to Django's built-in User model
    # This establishes a one-to-many relationship: one user can have many todos.
    # on_delete=models.CASCADE means if a User is deleted, all their associated Todos are also deleted.
    # related_name='todos' allows you to access a user's todos like user.todos.all()
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='todos',
        help_text="The user who owns this todo item."
    )

    class Meta:
        """
        Meta options for the Todo model.
        """
        # Orders query results by 'created_at' in descending order (newest first) by default.
        ordering = ['-created_at']
        # Verbose name for the model in the Django admin interface (optional)
        verbose_name = "Todo Item"
        verbose_name_plural = "Todo Items"

    def __str__(self):
        """
        String representation of the Todo object.
        This is what will be displayed in the Django admin and when printing objects.
        """
        return f"{self.title} (by {self.owner.username})" if self.owner else self.title
