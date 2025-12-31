#!/usr/bin/env python3
"""
Test script to verify the view tasks functionality.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from managers.todo_manager import TodoManager

def test_view_tasks():
    """Test that viewing tasks works correctly."""
    print("Testing view tasks functionality...")

    # Create a new TodoManager instance
    manager = TodoManager()

    # Test with no tasks
    tasks = manager.get_all_tasks()
    assert len(tasks) == 0, f"Expected 0 tasks initially, got {len(tasks)}"
    print("[PASS] Correctly handles case with no tasks")

    # Add a few tasks
    task1 = manager.create_task("First Task", "Description for first task")
    task2 = manager.create_task("Second Task", "Description for second task")
    manager.mark_task_complete(task1.id)  # Mark first task as complete

    # Get all tasks and verify
    tasks = manager.get_all_tasks()
    assert len(tasks) == 2, f"Expected 2 tasks, got {len(tasks)}"

    # Verify the tasks have the correct properties
    task_dict = {task.id: task for task in tasks}
    assert task1.id in task_dict, "First task should be in the list"
    assert task2.id in task_dict, "Second task should be in the list"

    # Verify first task is complete
    assert task_dict[task1.id].completed == True, "First task should be complete"
    # Verify second task is incomplete
    assert task_dict[task2.id].completed == False, "Second task should be incomplete"

    print(f"[PASS] Retrieved {len(tasks)} tasks correctly")
    print(f"[PASS] Task 1 (ID: {task1.id}) is {'complete' if task_dict[task1.id].completed else 'incomplete'}")
    print(f"[PASS] Task 2 (ID: {task2.id}) is {'complete' if task_dict[task2.id].completed else 'incomplete'}")

    # Test that all required fields are present
    for task in tasks:
        assert hasattr(task, 'id'), "Task should have an ID"
        assert hasattr(task, 'title'), "Task should have a title"
        assert hasattr(task, 'description'), "Task should have a description"
        assert hasattr(task, 'completed'), "Task should have a completion status"

    print("[PASS] All tasks have required fields (id, title, description, completed)")
    print("[PASS] All view tasks functionality verified!")

    return True

if __name__ == "__main__":
    success = test_view_tasks()
    if success:
        print("\n[PASS] All tests passed! View tasks functionality works correctly.")
    else:
        print("\n[FAIL] Tests failed!")