import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from managers.todo_manager import TodoManager

print("Testing update functionality...")

# Create a todo manager
manager = TodoManager()

# Create a task
task = manager.create_task("Original Title", "Original Description")
print(f"Created task: ID={task.id}, Title='{task.title}', Description='{task.description}'")

# Update the task
success = manager.update_task(task.id, "Updated Title", "Updated Description")
print(f"Update result: {success}")

# Get the updated task
updated_task = manager.get_task_by_id(task.id)
print(f"Updated task: ID={updated_task.id}, Title='{updated_task.title}', Description='{updated_task.description}'")

# Test validation - empty title should raise ValueError
try:
    manager.update_task(task.id, "")
    print("ERROR: Empty title should raise ValueError")
except ValueError as e:
    print(f"SUCCESS: Empty title validation works: {e}")

# Test updating non-existent task
success4 = manager.update_task(999, "Should not work")
print(f"Update non-existent task result: {success4}")

print("Update functionality test completed!")