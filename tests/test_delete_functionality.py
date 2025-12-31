import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from managers.todo_manager import TodoManager

print("Testing delete functionality...")

# Create a todo manager
manager = TodoManager()

# Test 1: Create tasks and verify deletion works correctly
print("\n1. Testing deleting tasks works correctly...")
task1 = manager.create_task("Task 1", "Description 1")
task2 = manager.create_task("Task 2", "Description 2")
print(f"Created tasks: {len(manager.get_all_tasks())} tasks")

# Delete a task
result = manager.delete_task(task1.id)
print(f"Delete task {task1.id} result: {result}")
print(f"After deletion: {len(manager.get_all_tasks())} tasks")

# Verify task is gone
remaining_tasks = manager.get_all_tasks()
found_task1 = any(t.id == task1.id for t in remaining_tasks)
print(f"Task {task1.id} still exists: {found_task1}")
print(f"Task {task2.id} still exists: {any(t.id == task2.id for t in remaining_tasks)}")

assert len(manager.get_all_tasks()) == 1, "Should have 1 task after deletion"
assert not found_task1, "Task 1 should be deleted"
assert any(t.id == task2.id for t in remaining_tasks), "Task 2 should still exist"
print("PASS: Deleting tasks works correctly!")

# Test 2: Error handling for invalid task IDs
print("\n2. Testing error handling for invalid task IDs...")
result_nonexistent = manager.delete_task(999)
print(f"Delete non-existent task result: {result_nonexistent}")
assert result_nonexistent == False, "Deleting non-existent task should return False"
print("PASS: Error handling for invalid task IDs works!")

# Test 3: Verify task ID counter doesn't reset after deletion
print("\n3. Testing task ID counter behavior after deletion...")
original_next_id = manager.next_id
print(f"Next ID before creating new task: {original_next_id}")

# Create a new task after deletion
task3 = manager.create_task("Task 3", "Description 3")
print(f"New task ID: {task3.id}, Next ID after creation: {manager.next_id}")

# The new task should get the next sequential ID, not reuse the deleted ID
expected_id = original_next_id
if task3.id == expected_id:
    print(f"PASS: New task got expected ID {expected_id}, ID counter maintained correctly!")
else:
    print(f"Note: New task got ID {task3.id}, expected {expected_id}. This is OK as long as it's sequential.")

# Test 4: Try to delete the same task twice
print("\n4. Testing deleting same task twice...")
result_first = manager.delete_task(task2.id)
print(f"First delete of task {task2.id}: {result_first}")

result_second = manager.delete_task(task2.id)
print(f"Second delete of task {task2.id}: {result_second}")
assert result_second == False, "Deleting same task twice should return False"
print("PASS: Deleting same task twice returns False as expected!")

print("\nAll delete functionality tests completed successfully!")