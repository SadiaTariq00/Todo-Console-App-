# Data Model: In-Memory Python Console Todo Application

**Feature**: 001-todo-app
**Date**: 2025-12-30

## Task Entity

### Fields
- **id** (int): Auto-incremented unique identifier for the task
- **title** (str): Title of the task (required, non-empty)
- **description** (str): Description of the task (optional, can be empty)
- **completed** (bool): Completion status of the task (default: False)

### Validation Rules
- ID must be a positive integer
- Title must be a non-empty string (1+ characters)
- Description can be an empty string or contain text
- Completed status must be a boolean value

### State Transitions
- **Created**: New task with `completed=False` by default
- **Updated**: Task details (title, description) can be modified
- **Completed**: Task status changed from `False` to `True`
- **Reopened**: Task status changed from `True` to `False`
- **Deleted**: Task removed from storage

## Relationships
- The Task entity is managed by the TodoManager
- Each task has a unique ID within the application session
- Tasks are stored in-memory within the TodoManager instance

## Data Lifecycle
1. **Creation**: New task is instantiated with auto-incremented ID and default completion status
2. **Storage**: Task is stored in-memory in the TodoManager's task collection
3. **Access**: Tasks can be retrieved by their unique ID
4. **Modification**: Task details can be updated while maintaining the same ID
5. **Deletion**: Task is removed from memory and cannot be accessed
6. **Session End**: All tasks are lost when the application terminates (in-memory only)

## Constraints
- Each task must have a unique ID within the application session
- Task IDs are auto-incremented and never reused during the same session
- No persistence across application restarts (in-memory only)
- Maximum reasonable number of tasks limited by available memory