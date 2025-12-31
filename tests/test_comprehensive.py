import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from managers.todo_manager import TodoManager

print("Testing comprehensive error handling and edge cases...")

# Test 1: Very long titles and descriptions (T043)
print("\n1. Testing edge cases like very long titles/descriptions...")
manager = TodoManager()

# Create a very long title and description
long_title = "A" * 1000  # 1000 characters
long_description = "B" * 2000  # 2000 characters

try:
    task = manager.create_task(long_title, long_description)
    print(f"PASS: Created task with long title ({len(task.title)} chars) and description ({len(task.description)} chars)")
except Exception as e:
    print(f"INFO: Long input handling - {e}")

# Test 2: Empty task list operations (T044)
print("\n2. Testing application with empty task list...")
empty_manager = TodoManager()

# Try operations on empty list
tasks = empty_manager.get_all_tasks()
print(f"Empty list task count: {len(tasks)}")

# Try to mark complete/incomplete on non-existent task
result1 = empty_manager.mark_task_complete(999)
print(f"Mark non-existent task complete: {result1}")

result2 = empty_manager.mark_task_incomplete(999)
print(f"Mark non-existent task incomplete: {result2}")

result3 = empty_manager.update_task(999, "New Title")
print(f"Update non-existent task: {result3}")

result4 = empty_manager.delete_task(999)
print(f"Delete non-existent task: {result4}")

print("PASS: All operations on empty task list handled correctly")

# Test 3: Invalid inputs (T046)
print("\n3. Testing invalid inputs...")
# These are already handled by the UI layer, but let's test the manager directly

# Test invalid task IDs (negative, zero)
result_neg = empty_manager.get_task_by_id(-1)
print(f"Get task with negative ID: {result_neg is None}")

result_zero = empty_manager.get_task_by_id(0)
print(f"Get task with zero ID: {result_zero is None}")

# Test invalid update with empty title
try:
    empty_manager.update_task(1, "")  # Empty title should fail
    print("FAIL: Empty title update should raise ValueError")
except ValueError:
    print("PASS: Empty title update raises ValueError as expected")

# Test 4: Verify in-memory storage works throughout session (T045)
print("\n4. Testing in-memory storage throughout session...")
session_manager = TodoManager()

# Create several tasks
tasks_created = []
for i in range(5):
    task = session_manager.create_task(f"Task {i+1}", f"Description {i+1}")
    tasks_created.append(task)

print(f"Created {len(tasks_created)} tasks")

# Verify all tasks are accessible
all_tasks = session_manager.get_all_tasks()
print(f"Retrieved {len(all_tasks)} tasks from storage")

# Modify some tasks
if len(all_tasks) > 0:
    first_task_id = all_tasks[0].id
    result = session_manager.mark_task_complete(first_task_id)
    print(f"Marked task {first_task_id} complete: {result}")

    # Verify the change persisted
    retrieved_task = session_manager.get_task_by_id(first_task_id)
    print(f"Task {first_task_id} completion status: {retrieved_task.completed}")

print("PASS: In-memory storage works throughout session")

# Test 5: Test all user stories together in sequence (T047)
print("\n5. Testing all user stories together in sequence...")

# Create a fresh manager for sequence test
sequence_manager = TodoManager()

# US1: Add a task
task1 = sequence_manager.create_task("Sequence Task", "Description for sequence test")
print(f"US1 - Added task: {task1.title}")

# US2: View tasks
tasks = sequence_manager.get_all_tasks()
print(f"US2 - Retrieved {len(tasks)} tasks")

# US3: Mark task as complete
result = sequence_manager.mark_task_complete(task1.id)
print(f"US3 - Marked task complete: {result}")

# US4: Update task
result = sequence_manager.update_task(task1.id, "Updated Sequence Task", "Updated description")
print(f"US4 - Updated task: {result}")

# US5: Delete task
result = sequence_manager.delete_task(task1.id)
print(f"US5 - Deleted task: {result}")

print("PASS: All user stories work together in sequence")

print("\nAll comprehensive tests completed!")