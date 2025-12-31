"""
Todo Manager for the In-Memory Python Console Todo Application.

This module handles business logic, data operations, and maintains state for tasks.
"""

from typing import Dict, List, Optional
from models.task import Task


class TodoManager:
    """
    Core business logic component that manages the collection of tasks and provides operations to manipulate them.

    The manager uses in-memory storage with a dictionary for O(1) access by task ID.
    """

    def __init__(self):
        """Initialize the TodoManager with an empty task dictionary and ID counter."""
        self.tasks: Dict[int, Task] = {}
        self.next_id: int = 1

    def create_task(self, title: str, description: str = "") -> Task:
        """
        Create a new task with auto-incremented ID and completion status set to False.

        Args:
            title: Title of the task (required)
            description: Description of the task (optional)

        Returns:
            Created Task object with assigned ID
        """
        task_id = self.next_id
        self.next_id += 1

        task = Task(id=task_id, title=title, description=description, completed=False)
        self.tasks[task_id] = task
        return task

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks in the system.

        Returns:
            List of all tasks
        """
        return list(self.tasks.values())

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Get a task by its ID.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            Task object if found, None otherwise
        """
        return self.tasks.get(task_id)

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """
        Update a task with new values.

        Args:
            task_id: The ID of the task to update
            title: New title (optional)
            description: New description (optional)

        Returns:
            True if successful, False if task not found
        """
        if task_id not in self.tasks:
            return False

        task = self.tasks[task_id]

        if title is not None:
            if not title or not title.strip():
                raise ValueError("Task title cannot be empty")
            task.title = title

        if description is not None:
            task.description = description

        return True

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if successful, False if task not found
        """
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False

    def mark_task_complete(self, task_id: int) -> bool:
        """
        Mark a task as complete.

        Args:
            task_id: The ID of the task to mark as complete

        Returns:
            True if successful, False if task not found
        """
        if task_id in self.tasks:
            task = self.tasks[task_id]
            task.completed = True
            # Set completed_at timestamp when marking as complete
            from datetime import datetime
            task.completed_at = datetime.now()
            return True
        return False

    def mark_task_incomplete(self, task_id: int) -> bool:
        """
        Mark a task as incomplete.

        Args:
            task_id: The ID of the task to mark as incomplete

        Returns:
            True if successful, False if task not found
        """
        if task_id in self.tasks:
            task = self.tasks[task_id]
            task.completed = False
            # Clear completed_at timestamp when marking as incomplete
            task.completed_at = None
            return True
        return False