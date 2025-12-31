#!/usr/bin/env python3
"""
Test script to verify the mark task as complete/incomplete functionality.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from managers.todo_manager import TodoManager

def test_mark_tasks():
    """Test that marking tasks as complete/incomplete works correctly."""
    print("Testing mark tasks functionality...")

    # Create a new TodoManager instance
    manager = TodoManager()

    # Add a task
    task = manager.create_task("Test Task", "Description for test task")
    assert task.completed == False, "Task should initially be incomplete"
    print(f"[PASS] Task created with ID {task.id} and is initially incomplete")

    # Test marking as complete
    success = manager.mark_task_complete(task.id)
    assert success == True, "Should be able to mark existing task as complete"

    # Verify the task is now complete
    updated_task = manager.get_task_by_id(task.id)
    assert updated_task is not None, "Task should still exist"
    assert updated_task.completed == True, "Task should now be complete"
    print(f"[PASS] Task marked as complete successfully")

    # Test marking as incomplete
    success = manager.mark_task_incomplete(task.id)
    assert success == True, "Should be able to mark existing task as incomplete"

    # Verify the task is now incomplete
    updated_task = manager.get_task_by_id(task.id)
    assert updated_task is not None, "Task should still exist"
    assert updated_task.completed == False, "Task should now be incomplete"
    print(f"[PASS] Task marked as incomplete successfully")

    # Test error handling for non-existent task
    success = manager.mark_task_complete(999)  # Non-existent ID
    assert success == False, "Should not be able to mark non-existent task as complete"
    print(f"[PASS] Correctly handles non-existent task ID for mark complete")

    success = manager.mark_task_incomplete(999)  # Non-existent ID
    assert success == False, "Should not be able to mark non-existent task as incomplete"
    print(f"[PASS] Correctly handles non-existent task ID for mark incomplete")

    # Add another task and test switching states multiple times
    task2 = manager.create_task("Second Task")
    original_state = task2.completed
    assert original_state == False, "Second task should initially be incomplete"

    # Complete it
    manager.mark_task_complete(task2.id)
    task2 = manager.get_task_by_id(task2.id)
    assert task2.completed == True, "Second task should be complete"

    # Make it incomplete again
    manager.mark_task_incomplete(task2.id)
    task2 = manager.get_task_by_id(task2.id)
    assert task2.completed == False, "Second task should be incomplete again"

    print(f"[PASS] Multiple state changes work correctly")

    print("[PASS] All mark tasks functionality verified!")

    return True

if __name__ == "__main__":
    success = test_mark_tasks()
    if success:
        print("\n[PASS] All tests passed! Mark tasks functionality works correctly.")
    else:
        print("\n[FAIL] Tests failed!")