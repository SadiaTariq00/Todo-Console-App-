#!/usr/bin/env python3
"""
Test script to verify update task functionality works correctly.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from managers.todo_manager import TodoManager
from models.task import Task

def test_update_task():
    """Test updating task title and description works correctly."""
    print("Testing update task functionality...")

    # Create a todo manager
    manager = TodoManager()

    # Create a task
    task = manager.create_task("Original Title", "Original Description")
    print(f"Created task: ID={task.id}, Title='{task.title}', Description='{task.description}', Completed={task.completed}")

    # Verify initial state
    assert task.title == "Original Title"
    assert task.description == "Original Description"
    assert task.completed == False

    # Update the task
    success = manager.update_task(task.id, "Updated Title", "Updated Description")
    print(f"Update result: {success}")

    # Get the updated task
    updated_task = manager.get_task_by_id(task.id)
    print(f"Updated task: ID={updated_task.id}, Title='{updated_task.title}', Description='{updated_task.description}', Completed={updated_task.completed}")

    # Verify the update worked
    assert success == True
    assert updated_task.title == "Updated Title"
    assert updated_task.description == "Updated Description"
    assert updated_task.completed == False  # Should remain unchanged

    print("✓ Update task title and description test passed!")

    # Test updating only title
    success2 = manager.update_task(task.id, "New Title Only")
    updated_task2 = manager.get_task_by_id(task.id)
    print(f"Updated title only: '{updated_task2.title}', description: '{updated_task2.description}'")

    assert success2 == True
    assert updated_task2.title == "New Title Only"
    assert updated_task2.description == "Updated Description"  # Should remain unchanged

    print("✓ Update task title only test passed!")

    # Test updating only description
    success3 = manager.update_task(task.id, description="New Description Only")
    updated_task3 = manager.get_task_by_id(task.id)
    print(f"Updated description only: '{updated_task3.title}', description: '{updated_task3.description}'")

    assert success3 == True
    assert updated_task3.title == "New Title Only"
    assert updated_task3.description == "New Description Only"

    print("✓ Update task description only test passed!")

    # Test validation - empty title should raise ValueError
    try:
        manager.update_task(task.id, "")
        print("✗ Error: Empty title should raise ValueError")
        return False
    except ValueError as e:
        print(f"✓ Empty title validation works: {e}")

    # Test updating non-existent task
    success4 = manager.update_task(999, "Should not work")
    assert success4 == False
    print("✓ Update non-existent task returns False as expected")

    print("\nAll update functionality tests passed!")
    return True

def test_update_validation():
    """Test that updated title is not empty."""
    print("\nTesting validation for updated title...")

    manager = TodoManager()

    # Create a task
    task = manager.create_task("Test Title", "Test Description")

    # Try to update with empty title
    try:
        manager.update_task(task.id, "")
        print("✗ Error: Updating with empty title should raise ValueError")
        return False
    except ValueError as e:
        print(f"✓ Updating with empty title raises ValueError: {e}")

    # Try to update with whitespace-only title
    try:
        manager.update_task(task.id, "   ")
        print("✗ Error: Updating with whitespace-only title should raise ValueError")
        return False
    except ValueError as e:
        print(f"✓ Updating with whitespace-only title raises ValueError: {e}")

    print("All validation tests passed!")
    return True

def test_error_handling_for_invalid_ids():
    """Test error handling for invalid task IDs during update."""
    print("\nTesting error handling for invalid task IDs...")

    manager = TodoManager()

    # Try to update a non-existent task
    result = manager.update_task(999, "New Title")
    assert result == False
    print("✓ Update with invalid ID returns False as expected")

    # Try to update with negative ID
    result2 = manager.update_task(-1, "New Title")
    assert result2 == False
    print("✓ Update with negative ID returns False as expected")

    # Try to update with zero ID
    result3 = manager.update_task(0, "New Title")
    assert result3 == False
    print("✓ Update with zero ID returns False as expected")

    print("All invalid ID error handling tests passed!")
    return True

if __name__ == "__main__":
    print("Starting update task functionality tests...\n")

    success1 = test_update_task()
    if not success1:
        print("Update functionality tests failed!")
        sys.exit(1)

    success2 = test_update_validation()
    if not success2:
        print("Update validation tests failed!")
        sys.exit(1)

    success3 = test_error_handling_for_invalid_ids()
    if not success3:
        print("Error handling tests failed!")
        sys.exit(1)

    print("\n🎉 All update functionality tests completed successfully!")

    # Update the task file to mark tests as completed
    print("\nUpdating tasks.md to mark tests as completed...")

    import re

    with open("specs/001-todo-app/tasks.md", "r") as f:
        content = f.read()

    # Update T031, T032, T033 to completed
    content = re.sub(r'- \[ \] T031 \[US4\]', '- [X] T031 [US4]', content)
    content = re.sub(r'- \[ \] T032 \[US4\]', '- [X] T032 [US4]', content)
    content = re.sub(r'- \[ \] T033 \[US4\]', '- [X] T033 [US4]', content)

    with open("specs/001-todo-app/tasks.md", "w") as f:
        f.write(content)

    print("Tasks T031, T032, T033 marked as completed in tasks.md")