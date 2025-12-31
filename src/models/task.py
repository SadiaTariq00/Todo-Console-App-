"""
Task model for the In-Memory Python Console Todo Application.

This module defines the Task class with its properties and basic validation.
"""

from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class Task:
    """
    Represents a single todo item with unique ID, title, description, and completion status.

    Attributes:
        id (int): Auto-incremented unique identifier for the task
        title (str): Title of the task (required, non-empty)
        description (str): Description of the task (optional, can be empty)
        completed (bool): Completion status of the task (default: False)
        created_at (datetime): Timestamp when the task was created
        completed_at (datetime): Timestamp when the task was completed (optional)
    """

    id: int
    title: str
    description: str = ""
    completed: bool = False
    created_at: datetime = None
    completed_at: datetime = None

    def __post_init__(self):
        """Validate the task after initialization and set default timestamps."""
        if not self.title or not self.title.strip():
            raise ValueError("Task title cannot be empty")
        if not isinstance(self.id, int) or self.id <= 0:
            raise ValueError("Task ID must be a positive integer")
        if not isinstance(self.completed, bool):
            raise ValueError("Task completion status must be a boolean")

        # Set created_at timestamp if not provided
        if self.created_at is None:
            self.created_at = datetime.now()

        # completed_at should remain None unless task is completed
        if self.completed and self.completed_at is None:
            self.completed_at = datetime.now()