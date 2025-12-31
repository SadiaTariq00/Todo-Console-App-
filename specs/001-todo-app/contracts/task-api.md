# Todo Application API Contracts

**Feature**: 001-todo-app
**Date**: 2025-12-30

## Task Management API

### Data Types

#### Task
```python
class Task:
    id: int          # Auto-incremented unique identifier
    title: str       # Task title (non-empty)
    description: str # Task description (can be empty)
    completed: bool  # Completion status (default: False)
```

### Operations

#### Create Task
- **Method**: `create_task(title: str, description: str = "") -> Task`
- **Input**: Title (required), Description (optional)
- **Output**: Created Task object with assigned ID
- **Behavior**: Creates a new task with auto-incremented ID and completion status set to False

#### Get All Tasks
- **Method**: `get_all_tasks() -> List[Task]`
- **Input**: None
- **Output**: List of all tasks
- **Behavior**: Returns all tasks in the system

#### Get Task by ID
- **Method**: `get_task(task_id: int) -> Optional[Task]`
- **Input**: Task ID
- **Output**: Task object if found, None otherwise
- **Behavior**: Returns the task with the specified ID

#### Update Task
- **Method**: `update_task(task_id: int, title: str = None, description: str = None) -> bool`
- **Input**: Task ID, new title (optional), new description (optional)
- **Output**: True if successful, False if task not found
- **Behavior**: Updates the specified task with new values

#### Delete Task
- **Method**: `delete_task(task_id: int) -> bool`
- **Input**: Task ID
- **Output**: True if successful, False if task not found
- **Behavior**: Removes the task with the specified ID

#### Mark Task Complete
- **Method**: `mark_task_complete(task_id: int) -> bool`
- **Input**: Task ID
- **Output**: True if successful, False if task not found
- **Behavior**: Sets the completion status to True

#### Mark Task Incomplete
- **Method**: `mark_task_incomplete(task_id: int) -> bool`
- **Input**: Task ID
- **Output**: True if successful, False if task not found
- **Behavior**: Sets the completion status to False

### Error Handling
- Invalid task IDs should return appropriate error indicators
- Empty titles should be handled gracefully
- Operations on non-existent tasks should return False or None as appropriate