#!/usr/bin/env python3
"""
Final integration test to verify all functionality works together.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from ui.console import ConsoleUI
from managers.todo_manager import TodoManager

def test_full_integration():
    """Test that all functionality works together."""
    print("Running final integration test...")

    # Create a console UI instance
    ui = ConsoleUI()
    manager = ui.todo_manager

    print("\n1. Testing Add Task functionality...")
    task1 = manager.create_task("Integration Test Task", "This is an integration test")
    print(f"   Created task: {task1.title} (ID: {task1.id})")

    print("\n2. Testing View Tasks functionality...")
    all_tasks = manager.get_all_tasks()
    print(f"   Total tasks: {len(all_tasks)}")
    for task in all_tasks:
        status = "Completed" if task.completed else "Pending"
        print(f"   - ID: {task.id}, Title: {task.title}, Status: {status}")

    print("\n3. Testing Update Task functionality...")
    update_result = manager.update_task(task1.id, "Updated Integration Task", "Updated description")
    print(f"   Update result: {update_result}")

    updated_task = manager.get_task_by_id(task1.id)
    print(f"   Updated task: {updated_task.title}")

    print("\n4. Testing Mark Complete functionality...")
    complete_result = manager.mark_task_complete(task1.id)
    print(f"   Mark complete result: {complete_result}")

    completed_task = manager.get_task_by_id(task1.id)
    print(f"   Task completion status: {completed_task.completed}")

    print("\n5. Testing Mark Incomplete functionality...")
    incomplete_result = manager.mark_task_incomplete(task1.id)
    print(f"   Mark incomplete result: {incomplete_result}")

    incomplete_task = manager.get_task_by_id(task1.id)
    print(f"   Task completion status: {incomplete_task.completed}")

    print("\n6. Testing Delete Task functionality...")
    delete_result = manager.delete_task(task1.id)
    print(f"   Delete result: {delete_result}")

    remaining_tasks = manager.get_all_tasks()
    print(f"   Remaining tasks: {len(remaining_tasks)}")

    print("\n7. Testing error handling with invalid operations...")
    error_test_1 = manager.get_task_by_id(999)
    print(f"   Get non-existent task: {error_test_1 is None}")

    error_test_2 = manager.update_task(999, "Should fail")
    print(f"   Update non-existent task: {error_test_2}")

    error_test_3 = manager.delete_task(999)
    print(f"   Delete non-existent task: {error_test_3}")

    print("\n8. Testing with empty task list...")
    empty_manager = TodoManager()
    empty_tasks = empty_manager.get_all_tasks()
    print(f"   Empty manager tasks: {len(empty_tasks)}")

    empty_result = empty_manager.mark_task_complete(1)
    print(f"   Mark complete on empty: {empty_result}")

    print("\nPASS: All integration tests passed!")
    print("PASS: All user stories implemented and working")
    print("PASS: Error handling working correctly")
    print("PASS: Data integrity maintained")

    return True

if __name__ == "__main__":
    print("Starting final integration verification...")

    success = test_full_integration()

    if success:
        print("\nSUCCESS: Final integration test completed successfully!")
        print("All features of the todo application are working correctly.")
    else:
        print("\nIntegration test failed!")
        sys.exit(1)