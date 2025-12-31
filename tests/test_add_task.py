#!/usr/bin/env python3
"""
Test script to verify the todo application functionality.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from managers.todo_manager import TodoManager

def test_add_task():
    """Test that adding a task works correctly."""
    print("Testing add task functionality...")

    # Create a new TodoManager instance
    manager = TodoManager()

    # Test adding a task with title and description
    task = manager.create_task("Test Task", "This is a test description")

    # Verify the task was created with correct properties
    assert task.id == 1, f"Expected ID 1, got {task.id}"
    assert task.title == "Test Task", f"Expected title 'Test Task', got {task.title}"
    assert task.description == "This is a test description", f"Expected description 'This is a test description', got {task.description}"
    assert task.completed == False, f"Expected completed False, got {task.completed}"

    print(f"[PASS] Task created successfully - ID: {task.id}, Title: {task.title}, Description: {task.description}, Completed: {task.completed}")

    # Test adding another task to verify ID increment
    task2 = manager.create_task("Second Task")
    assert task2.id == 2, f"Expected ID 2, got {task2.id}"
    assert task2.title == "Second Task", f"Expected title 'Second Task', got {task2.title}"
    assert task2.description == "", f"Expected empty description, got '{task2.description}'"
    assert task2.completed == False, f"Expected completed False, got {task2.completed}"

    print(f"[PASS] Second task created successfully - ID: {task2.id}, Title: {task2.title}, Description: {task2.description}, Completed: {task2.completed}")

    # Test that tasks are stored properly
    all_tasks = manager.get_all_tasks()
    assert len(all_tasks) == 2, f"Expected 2 tasks, got {len(all_tasks)}"

    print("[PASS] Both tasks are stored correctly in the manager")
    print("[PASS] ID auto-increment works correctly")
    print("[PASS] All basic functionality verified!")

    return True

if __name__ == "__main__":
    success = test_add_task()
    if success:
        print("\n[PASS] All tests passed! Add task functionality works correctly.")
    else:
        print("\n[FAIL] Tests failed!")