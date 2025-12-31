import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from managers.todo_manager import TodoManager

print("Testing update validation more accurately...")

manager = TodoManager()

# Create a task first
task = manager.create_task("Original Title", "Original Description")
print(f"Created task with ID: {task.id}")

# Try to update with empty title on existing task
try:
    result = manager.update_task(task.id, "")
    print(f"ERROR: Expected ValueError but got result: {result}")
except ValueError as e:
    print(f"SUCCESS: Empty title validation works: {e}")

# Try to update with whitespace-only title on existing task
try:
    result = manager.update_task(task.id, "   ")
    print(f"ERROR: Expected ValueError but got result: {result}")
except ValueError as e:
    print(f"SUCCESS: Whitespace-only title validation works: {e}")

print("Update validation test completed!")